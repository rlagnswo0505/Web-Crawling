from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import urllib.request

driver = webdriver.Chrome()
driver.get("https://www.laneige.com/kr/ko/homme/")


imgs = driver.find_elements(By.CSS_SELECTOR, ".product-item__img")
count = 1
for img in imgs:
    try: 
        imgUrl = img.get_attribute('src')
        urllib.request.urlretrieve(imgUrl,str(count) + ".jpg")
        count += 1
    except:
        pass

driver.close()

