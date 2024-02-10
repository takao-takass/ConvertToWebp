import os
from PIL import Image

def convert_to_webp(input_folder, output_folder):
    for filename in os.listdir(input_folder):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            img = Image.open(os.path.join(input_folder, filename))
            base_filename = os.path.splitext(filename)[0]  # Remove the extension
            img.save(os.path.join(output_folder, base_filename + '.webp'), 'webp')

# 使用例
convert_to_webp('images', 'images')
