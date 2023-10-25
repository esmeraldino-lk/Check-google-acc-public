import os
import cv2
import pytesseract

def extract_text(image_path, regions_of_interest):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    texts = []

    for region in regions_of_interest:
        x, y, width, height = region
        region_image = gray[y:y+height, x:x+width]
        text = pytesseract.image_to_string(region_image)
        texts.append(text.strip())

    return texts


def compare_text_regions(image_paths, threshold=0.2, specific_text=None):
    anomalies = []

    for image_path in image_paths:
        text = extract_text(image_path)
        # Código para comparar o texto e identificar anomalias
        # ...

    return anomalies

if __name__ == "__main__":
    current_directory = os.path.dirname(os.path.abspath(__file__))
    input_folder = os.path.join(current_directory, "images")
    output_folder = os.path.join(current_directory, "../logs")

    image_files = os.listdir(input_folder)
    image_paths = [os.path.join(input_folder, filename) for filename in image_files]

    anomalies = compare_text_regions(image_paths)

    if anomalies:
        with open(os.path.join(output_folder, "text_anomalies.txt"), "w") as f:
            f.write("Text Anomalies:\n")
            for anomaly in anomalies:
                f.write(f"{anomaly}\n")
