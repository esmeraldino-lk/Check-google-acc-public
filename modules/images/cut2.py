import cv2
import os

def generate_image_path(base_path, categories_path, image_name):
    return os.path.join(base_path, categories_path, image_name)

def crop_and_save(image_path, output_path, x, y, width, height):
    try:
        image = cv2.imread(image_path)
        roi = image[y:y+height, x:x+width]
        
        cv2.imwrite(output_path, roi)
        print(f"Região recortada salva em: {output_path}")
    except Exception as e:
        print(f"Erro ao recortar e salvar a imagem: {e}")

if __name__ == "__main__":
    basic_image_path = "../../output/images/"
    categories_path = "my-drive"
    image_name = "1-coordenadorlogdromos@gmail.com.png"
    log_image_folder = f"../../output/logs/images/{categories_path}/"

    if not os.path.exists(log_image_folder):
        os.makedirs(log_image_folder)

    x, y, width, height = 620, 155, 270, 30
    
    image_path = generate_image_path(basic_image_path, categories_path, image_name)
    cropped_image_path = generate_image_path(log_image_folder, categories_path, image_name.replace(".png", "_recortada.png"))

    crop_and_save(image_path, cropped_image_path, x, y, width, height)
