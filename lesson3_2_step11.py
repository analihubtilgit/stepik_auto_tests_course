from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

class TestAbs(unittest.TestCase):
    def  test_abs1(self):
        browser = webdriver.Chrome()
        link = "   http://suninjuly.github.io/registration1.html"
        browser.get(link)
        input1 = browser.find_element(By.CLASS_NAME, 'form-control.first')
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your last name']")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.CLASS_NAME, 'form-control.third')
        input3.send_keys("Smolensk")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        time.sleep(5)

        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Should be no registretion")

    def test_abs2(self):
        browser = webdriver.Chrome()
        link = "   http://suninjuly.github.io/registration2.html"
        browser.get(link)
        input1 = browser.find_element(By.CLASS_NAME, 'form-control.first')
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your last name']")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.CLASS_NAME, 'form-control.third')
        input3.send_keys("Smolensk")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        time.sleep(5)

        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Should be no registretion")



if __name__ == "__main__":
    unittest.main()