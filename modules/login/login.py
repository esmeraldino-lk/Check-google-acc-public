from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
import time
import json
import drive_verification as drive
import monitoring

timeout = 8
imagesFolder = r'images/images/'


#       OPEN AND READ JSON
with open("modules\\accounts.json",'r') as json_file:
    accounts = json.load(json_file)

#       LOOP
count = 1
for account in accounts:
    email = accounts["conta{}".format(count)]["email"]
    passw = accounts["conta{}".format(count)]["senha"]

    print("[!] Scanning {}".format(email))

    #       STARTS LOGIN PROCESS

    driver = uc.Chrome( browser_executable_path='chrome-win\chrome.exe')
    driver.delete_all_cookies()
    driver.get("https://drive.google.com/drive/my-drive")

    #       ENTER E-MAIL
    WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, '//*[@id="identifierId"]'))).send_keys(email)
    driver.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button/span').click()

    #       ENTER PASSW
    senha_input = WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')))
    driver.execute_script(f"arguments[0].value='{passw}'", senha_input)
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="passwordNext"]/div/button/span').click()
    
    drive.driveVerification(driver,imagesFolder,count,email,timeout)

    monitoring.monitorAcc(driver,timeout,email)

    #       LOG OUT
    driver.get("https://accounts.google.com/Logout?hl=pt-BR&continue=https://drive.google.com/drive/my-drive&service=writely&timeStmp=1692982336&secTok=.AG5fkS_ZyCbRRUzLM0pzhKpZ9AnXz5cFig&ec=GAdAMQ&hl=pt_BR")
    WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, '//*[@class="tgnCOd"]')))

    count = count+1
    driver.quit()