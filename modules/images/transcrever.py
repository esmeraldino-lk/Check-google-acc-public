import cv2
import pytesseract

def extract_text_and_digit_from_region(image_path, x, y, width, height):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    region = gray[y:y+height, x:x+width]  # Seleciona a região definida pelas coordenadas
    
    extracted_text = pytesseract.image_to_string(region)
    
    digit = int(''.join(filter(str.isdigit, extracted_text.strip())))
    
    return extracted_text.strip(), digit

if __name__ == "__main__":
    image_path = "2-aprendiz02dromos@gmail.com-devices.png"
    
    x, y, width, height = 620, 155, 280, 30
    
    extracted_text, extracted_digit = extract_text_and_digit_from_region(image_path, x, y, width, height)
    
    print("Dígito extraído da região definida pelas coordenadas:")
    print(extracted_digit)
