# Text retrieval from images (OCR)

# Libraries
import pytesseract
import cv2
import sys
import argparse
import os

### Helper method - to extract text from image

def extract_text(image_path):
    # Get image filename
    image_filename = os.path.basename(image_path)
    # Remove file extension
    file_root, _ = os.path.splitext(image_filename)    
    # Read image using opencv
    image = cv2.imread(image_path)
    # Check if image is None
    if image is None:
        print("Image not found")
        sys.exit()

    ## Preprocessing the image

    # Increase the size of the image
    image = cv2.resize(image, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
    # Save image to disk
    cv2.imwrite(f"resized_{file_root}.jpg", image)

    # Denoising the image 
    image = cv2.medianBlur(image, 3)
    # Save denoised image to disk
    cv2.imwrite(f"denoised_{file_root}.jpg", image)

    # Calculate the mean brightness of the image
    mean_brightness = cv2.mean(image)[0] # 0th index is for brightness
    # Adjust alpha and beta based on mean brightness
    if mean_brightness < 100:
        alpha = 1.5     # --- increase contrast
        beta = 50       # --- increase brightness
    elif mean_brightness > 150:
        alpha = 1.0     # --- no change in contrast
        beta = -50      # --- decrease brightness
    else:
        alpha = 1.0     # --- no change in contrast
        beta = 0        # --- no change in brightness
    # Apply alpha and beta to the image
    image = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)
    # Save adjusted image to disk
    cv2.imwrite(f"adjusted_{file_root}.jpg", image)

    # Convert image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Save grayscale image to disk
    cv2.imwrite(f"gray_{file_root}.jpg", gray_image)

    ## Extract text from image and saving it to disk
    text = pytesseract.image_to_string(gray_image)
    # Saving extracted text to disk 
    with open(f"extracted_text_{file_root}.txt", "w") as file:
        file.write(text)
    
    return text

### Main function

def main():
    # Creating argument parser
    parser = argparse.ArgumentParser(description="OCR using pytesseract")
    # Adding argument
    parser.add_argument("-i", "--image", required=True, help="Path to image file")
    # Parsing arguments
    args = parser.parse_args()
    # Extracting text from image
    text = extract_text(args.image)
    # Printing extracted text
    print(text)

### Entry point of the program
if __name__ == "__main__":
    main()