import os
import json
import torch
from tqdm import tqdm
from models.blip_loader import load_blip_model
from utils.image_utils import load_image, get_image_paths
from utils.export_utils import export_to_csv

def generate_caption(processor, model, image, device):
    inputs = processor(images=image, return_tensors="pt").to(device)
    with torch.no_grad():
        output = model.generate(**inputs)
    return processor.decode(output[0], skip_special_tokens=True)

def caption_images(image_folder="images/", output_json="outputs/captions.json"):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    processor, model = load_blip_model()
    model.to(device)

    image_paths = get_image_paths(image_folder)
    results = []

    for path in tqdm(image_paths, desc="Captioning images"):
        image = load_image(path)
        caption = generate_caption(processor, model, image, device)
        results.append({"image": os.path.basename(path), "caption": caption})

    with open(output_json, "w") as f:
        json.dump(results, f, indent=4)

    export_to_csv(results, path="outputs/captions.csv")
    print(f"✔ Captions saved to {output_json} and outputs/captions.csv")

if __name__ == "__main__":
    caption_images()
