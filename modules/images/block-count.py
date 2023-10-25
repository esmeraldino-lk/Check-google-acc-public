import os
import cv2
import pytesseract

def extract_text_and_digit_from_region(image_path, x, y, width, height):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    region = gray[y:y+height, x:x+width]
    
    extracted_text = pytesseract.image_to_string(region)
    extracted_digit_str = ''.join(filter(str.isdigit, extracted_text.strip()))
    
    if extracted_digit_str:
        digit = int(extracted_digit_str)
    else:
        digit = None
    
    return extracted_text.strip(), digit

if __name__ == "__main__":
    image_folder = "images/devices"
    log_folder = "../logs"
    x, y, width, height = 620, 155, 280, 30
    
    if not os.path.exists(log_folder):
        os.makedirs(log_folder)

    devices_log_path = os.path.join(log_folder, "devices.txt")

    with open(devices_log_path, "w") as devices_log:
        for image_filename in os.listdir(image_folder):
            image_path = os.path.join(image_folder, image_filename)
            extracted_text, extracted_digit = extract_text_and_digit_from_region(image_path, x, y, width, height)

            if extracted_digit is not None and extracted_digit > 3:
                devices_log.write(f"Imagem: {image_filename}, Dígito: {extracted_digit}\n")

    print("Verificação concluída.")
