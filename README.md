# Face Recognition Project

## Overview
This project implements a face recognition system using Python's `face_recognition` and `OpenCV` libraries. It identifies and matches faces from a directory of known faces with images in a directory of unknown faces. This project serves as a basic tool for face matching tasks and visualization.

---

## Features
- **Known Faces Management:** Encodes and stores face data from the `known_faces` directory.
- **Unknown Faces Processing:** Compares unknown faces from the `unknown_faces` directory with known encodings.
- **Face Matching:** Matches faces based on a customizable tolerance value.
- **Visual Feedback:** Draws bounding boxes and labels on matched faces in the output images.

---

## Project Structure
```
FaceRecognition/
├── known_faces/          # Subdirectories for each known person, containing their images.
├── unknown_faces/        # Directory containing images of unknown faces for recognition.
├── my_face_recognition_env/ # Virtual environment (not included in the repository).
├── face_recog_ex.py      # Main script for face recognition.
├── face_recog_test.py    # Test script to verify library imports and functionality.
├── requirements.txt      # List of dependencies.
```

---

## Setup Instructions

### Prerequisites
- Python 3.6 or higher
- `pip` (Python package installer)
- `virtualenv` (recommended for environment isolation)

### Installation
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/rare20/FaceRecognition.git
   cd FaceRecognition
   ```

2. **Create a Virtual Environment:**
   ```bash
   python -m venv my_face_recognition_env
   source my_face_recognition_env/bin/activate   # Linux/Mac
   my_face_recognition_env\Scripts\activate    # Windows
   ```

3. **Install Dependencies:**
   Install the required libraries from `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

4. **Prepare Directories:**
   - Add subdirectories for each known person inside `known_faces/`. Place their images in the respective folders.
   - Place images of unknown individuals in the `unknown_faces/` directory.

5. **Run the Script:**
   ```bash
   python face_recog_ex.py
   ```

---

## How It Works
1. **Loading Known Faces:**
   - Scans the `known_faces` directory, encodes the faces, and stores them in memory.
2. **Processing Unknown Faces:**
   - Scans the `unknown_faces` directory and attempts to match the faces with known encodings.
3. **Face Matching:**
   - Uses a tolerance value (default: `0.4`) to determine matches.
4. **Output Visualization:**
   - Displays matched faces with bounding boxes and labels using OpenCV.

---

## Key Parameters
- **TOLERANCE:** Adjusts strictness of face matching (default: `0.4`).
- **MODEL:** Specifies the face detection model (`cnn` for GPU or `hog` for CPU).
- **FRAME_THICKNESS & FONT_THICKNESS:** Customizes bounding box and label appearance.

---

## Example Usage
1. Add a folder `known_faces/JohnDoe/` containing images of John Doe.
2. Add images of unknown people to `unknown_faces/`.
3. Run the script to see matches:

```plaintext
Loading known faces...
Loaded and encoded John Doe's face from image1.jpg
Loaded 1 faces.
Processing unknown faces...
Match found: John Doe
```

---

## Dependencies
This project relies on the following Python libraries:
- `face_recognition`
- `opencv-python`
- `numpy`

All dependencies are listed in the `requirements.txt` file.

---

## Notes
- Ensure clear and well-lit images in `known_faces/` for better accuracy.
- Large images in `unknown_faces/` may impact processing speed.
- Use the `cnn` model for better results on GPU-enabled systems.

---

## Contributing
Contributions are welcome! Fork the repository and create a pull request. For significant changes, open an issue to discuss your ideas.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Acknowledgements
- Built using the [face_recognition](https://github.com/ageitgey/face_recognition) library by Adam Geitgey.
- Thanks to the OpenCV community for their tools and resources.

