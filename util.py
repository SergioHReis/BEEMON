import logging

def save_screenshot(driver, filename):
    driver.save_screenshot(filename)

def setup_logger():
    logging.basicConfig(filename='scraping.log', level=logging.INFO)
