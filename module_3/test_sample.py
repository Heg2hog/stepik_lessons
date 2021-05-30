#проверка на невозможность регистрации при неподходящем пароле
import time

from selenium import webdriver
driver = webdriver.Chrome()
#предусловие: браузер открыт на странице с регистрацией
driver.get("http://selenium1py.pythonanywhere.com/ru/accounts/login/")
browser = driver
mail = browser.find_element_by_name("registration-email")
#шаг первый: вводим e-mail для регистрации пользователя
mail.clear()
mail.send_keys("12345@gmail.com")
#шаг второй: вводим пароль для регистрации пользователя
password = browser.find_element_by_name("registration-password1")
password.clear()
password.send_keys("qwerty")
#шаг третий: подтверждаем пароль для регистрации пользователя
password = browser.find_element_by_name("registration-password2")
password.clear()
password.send_keys("qwerty")
button = browser.find_element_by_name("registration_submit")
#шаг четвертый: нажимаем кнопку "Зарегистрироваться"
button.click()
time.sleep(3)
#Ожидаемый результат: невозможность произвести регистрацию с неподходящим паролем
#Фактический результат совпадает с ожидаемым
#Закрытие страницы
browser.quit()
