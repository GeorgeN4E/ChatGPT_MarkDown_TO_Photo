import cv2
import os

def select_crop_area(image_path, output_folder):
    img = cv2.imread(image_path)
    clone = img.copy()
    height, width = img.shape[:2]
    scale_factor = 0.3  # Adjust this value as needed
    resized_img = cv2.resize(img, (int(width * scale_factor), int(height * scale_factor)))
    
    def mouse_callback(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            original_y = int(y / scale_factor)  # Convert back to original coordinates
            cropped_img = clone[:original_y, :]
            output_path = os.path.join(output_folder, os.path.basename(image_path))
            cv2.imwrite(output_path, cropped_img)
            print(f"Cropped image saved: {output_path}")
            cv2.destroyAllWindows()
    
    cv2.imshow("Select Crop Point", resized_img)
    cv2.setMouseCallback("Select Crop Point", mouse_callback)
    cv2.waitKey(0)

def process_images(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(".jpg"):
            image_path = os.path.join(input_folder, filename)
            print(f"Processing {filename}...")
            select_crop_area(image_path, output_folder)

if __name__ == "__main__":
    input_folder = "Photos"  # Change this to your input folder
    output_folder = "cropped_images"  # Change this to your output folder
    process_images(input_folder, output_folder)