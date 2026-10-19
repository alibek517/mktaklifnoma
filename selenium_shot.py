import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def take_shot():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    html_path = f"file:///{os.path.join(current_dir, 'poster.html').replace('\\', '/')}"
    output_path = os.path.join(current_dir, "taklifnoma_rasm.png")

    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=860,1350")
    options.add_argument("--force-device-scale-factor=2")
    options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

    driver = webdriver.Chrome(options=options)
    try:
        driver.get(html_path)
        time.sleep(3) # Wait for webfonts to load
        elem = driver.find_element("id", "poster")
        elem.screenshot(output_path)
        print(f"SELENIUM_SUCCESS: {output_path}")
    finally:
        driver.quit()

if __name__ == "__main__":
    take_shot()
