from selenium.webdriver.common.by import By
from .pages.main_page import MainPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина



#link = "http://selenium1py.pythonanywhere.com/"
#def go_to_login_page(browser):
#    login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
#    login_link.click()
#def test_guest_can_go_to_login_page(browser):
#    browser.get(link)
#    go_to_login_page(browser)

# def test_guest_can_go_to_login_page(browser):
#    link = "http://selenium1py.pythonanywhere.com/"
#    browser.get(link)
#    login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
#    login_link.click()
