from PIL import Image
import os

def load_image(image_path, size=(384, 384)):
    image = Image.open(image_path).convert("RGB")
    image = image.resize(size)
    return image

def get_image_paths(folder):
    supported = (".jpg", ".jpeg", ".png")
    return [os.path.join(folder, f) for f in os.listdir(folder) if f.lower().endswith(supported)]
