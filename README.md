# tinyOCR
Lightweight OCR for extracting text from images efficiently.

## Overview

Python-based Optical Character Recognition (OCR) tool that extracts text from images using OpenCV for preprocessing and Tesseract for text recognition. Supports adaptive image preprocessing including resizing, denoising, contrast enhancement, and histogram equalization, to improve OCR accuracy.

## Features

* Extracts text from images using Tesseract.
* Adaptive contrast and brightness adjustments for improved output.
* Saves preprocessed images and extracted text to disk.
* Accepts image input via command-line arguments.

## Installation
### Prerequisites
Before using TinyOCR, ensure the following dependencies are installed:
- **Python 3.6+**:    Download and install from [python.org](https://www.python.org).
- **OpenCV & pytesseract**: Install the dependencies using `pip`
      ```bash
       pip install opencv-python pytesseract
      ```
- **Tesseract OCR**: Install Tesseract OCR (System level dependency) and add to the system _Path_.
  - **Windows:**  
  Download Tesseract from the [Tesseract GitHub page](https://github.com/UB-Mannheim/tesseract/wiki).

  - **Linux:**  
  Install it using your package manager:
      ```bash
      sudo apt-get install tesseract-ocr
      ```
  
## Usage
Run the program from the command line:
    ```bash
    python tinyocr.py -i <imagepath>
    ```

## Troubleshooting
### Common Issues

  **TesseractNotFoundError**
  
  Ensure Tesseract OCR is installed and added to the system PATH.
  On Windows, add C:\Program Files\Tesseract-OCR to the PATH variable.

  **cv2.error** (Image not found)
  
  Verify the image path is correct and accessible.
  Use absolute paths to avoid ambiguity.

  **Unsatisfactory OCR Output**
  
  Ensure the image quality is sufficient (not blurry or overly noisy).
  Adjust the preprocessing steps, such as brightness and contrast.

## Contributions
Contributions are welcome! To contribute:

1. Fork the repository.
   Create a new branch for your feature or fix:
    ```bash
      git checkout -b feature-name
    ```
2. Commit your changes and push the branch:
    ```bash
      git add .
      git commit -m "Add your message here"
      git push origin feature-name
    ```
3. Open a pull request describing your changes.

Feel free to submit issues or feature requests via the GitHub Issues page.

