### Tarea4_BibliotecaOnline
### Luis Alonso Hernandez Perdomo / 2023-1804

Biblioteca online donde se podran comprar libros. Actualmente solo cuenta con un login y una seccion para gestionar el inventario de libros en la cual se puede registrar, actualizar, eliminar y ver todos los libros y los detalles de estos.

Los libros son almacenados en una base de datos **SQL Server** con la cual la pagina web se comunica mediante un **CRUD**, por lo tanto, es necesario tener **SQL Server** instalado y el **servicio del motor de SQL Server** corriendo. 

Para crear la base de datos se debe ejecutar el archivo de script SQL *BibliotecaOnline_20231804.sql*

### Pruebas automaziadas con Selenium

El codigo fuente de las pruebas de **Selenium** y el **report.html** junto a los screenshots se encuentran en la carpeta **biblioteca_tests**. Estas fueron desarrolladas con Python utilizando los paquetes de *selenium*, *pytest* y *pytest-html*. 

El enlace de la pagina en la cual se realizaran las pruebas se encuentra en *utils\base_test.py*
