from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import undetected_chromedriver as uc
import time
import json
import drive_verification as drive
import monitoring
import os
import colors

timeout = 8

imagesFolderDevices = r'output/images/devices'
imagesFolderDrive = r'output/images/my-drive'
imagesFolderShare = r'output/images/share'
imagesFolderError = r'output/images/error'
logsFolderNavigation = r'output/logs/navigation'


#       VERIFY AND CREATE FOLDERS
folders = ["output","output//images","output//logs",imagesFolderShare,imagesFolderDevices,imagesFolderDrive,imagesFolderError,logsFolderNavigation]
for folder in folders:
    if not os.path.exists(folder):
        os.mkdir(folder)
        print(colors.c.YELLOW,"Created ", folder, " ",colors.c.WHITE)
    else:
        print(colors.c.GREEN,"Checked ", folder, " ",colors.c.WHITE)


#       OPEN AND READ JSON
with open("accounts.json",'r') as json_file:
    accounts = json.load(json_file)

#       START ACCOUNT
count = int(input("Start account: "))

#       LOOP
for account in accounts:
    email = accounts["conta{}".format(count)]["email"]
    passw = accounts["conta{}".format(count)]["senha"]

    print(colors.c.YELLOW,"[!]",colors.c.WHITE," Scanning {}".format(email), end="")

    #       STARTS LOGIN PROCESS
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--log-level=3')
    driver = uc.Chrome( browser_executable_path='chrome-win\chrome.exe',options=options)
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


    #       MAKE LOGIN AS CASE
    try:
        #class="VfPpkd-vQzf8d"
        WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, '//*[@id="idvPin"]')))
        print(colors.c.RED, "TWO STEP ACTIVATED!")
    except:
        print(colors.c.GREEN ,"Pass!", end="")

        driver.get("https://drive.google.com/drive/my-drive")

        #       DRIVE VERIFICATION
        drive.driveVerification(driver,imagesFolderDrive,imagesFolderShare,imagesFolderDevices,imagesFolderError,count,email,timeout)

        #       NAVIGATION MONITORING
        monitoring.monitorAcc(driver,timeout,email,logsFolderNavigation,count)

        #       LOG OUT
        driver.get("https://accounts.google.com/Logout?hl=pt-BR&continue=https://drive.google.com/drive/my-drive&service=writely&timeStmp=1692982336&secTok=.AG5fkS_ZyCbRRUzLM0pzhKpZ9AnXz5cFig&ec=GAdAMQ&hl=pt_BR")
        WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, '//*[@class="tgnCOd"]')))

    count = count+1
    driver.quit()

