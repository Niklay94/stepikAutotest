from selenium import webdriver
import time
import math
#from selenium.webdriver.support.ui import Select

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_element_input1 = browser.find_element_by_id("input_value")
    x = x_element_input1.text
    y = calc(x)

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
    
    input2 = browser.find_element_by_id("robotCheckbox")
    browser.execute_script("return arguments[0].scrollIntoView(true);", input2)
    input2.click()

    input3 = browser.find_element_by_css_selector("[value='robots']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", input3)
    input3.click()

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
    