import cv2
import pytesseract
import json

def extract_text(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Usando pytesseract para extrair texto da imagem
    text = pytesseract.image_to_string(gray)
    
    return text

def compare_images(image_paths):
    texts = [extract_text(path) for path in image_paths]
    
    anomalies = []
    for i, text in enumerate(texts):
        different_texts = []
        for j, other_text in enumerate(texts):
            if i != j and text != other_text:
                different_texts.append(j)
        
        if different_texts:
            anomalies.append((i, different_texts))
    
    return anomalies

if __name__ == "__main__":
    with open("accounts.json", "r") as json_file:
        data = json.load(json_file)
    
    email_list = []
    for num, (key, account) in enumerate(data.items(), start=1):
        email = account["email"]
        email_list.append((num, email))
    
    for num, email in email_list:
        image_paths = [
            f"{num}-{email}.png",
            f"{num}-{email}-devices.png",
            f"{num}-{email}-share.png"
        ]
        
        anomalies = compare_images(image_paths)
        
        if anomalies:
            with open(f"differences_{email}.txt", "w") as f:
                for i, different_texts in anomalies:
                    f.write(f"Anomaly in Image {i+1}-{email}.png\n")
                    for j in different_texts:
                        f.write(f"   Different from Image {j+1}-{email}.png\n")
import cv2

def compare_similarity_regions(image_paths, threshold=0.2):
    anomalies = []

    for image_path in image_paths:
        # Aqui você pode implementar a comparação de semelhança entre regiões
        # Se a divergência for maior que 20%, adicione o caminho da imagem à lista de anomalias
        # Exemplo: if condition:
        #               anomalies.append(image_path)

    return anomalies

if __name__ == "__main__":
    # Coloque aqui o código para ler as imagens e definir as regiões específicas
    # para cada imagem que você deseja comparar

    image_paths = ["image1.png", "image2.png", "image3.png"]
    anomalies = compare_similarity_regions(image_paths)

    if anomalies:
        with open("similarity_anomalies.txt", "w") as f:
            f.write("Similarity Anomalies:\n")
            for anomaly in anomalies:
                f.write(f"{anomaly}\n")
