from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import urllib.request

driver = webdriver.Chrome()
driver.get("https://www.google.co.kr/imghp?hl=ko&ogbl")
elem = driver.find_element(By.NAME, "q")
elem.send_keys("고양이")
elem.send_keys(Keys.RETURN)

# 브라우저 스크롤 맨 밑까지 내리기
SCROLL_PAUSE_TIME = 0.5

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

imgs = driver.find_elements(By.CSS_SELECTOR, ".rg_i.Q4LuWd")
count = 1
for img in imgs:
    img.click()
    time.sleep(3)
    imgUrl = driver.find_element(By.CSS_SELECTOR, ".n3VNCb").get_attribute('src')
    urllib.request.urlretrieve(imgUrl,str(count) + ".jpg")
    count += 1



# assert "Python" in driver.title
# elem = driver.find_element(By.NAME, "q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()