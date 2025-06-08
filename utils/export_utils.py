import csv

def export_to_csv(data, path="outputs/captions.csv"):
    with open(path, "w", newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["image", "caption"])
        writer.writeheader()
        writer.writerows(data)
