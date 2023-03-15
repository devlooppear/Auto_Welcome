from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

USER = "<you put here your user>"
PASSWORD = "<you put here your password>"
MESSAGE = "Olá, obrigado por conectar comigo no LinkedIn!"

def Iniciate_browser():
    servico = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=servico)
    return driver

def Navigate_to_loguin(driver):
    driver.get("https://www.linkedin.com/home")

def Inserting_in_loguin(driver):
    username = driver.find_element(By.XPATH, '//*[@id="session_key"]')
    password = driver.find_element(By.XPATH, '//*[@id="session_password"]')
    sleep(2)
    username.send_keys(USER)
    password.send_keys(PASSWORD)
    password.send_keys(Keys.RETURN)
    sleep(2)

def Navigate_to_connections_page(driver):
    profile = driver.find_element(By.XPATH, '//*/div[@class="t-16 t-black t-bold"]')
    profile.click()
    sleep(2)
    connections_view = driver.find_element(By.XPATH, '//*/span/span[@class="t-bold"]')
    connections_view.click()
    sleep(3)

def Loop_connections_pages(driver):
    for page_number in range(1, 241, 1):

        connections = driver.find_elements(By.XPATH, '//*/div[@class="entity-result__item"]')

        for i, connection in enumerate(connections, start=1):

            message_button = connection.find_element(By.XPATH, f'//*/li[{i}]/div/div/div[3]/div/div/button')
            message_button.click()
            sleep(0.5)

            message_input = driver.find_element(By.XPATH, '//*/div[@aria-label="Escreva uma mensagem"]')
            message_input.send_keys(MESSAGE)
            sleep(0.5)
            send_button_enter = driver.find_element(By.XPATH, '//*/button[@class="msg-form__send-button artdeco-button artdeco-button--1"][@type="submit"]')
            send_button_enter.click()

            send_button_exit = driver.find_element(By.XPATH, '//*/button[@class="msg-overlay-bubble-header__control artdeco-button artdeco-button--circle artdeco-button--muted artdeco-button--1 artdeco-button--tertiary ember-view"]')
            send_button_exit.click()

        next_page_button = driver.find_elements(By.XPATH, f'//button[@aria-label="Página {page_number + 1}"]')
        if not next_page_button:
            break
        next_page_button[0].click()
        sleep(2)

def main():

    driver = Iniciate_browser()
    Navigate_to_loguin(driver)
    Inserting_in_loguin(driver)
    Navigate_to_connections_page(driver)
    Loop_connections_pages(driver)

if __name__ == '__main__':
    main()