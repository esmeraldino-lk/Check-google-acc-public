import cv2
import os

def crop_and_save(image_path, x, y, width, height):
    """
    Recorta a região de interesse (ROI) da imagem e salva em um novo arquivo.
    :param image_path: O caminho da imagem original.
    :param x: A coordenada x do canto superior esquerdo da ROI.
    :param y: A coordenada y do canto superior esquerdo da ROI.
    :param width: A largura da ROI.
    :param height: A altura da ROI.
    """
    image = cv2.imread(image_path)
    
    roi = image[y:y+height, x:x+width]  # Recorta a região de interesse
    
    cropped_image_path = os.path.join(log_image_folder, f"{image_name.replace('.png', '_recortada.png')}")
    
    cv2.imwrite(cropped_image_path, roi)
    
    print(f"Região recortada salva em: {cropped_image_path}")

if __name__ == "__main__":
    basic_image_path = "../../output/images"
    categories_path = "my-drive"
    image_name = "1-coordenadorlogdromos@gmail.com.png"
    log_image_folder = os.path.join("../../output/logs/images", categories_path)
    image_path = os.path.join(basic_image_path, categories_path, image_name)
    
    if not os.path.exists(log_image_folder):
        os.makedirs(log_image_folder)

    
    x, y, width, height = 620, 155, 270, 30 # Defina as coordenadas e dimensões da ROI
    
    crop_and_save(image_path, x, y, width, height)