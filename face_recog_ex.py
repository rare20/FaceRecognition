import face_recognition
import os
import cv2

# Directories for known and unknown faces
KNOWN_FACES_DIR = "known_faces"
UNKNOWN_FACES_DIR = "unknown_faces"

# Constants
TOLERANCE = 0.4
FRAME_THICKNESS = 3
FONT_THICKNESS = 2
MODEL = "cnn"

print("Loading known faces...")

# Lists to store known face encodings and names
known_faces = []
known_names = []

# Load known faces
for name in os.listdir(KNOWN_FACES_DIR):
    # Skip hidden files and system files
    if name.startswith('.'):
        continue
    
    # Ensure it's a directory
    person_dir = os.path.join(KNOWN_FACES_DIR, name)
    if not os.path.isdir(person_dir):
        continue

    # Iterate through each person's images
    for filename in os.listdir(person_dir):
        # Skip hidden files
        if filename.startswith('.'):
            continue
            
        # Construct proper file path
        image_path = os.path.join(person_dir, filename)
        
        try:
            # Load the image and encode the face
            image = face_recognition.load_image_file(image_path)
            encodings = face_recognition.face_encodings(image)
            
            if encodings:  # Ensure at least one face was found
                encoding = encodings[0]
                known_faces.append(encoding)
                known_names.append(name)
                print(f"Loaded and encoded {name}'s face from {filename}")
            else:
                print(f"No face found in {filename}")
                
        except Exception as e:
            print(f"Error processing {image_path}: {str(e)}")

print(f"Loaded {len(known_faces)} faces.")
print("Processing unknown faces...")

# Process unknown faces
for filename in os.listdir(UNKNOWN_FACES_DIR):
    # Skip hidden files
    if filename.startswith('.'):
        continue
        
    print(f"Processing {filename}")
    image_path = os.path.join(UNKNOWN_FACES_DIR, filename)
    
    try:
        # Load the unknown image
        image = face_recognition.load_image_file(image_path)
        
        # Find face locations and encodings in the image
        locations = face_recognition.face_locations(image, model=MODEL)
        encodings = face_recognition.face_encodings(image, locations)
        
        # Convert the image from RGB to BGR for OpenCV
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        
        # Compare each face encoding to known faces
        for face_encoding, face_location in zip(encodings, locations):
            results = face_recognition.compare_faces(known_faces, face_encoding, TOLERANCE)
            match = None

            if True in results:  # If a match is found
                match = known_names[results.index(True)]
                print(f"Match found: {match}")

                # Draw rectangle around the face
                top_left = (face_location[3], face_location[0])
                bottom_right = (face_location[1], face_location[2])
                color = [0, 255, 0]  # Green color for rectangle
                cv2.rectangle(image, top_left, bottom_right, color, FRAME_THICKNESS)

                # Draw label with the name
                top_left = (face_location[3], face_location[2] + 22)
                bottom_right = (face_location[1], face_location[2] + 22)
                cv2.rectangle(image, top_left, bottom_right, color, cv2.FILLED)
                cv2.putText(
                    image, match, (face_location[3] + 10, face_location[2] + 15),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (200, 200, 200), FONT_THICKNESS
                )

        # Display the image
        cv2.imshow(filename, image)
        cv2.waitKey(1000)  # Display for 10 seconds
        cv2.destroyWindow(filename)
        
    except Exception as e:
        print(f"Error processing {image_path}: {str(e)}")