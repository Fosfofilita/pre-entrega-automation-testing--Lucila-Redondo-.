Proyecto de automatizacion Sauce Demo

Descripcion
Pruebas de interfaz web simulando interacciones de un usuario. Consta de tres scripts:

test_login.py: Valida el inicio de sesion exitoso.

test_inventario.py: Verifica la carga de productos, precios y visualizacion de menues.

test_carrito.py: Comprueba el agregado de items y la exactitud de los datos en el carrito.

Tecnologias
Python, Selenium WebDriver, Pytest, pytest-html.

Instalacion
Requiere tener instalados Python y el navegador Firefox.
Dependencias
pip install pytest selenium pytest-html

Ejecucion
Comando para correr los tests:
python -m pytest

Resultados
La configuracion de pytest.ini genera automaticamente un archivo visual con los resultados en la ruta: resports/reporte.html
