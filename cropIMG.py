import cv2
import os
import re
from PIL import Image

def remove_metadata(image_path):
    image = Image.open(image_path)
    data = list(image.getdata())
    new_image = Image.new(image.mode, image.size)
    new_image.putdata(data)
    return new_image

def select_crop_area(image_path, output_folder):
    img = cv2.imread(image_path)
    if img is None:
        print(f"Could not read image: {image_path}")
        return

    clone = img.copy()
    height, width = img.shape[:2]
    scale_factor = 0.1  # Adjust this value as needed
    resized_img = cv2.resize(img, (int(width * scale_factor), int(height * scale_factor)))
    
    def mouse_callback(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            original_y = int(y / scale_factor)  # Convert back to original coordinates
            cropped_img = clone[:original_y, :]
            output_path = os.path.join(output_folder, os.path.basename(image_path))
            cv2.imwrite(output_path, cropped_img)
            
            # Optionally remove metadata (currently commented out)
            """
            clean_image = remove_metadata(output_path)
            clean_image.save(output_path)
            """
            
            print(f"Cropped image saved without metadata: {output_path}")
            cv2.destroyAllWindows()
    
    cv2.imshow("Select Crop Point", resized_img)
    cv2.setMouseCallback("Select Crop Point", mouse_callback)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def natural_keys(text):
    """
    alist.sort(key=natural_keys) sorts in human order.
    Example:
        "page_2.jpg" comes before "page_10.jpg"
    """
    return [int(c) if c.isdigit() else c for c in re.split(r'(\d+)', text)]

def process_images(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # List only jpg files and sort them naturally
    image_files = [
        filename for filename in os.listdir(input_folder)
        if filename.lower().endswith(".jpg")
    ]
    image_files.sort(key=natural_keys)
    
    for filename in image_files:
        image_path = os.path.join(input_folder, filename)
        print(f"Processing {filename}...")
        select_crop_area(image_path, output_folder)

if __name__ == "__main__":
    input_folder = "Content/extracted_img"         # Change this to your input folder
    output_folder = "Content/croped_extracted_images"  # Change this to your output folder
    process_images(input_folder, output_folder)
