from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def scrape_quotes(url, xpath_expression):
    options = Options()
    options.headless = False  # Defina como True para ocultar a interface gráfica
    driver = webdriver.Chrome(options=options)
    
    try:
        driver.get(url)
        time.sleep(2)
        
        data = []
        for item in driver.find_elements(By.XPATH, xpath_expression):
            quote_info = {
                'text': item.find_element(By.XPATH, ".//span[@class='text']").text.strip(),
                'author': item.find_element(By.XPATH, ".//small[@class='author']").text.strip(),
                'tags': [tag.text.strip() for tag in item.find_elements(By.XPATH, ".//div[@class='tags']/a")]
            }
            data.append(quote_info)

        return data
    
    finally:
        driver.quit()
