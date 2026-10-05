import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By 

def test_login_exitoso():
    driver= webdriver.Firefox()
    
    try:
        driver.get("https://www.saucedemo.com/")

        usuario = driver.find_element(By.ID, "user-name")
        password = driver.find_element(By.ID, "password")
        boton = driver.find_element(By.ID,"login-button")


        usuario.send_keys("standard_user")
        password.send_keys("secret_sauce")
        boton.click()

        assert "/inventory.html" in driver.current_url

        logo = driver.find_element(By.CLASS_NAME, "app_logo")
        assert logo.text == "Swag Labs" #valido que aparezca texto swag labs    

    finally:
            driver.quit()


#verificar nombre de éstaña = dirver.title
#verifficar la existencia de un producto  / cantidad de productos 
#

