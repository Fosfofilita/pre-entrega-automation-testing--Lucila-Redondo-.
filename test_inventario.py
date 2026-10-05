import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By 

def test_inventario():
    driver= webdriver.Firefox()
    
    try:
        driver.get("https://www.saucedemo.com/")
        
        usuario = driver.find_element(By.ID, "user-name")
        password = driver.find_element(By.ID, "password")
        boton = driver.find_element(By.ID,"login-button")


        usuario.send_keys("standard_user")
        password.send_keys("secret_sauce")
        boton.click()
    
        assert driver.title == "Swag Labs"

    # reviso que haya productos visibles  
        productos = driver.find_elements(By.CLASS_NAME, "inventory_item")
        assert len(productos) > 0

    # compruebo el nombre y precio del primer producto 
        primer_producto = productos[0]
        nombre_producto = primer_producto.find_element(By.CLASS_NAME,"inventory_item_name").text
        precio_producto = primer_producto.find_element(By.CLASS_NAME, "inventory_item_price").text

        assert nombre_producto == "Sauce Labs Backpack"
        assert precio_producto == "$29.99"
        
    # reviso menu hamburgesa 
        menu = driver.find_element (By.ID,"react-burger-menu-btn")
        assert menu.is_displayed()

    #verifico filtro 
        filtro = driver.find_element(By.CLASS_NAME, "product_sort_container")
        assert filtro.is_displayed() 

    finally: 
        driver.quit()