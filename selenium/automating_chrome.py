from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

def test_drive_manager_chrome():
    service = Service(executable_path=ChromeDriverManager().install())

    driver = webdriver.Chrome(service=service)


# test_drive_manager_chrome()

def get_random_quote():
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    driver.get("https://iamcodefoxx.github.io/Random-Quote-Generator/")

    print("Currently in", driver.title)

    button = driver.find_element(By.ID, "generate")
    button.click()
    
    driver.implicitly_wait(1)

    quote = driver.find_element(By.ID, "quote").get_attribute("textContent")
    print("Quote:", quote)
    
    author = driver.find_element(By.ID, "author").get_attribute("textContent")
    print("Author:", author)

    driver.quit()

get_random_quote()
