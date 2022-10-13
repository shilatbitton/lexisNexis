from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time



def lexisNexis():
    government_list=[]
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://risk.lexisnexis.com/")
    driver.find_element(By.LINK_TEXT,'Our Products').click()
    time.sleep(10)
    dropdown_select=driver.find_element(By.CSS_SELECTOR,'.ais-hierarchical-menu--header')
    dropdown_select.click()
    time.sleep(10)
    select= driver.find_element(By.LINK_TEXT,'Government')
    select.click()
    time.sleep(10)
    items_list=driver.find_element(By.CSS_SELECTOR,'.product-index-items')
    items=items_list.find_elements(By.TAG_NAME,"li")
    for i in items:
        text=i.find_elements(By.TAG_NAME,"h2")
        government_list.append(text[0].text)
    return government_list


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(lexisNexis())


