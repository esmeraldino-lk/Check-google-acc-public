from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Screenshot import Screenshot


def driveVerification(driver,imagesFolder,count,email,timeout):
    try:

        #       MY DRIVE 
        WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, '//*[@class="a-b-Sh"]')))
        ob=Screenshot.Screenshot()
        
        hide_elements = ['id=gb','class=ZHllM','class=ALpC8b fVVp2c','class=S630me','class=Z7C2he','class=bwAv4d','class=oLzOxb']
        
        img=ob.full_screenshot(driver,save_path=imagesFolder,image_name="{}-{}.png".format(count,email), hide_elements=hide_elements)

        #       SHARED WITH ME PAGE
        driver.get("https://drive.google.com/drive/shared-with-me")
        WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, '//*[@class="NtzyH"]')))   
        
        hide_elements = ['id=gb','class=ZHllM','class=ALpC8b fVVp2c','class=S630me','class=Z7C2he','class=bwAv4d','class=oLzOxb']

        ob=Screenshot.Screenshot()
        img=ob.full_screenshot(driver,save_path=imagesFolder,image_name="{}-{}-share.png".format(count,email),hide_elements=hide_elements)

        #       DEVICES PAGE
        driver.get("https://myaccount.google.com/device-activity?continue=https%3A%2F%2Fmyaccount.google.com%2Fsecurity%3Fhl%3Dpt_PT&hl=pt_PT")
        WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, '//*[@role="main"]')))
        
        hide_elements = ['id=gb','class=VjFXz','class=EWuRAb OUzXuf','class=ikIPKb']
        
        ob=Screenshot.Screenshot()
        img=ob.full_screenshot(driver,save_path=imagesFolder,image_name="{}-{}-devices.png".format(count,email),hide_elements=hide_elements)
        
    except:

        ob=Screenshot.Screenshot()
        img=ob.full_screenshot(driver,save_path=imagesFolder,image_name="{}-{}-exception.png".format(count,email))
