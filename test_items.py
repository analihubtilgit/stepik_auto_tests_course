from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_login_link_pass(browser):
    browser.get(link)
    time.sleep(20)
    welcome_text_elt = browser.find_element(By.CSS_SELECTOR, 'button[value="Ajouter au panier"]')
    welcome_text = welcome_text_elt.text
    assert welcome_text == "Ajouter au panier", "Should be no registretion"

