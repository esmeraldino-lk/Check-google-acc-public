import cv2
import os

def crop_and_save(image_path, x, y, width, height):
    image = cv2.imread(image_path)
    
    roi = image[y:y+height, x:x+width]  # Recorta a região de interesse
    
    cropped_image_path = image_path.replace(".png", "_recortada.png")
    cv2.imwrite(cropped_image_path, roi)
    
    print(f"Região recortada salva em: {cropped_image_path}")

if __name__ == "__main__":
    image_path = "2-aprendiz02dromos@gmail.com-devices.png"
    
    x, y, width, height = 620, 155, 270, 30 # Defina as coordenadas e dimensões da ROI
    
    crop_and_save(image_path, x, y, width, height)