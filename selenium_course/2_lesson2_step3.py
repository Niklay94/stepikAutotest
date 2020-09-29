from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select

def calc(x,y):
  return str(int(x)+int(y))

try: 
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    findElement_x = browser.find_element_by_id("num1")
    findElement_y = browser.find_element_by_id("num2")
    x = findElement_x.text
    y = findElement_y.text
    answer = calc(int(x),int(y))
    
    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(answer)
    
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    