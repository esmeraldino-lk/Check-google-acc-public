from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import colors

def monitorAcc(driver,timeout,email,logsFolderNavigation,count):
    
    #       SEARCH GOOGLE LOG
    driver.get("https://myactivity.google.com/myactivity?hl=pt-BR&product=19")
    WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, '//*[@class="l8sGWb"]')))

    #       SCROLL DOWN PAGE
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)

    #       FIND FOR ELEMENTS
    logs = driver.find_elements(By.XPATH, '//*[@class="l8sGWb"]')
    horas = driver.find_elements(By.XPATH, '//*[@class="H3Q9vf XTnvW"]')

    #       FORMAT LOGS
    countH = 0
    for hora in horas:
        hora = hora.text
        try:
            horas[countH] = hora.replace(' • • Detalhes', '')
            countH +=1
        except:
            horas[countH] = hora.replace(' • Detalhes', '')
            countH +=1
    logFull = []
    for countL in range(len(logs)):
        logFull.append('[' + horas[countL] + ']  - ' + logs[countL].text)

    #       CREATE LOG FILE AND WRITE IN UTF-8
    with open("{}\\{}-{}-google-search.log".format(logsFolderNavigation,count,email), 'w', encoding='utf-8') as outputFile:

        for item in logFull:
            outputFile.write(item + '\n')
    print(colors.c.GREEN,'  Log created!')