import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By 

def test_inventario():
    driver= webdriver.Firefox()
    
    try:
        driver.get("https://www.saucedemo.com/")
        
        usuario = driver.find_element(By.ID, "user-name")
        password = driver.find_element(By.ID, "password")
        boton_login = driver.find_element(By.ID,"login-button")


        usuario.send_keys("standard_user")
        password.send_keys("secret_sauce")
        boton_login.click()

        boton_onesie = driver.find_element(By.ID,"add-to-cart-sauce-labs-onesie")
        boton_onesie.click()

        boton_luz = driver.find_element(By.ID,"add-to-cart-sauce-labs-bike-light")
        boton_luz.click()

        carrito = driver.find_element(By.CLASS_NAME,"shopping_cart_link")
        carrito.click()

        assert "/cart.html" in driver.current_url
        items_carrito = driver.find_elements(By.CLASS_NAME, "cart_item")

        assert len(items_carrito) == 2
        
        nombres_esperados = ["Sauce Labs Onesie", "Sauce Labs Bike Light"]
        precios_esperados = ["$7.99", "$9.99"]
        
        for i in range(len(items_carrito)):
            item = items_carrito[i] 
            
            nombre_actual = item.find_element(By.CLASS_NAME, "inventory_item_name").text
            precio_actual = item.find_element(By.CLASS_NAME, "inventory_item_price").text
            
            assert nombre_actual == nombres_esperados[i]
            assert precio_actual == precios_esperados[i]

    finally: 
        driver.quit()

       