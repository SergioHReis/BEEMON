from util import setup_logger, save_screenshot
from collector import scrape_quotes
from storage import save_to_database, create_dataframe, save_to_json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import schedule
import time

def job():
    setup_logger()

    quotes_url = 'http://quotes.toscrape.com/'
    quotes_xpath_expression = "//div[@class='quote']"

    options = Options()
    options.headless = False  # Defina como True para ocultar a interface gráfica
    driver = webdriver.Chrome(options=options)

    try:
        # Aguarde até que a página seja totalmente carregada
        driver.get(quotes_url)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, quotes_xpath_expression)))

        # Coleta os dados, salva no banco, cria dataframe e gera arquivo JSON
        data = scrape_quotes(quotes_url, quotes_xpath_expression)
        save_to_database(data)
        create_dataframe(data)
        save_to_json(data)

        # Tira um screenshot do site "Quotes" como prova da consulta
        save_screenshot(driver, 'quotes_screenshot.png')

        logging.info(f'Raspagem de {quotes_url} concluída com sucesso!')
    
    except Exception as e:
        logging.error(f'Erro durante a raspagem de {quotes_url}: {e}')

    finally:
        driver.quit()

# Agendar a execução diariamente às 10:00 AM
schedule.every().day.at("10:00").do(job)

if __name__ == '__main__':
    setup_logger()

    quotes_url = 'http://quotes.toscrape.com/'
    quotes_xpath_expression = "//div[@class='quote']"

    options = Options()
    options.headless = False  # Defina como True para ocultar a interface gráfica
    driver = webdriver.Chrome(options=options)

    try:
        # Aguarde até que a página seja totalmente carregada
        driver.get(quotes_url)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, quotes_xpath_expression)))

        # Coleta os dados, salva no banco, cria dataframe e gera arquivo JSON
        data = scrape_quotes(quotes_url, quotes_xpath_expression)
        save_to_database(data)
        create_dataframe(data)
        save_to_json(data)

        # Tira um screenshot do site "Quotes" como prova da consulta
        save_screenshot(driver, 'quotes_screenshot.png')

        logging.info(f'Raspagem de {quotes_url} concluída com sucesso!')
    
    except Exception as e:
        logging.error(f'Erro durante a raspagem de {quotes_url}: {e}')

    finally:
        driver.quit()

    # Agendar a e'xecução di'ariamente às 10:00 AM
    schedule.every().day.at("10:00").do(job)

    # Manter o script em execução continuamente
    while True:
        schedule.run_pending()
        time.sleep(1)
