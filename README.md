# Virtual Mirror
## Flask Video Streaming with Face Detection and Overlay
This Flask application provides real-time video streaming from a webcam with optional face detection and overlay of images on detected faces. The overlays are different styles of glasses that can be chosen from a web interface.

### Features

* Real-time video streaming from a webcam.
* Face detection using Haar cascades.
* Overlay of images (glasses) on detected faces.
* Simple web interface to choose different overlays.

### Notes
* Ensure your webcam is properly connected and accessible by OpenCV.
* The application uses Haar cascades for face detection which may not be the most accurate or fastest method. For better performance, consider using more advanced techniques like deep learning-based face detectors.
### License
This project is licensed under the MIT License. See the LICENSE file for details.
