from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager не запускается из за этого

import time

link = "http://suninjuly.github.io/registration2.html"

try:
    #browser = webdriver.Chrome(ChromeDriverManager().install()) смотри выше
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля

    input1 = browser.find_element_by_css_selector(".first_block .form-control.first")
    input1.send_keys("111")
    input2 = browser.find_element_by_css_selector(".first_block .form-control.second")
    input2.send_keys("123")
    input3 = browser.find_element_by_css_selector(".first_block .form-control.third")
    input3.send_keys("144")
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
