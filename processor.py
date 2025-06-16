#!/usr/bin/env python3

def download_images(input="links.txt", dest_folder="images"):
    import os
    import requests
    """
    Downloads images from URLs listed in links.txt and saves them to the 'images' folder.
    Each image is saved with a unique filename based on its order in the list.
    """
    if not os.path.exists(input):
        print(f"File {input} not found. Please create it with image URLs.")
        return
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
        print(f"Created {dest_folder} folder.")
    else:
        print(f"Using existing folder: {dest_folder}")

    urls = []
    with open(input, "r") as file:
        urls = [line.strip() for line in file if line.strip()]
    if not urls:
        print("No URLs found in the file.")
        return
    print(f"Found {len(urls)} URLs to process.")


    for i, url in enumerate(urls):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()

        except requests.RequestException as e:
            print(f"Error accessing the first URL: {urls[0]}. Error: {e}")
            return
        
        filename = dest_folder + "/" + f"image_{i+1}.jpg"
        
        with open(filename, "wb") as f:
             f.write(response.content)

def OCR():
    import pytesseract
    from PIL import Image
    import os

    input_folder = "images"
    output_file = "extracted_text.txt"

    if not os.path.exists(input_folder):
        print(f"Folder {input_folder} does not exist.")
        return

    with open(output_file, "w") as out_file:
        for filename in os.listdir(input_folder):
            if filename.endswith(".jpg"):
                img_path = os.path.join(input_folder, filename)
                try:
                    img = Image.open(img_path)
                    text = pytesseract.image_to_string(img)
                    out_file.write(f"Text from {filename}:\n{text}\n\n")
                except Exception as e:
                    print(f"Error processing {filename}: {e}")

    print(f"Text extracted to {output_file}.")
        
    
    

    
download_images()

