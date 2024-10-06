import os
from PIL import Image

def merged(photos):

    image_paths = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith(('.png', '.jpg', '.jpeg'))]
    if not image_paths:
        print("no photos r there")
        return
    opened_images = [Image.open(img) for img in image_paths]
    total_width = sum(img.width for img in opened_images)
    max_height = max(img.height for img in opened_images)
    new_img = Image.new('RGB', (total_width, max_height), color=(255, 255, 255))
    x_offset = 0
    for img in opened_images:
        y_offset = (max_height - img.height) // 2
        new_img.paste(img, (x_offset, y_offset))
        x_offset += img.width
    new_img.show()
    new_img.save('merged.jpg')
folder_path = input("folder: ")
merged(photos)
