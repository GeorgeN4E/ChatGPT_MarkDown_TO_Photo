from pdf2image import convert_from_path
from concurrent.futures import ProcessPoolExecutor, as_completed
import os

def save_page(pdf_path, output_folder, dpi, poppler_path, page_number):
    # Convert only the specified page
    images = convert_from_path(
        pdf_path,
        dpi=dpi,
        poppler_path=poppler_path,
        first_page=page_number,
        last_page=page_number
    )
    image = images[0]
    image_path = os.path.join(output_folder, f"page_{page_number}.jpg")
    image.save(image_path, 'JPEG')
    return f"Saved {image_path}"

def pdf_to_images(pdf_path, output_folder, quality='high'):
    quality_map = {
        'low': 50,
        'medium': 100,
        'high': 300,
        'full': 600
    }
    dpi = quality_map.get(quality, 300)
    poppler_path = r"C:\poppler\Library\bin"
    
    # Get total number of pages
    # You can use pdfinfo_from_path to get metadata if needed
    images_for_info = convert_from_path(pdf_path, dpi=50, poppler_path=poppler_path)
    total_pages = len(images_for_info)
    print(f"Total pages: {total_pages}")
    
    os.makedirs(output_folder, exist_ok=True)
    
    with ProcessPoolExecutor() as executor:
        futures = [
            executor.submit(save_page, pdf_path, output_folder, dpi, poppler_path, page_number)
            for page_number in range(1, total_pages + 1)
        ]
        for future in as_completed(futures):
            print(future.result())
    
    print("All pages processed.")

if __name__ == "__main__":
    pdf_to_images(r"Content\v3 Curs 1-12_removed.pdf", "Content/extracted_img", quality='full')
