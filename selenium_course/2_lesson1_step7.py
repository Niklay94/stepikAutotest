from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    # Ваш код, который заполняет обязательные поля

    findElement = browser.find_element_by_id("treasure")
    x_element_input1 = findElement.get_attribute("valuex")
    print(x_element_input1)
    #x_element_input1 = browser.find_element_by_id("input_value")
    #x = x_element_input1.text
    y = calc(x_element_input1)

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
    
    input2 = browser.find_element_by_id("robotCheckbox")
    input2.click()

    input3 = browser.find_element_by_css_selector("[value='robots']")
    input3.click()
    
    #input5 = browser.find_element_by_xpath('//input[@placeholder="Input your last name"]')
    #input5.send_keys("Ivanov")
    
    #input6 = browser.find_element_by_xpath('//input[@placeholder="Input your email"]')
    #input6.send_keys("ivan@gmail.com")
    
    #input4 = browser.find_element_by_id("country")
    #input4.send_keys("Russia")

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
    