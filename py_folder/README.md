Descripción de esta carpeta
--------------------
Mas adelante es posible que trabajen en proyectos mas grandes y quizás que tengan que usar arhivos .py y no notebooks.

Tal como se lo dijeron en el teórico, al tener la funcion main pueden correr desde la terminal python main.py y 
va a ejecutar lo definido en la funcion main.

Para correr el archivo main.py, en una terminal:

    (.venv) $ python main.py

Para generar la documentación con pdoc (https://pdoc.dev/) deben describir sus funciones en docstrings.
 
    1) Instalarlo:
       (.venv) $ pip install pdoc
    2) Crear la carpeta con la documentación
       (.venv) $ pdoc main.py utils/ -o ./documentacion/Docs -t ./documentacion/pdoc_templates/
