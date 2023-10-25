import os
import cv2
import pytesseract
from shutil import copy2

def extract_text_from_region(image_path, x, y, width, height):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    region = gray[y:y+height, x:x+width]
    extracted_text = pytesseract.image_to_string(region)
    extracted_text_clean = "".join(c for c in extracted_text if c.isalnum())
    expected_text_clean = "".join(c for c in expected_text if c.isalnum())

    if extracted_text_clean.lower() != expected_text_clean.lower():
        return extracted_text
    else:
        return ""

    
    return extracted_text.strip()

if __name__ == "__main__":
    image_folder = "images/devices"
    expected_text = "Texto Esperado"
    x, y, width, height = 920, 150, 400, 130

    extracted_texts = {}

    for image_filename in os.listdir(image_folder):
        if image_filename.endswith("devices.png"):
            image_path = os.path.join(image_folder, image_filename)
            extracted_text = extract_text_from_region(image_path, x, y, width, height)
            extracted_texts[image_filename] = extracted_text

    divergence_log = "divergences.txt"
    with open(divergence_log, "w") as log_file:
        log_file.write("Divergências Encontradas:\n\n")
        for image_filename, extracted_text in extracted_texts.items():
            if extracted_text != expected_text:
                log_file.write(f"Imagem: {image_filename}\n")
                log_file.write(f"Texto Extraído:\n{extracted_text}\n")
                log_file.write(f"Texto Esperado:\n{expected_text}\n\n")

    print("Verificação concluída. Divergências registradas em divergences.txt.")