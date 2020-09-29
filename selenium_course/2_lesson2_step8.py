from selenium import webdriver
import time
import os 

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    input4 = browser.find_element_by_xpath('//input[@placeholder="Enter first name"]')
    input4.send_keys("Ivan")

    input5 = browser.find_element_by_xpath('//input[@placeholder="Enter last name"]')
    input5.send_keys("Ivanov")
    
    input6 = browser.find_element_by_xpath('//input[@placeholder="Enter email"]')
    input6.send_keys("ivan@gmail.com")

    input7 = browser.find_element_by_xpath('//input[@type="file"]')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'text.txt')
    input7.send_keys(file_path)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    