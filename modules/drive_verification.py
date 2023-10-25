from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Screenshot import Screenshot

def hideElements(driver,elements):

    for element in elements:
        try:
            try:
                #if str('id=') in element:
                #element = element.replace('id=','')
                element = driver.find_element(By.ID, element)
            except:        
                #if str('class=') in element:
                #element = element.replace('class=','')
                element = driver.find_element(By.CLASS_NAME, element)

            driver.execute_script("arguments[0].style.display = 'none';", element)
        except:
            pass

def driveVerification(driver,imagesFolderDrive,imagesFolderShare,imagesFolderDevices,imagesFolderError,count,email,timeout):
    try:

        #MY DRIVE#
        WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, '//*[@class="a-b-Sh"]')))
        ob=Screenshot.Screenshot()

        #       HIDE PAGE ELEMENTS
        elements = ['gb','ZHllM','ALpC8b fVVp2c','S630me','Z7C2he','bwAv4d','oLzOxb']
        hideElements(driver,elements)

        #       SCREENSHOT
        img=ob.full_screenshot(driver,save_path=imagesFolderDrive,image_name="{}-{}.png".format(count,email))

        #SHARED WITH ME PAGE#
        driver.get("https://drive.google.com/drive/shared-with-me")
        WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, '//*[@class="NtzyH"]')))   

        #       HIDE PAGE ELEMENTS
        elements = ['gb','ZHllM','ALpC8b fVVp2c','S630me','Z7C2he','bwAv4d','oLzOxb','ak25Me','a-da-Mf-B','a-b-K']
        hideElements(driver,elements)

        #       SCREENSHOT
        ob=Screenshot.Screenshot()
        img=ob.full_screenshot(driver,save_path=imagesFolderShare,image_name="{}-{}-share.png".format(count,email))

        #DEVICES PAGE#
        driver.get("https://myaccount.google.com/device-activity?continue=https%3A%2F%2Fmyaccount.google.com%2Fsecurity%3Fhl%3Dpt_PT&hl=pt_PT")
        WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, '//*[@role="main"]')))

        #       HIDE PAGE ELEMENTS
        elements = ['gb','VjFXz','EWuRAb','OUzXuf','ikIPKb','EWuRAb','gb_id','gb_cd','gb_od']
        hideElements(driver,elements)

        #       SCREESHOT
        ob=Screenshot.Screenshot()
        img=ob.full_screenshot(driver,save_path=imagesFolderDevices,image_name="{}-{}-devices.png".format(count,email))

    except:

        ob=Screenshot.Screenshot()
        img=ob.full_screenshot(driver,save_path=imagesFolderError,image_name="{}-{}-exception.png".format(count,email))
