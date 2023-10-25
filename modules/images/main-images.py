import subprocess

def run_script(script_name):
    subprocess.run(["python", script_name])

if __name__ == "__main__":
    # Executa cada um dos scripts em sequência
    run_script("script_text_compare.py")
    run_script("script_similarity_compare.py")
    run_script("script_centralize_images.py")
