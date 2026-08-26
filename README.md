# Proyecto Urban Grocers 

## Descripción

En este proyecto se hizo la automatización de la función para crear kits asociadas a un usuario, específicamente, generando un token de autorización a la hora de crear un usuario para así poder hacer la creación del kit y así pueda quedar ligada especificamente al usuario correspondiente de ese token. En esta automatización hacemos 5 pruebas positivas y 4 pruebas negativas para el campo "name" en la creación de kits, para corroborar que funcione correctamente y acepte los caracteres de los requisitos los cuales son, aceptar alfabeto latino, aceptar numeros en formato de texto, aceptar espacios y aceptar caracteres especiales. Mientras que en las pruebas negativas en el mismo campo "name" se realizan para verificar que la creación de un kit ligada a una cuenta no proceda cuando los caracteres introducidos no cumplan la especificación de los requisitos.

## Tecnologías utilizadas
Pycharm para poder realizar el código en lenguaje Python.

Pytest para poder realizar la automatización de las pruebas. El medio de instalación fue mediante la terminal utilizando el comando: pip install pytest

Requests para lograr una comunicación efectiva al servidor mediante API REST . El medio de instalación fue mediante la terminal utilizando el comando : pip install requests

Git para la publicación del proyecto en GitHub

## Documentacion 

configuration.py: URL base y endpoints.

data.py: cuerpos de solicitud y datos necesarios para las pruebas.

sender_stand_request.py: funciones encargadas de enviar las solicitudes.

create_kit_name_kit_test.py: funciones auxiliares, assertions y escenarios automatizados.

.gitignore: exclusión de archivos locales que no deben formar parte del repositorio.

## Funciones principales

post_new_user(body): esta es la función encargada de hacer una petición Post al servidor para poder crear un usuario. 

get_new_user_token(body) : con esta función podemos obtener el token creado a la hora de crear un usuario para poder utilizar la autorización y crear el kit enlazado al usuario con otra función.

post_new_kits(kit_body: auth_token) : función que nos crea un kit, creando una copia del header para poder modificar el campo token con el token generado, utilizarlo como autorización y así crear el kit  ligado al usuario.

get_kit_body(kit_name): esta función es la que nos va a permitir  generar una copia del body en el kit para poder cambiar el campo "name" a los valores correspondientes de cada prueba.

positive_assert(kit_name): nuestra función para la automatización de pruebas positivas, nos permite mandar como argumento el valor que queremos tener en el campo "name" para poder realizar las pruebas, que buscaran como resultado un status code 201 y comparar que el cuerpo del kit coincida con el cuerpo de la solicitud. En caso de que el status code no devuelva un 201 o el cuerpo de la solicitud no coincida, la prueba lanzará una prueba fallida detectando asi un bug en Urban Grocers.

negative_assert(kit_name): esta es la función que permite automatizar las pruebas en las que esperamos que de vuelva un status code 400, es decir que la solicitud no pueda completarse a la hora de hacer la creación del kit, nos permite mandar como argumento el valor que queremos tener en el campo "name" y así poder realizar las pruebas. Este código busca que el status code devuelva un 400, la solicitud no pueda procesarse y mande un mensaje al usuario indicando que ha introducido un formato incorrecto en el campo "name". En caso contrario de que el status code no devuelva un 400, la prueba fallará detectando un bug en Urban Grocers.


## Pruebas realizadas

Se realizaron las 9 pruebas de la lista de comprobación otorgada para el campo "name" en la creación de kits ligadas a un usuario. Las pruebas se pueden ejecutar en la terminal con el comando : pytest create_kit_name_kit_test.py -v

Prueba 1 (positiva) = Passed 201 

Prueba 2 (positiva) = Passed 201

Prueba 3 (positiva) = Passed 201

Prueba 4 (positiva) = Passed 201

Prueba 5 (positiva) = Passed 201

Prueba 6 (negativa) = Failed 201 != 400 , la prueba debió generar un código de error 400 y mandar un mensaje al usuario de que el campo "name" es incorrecto, sin embargo la prueba falló, ya que la solicitud creó el kit a pesar de tener un formato no permitido en el campo "name". Por lo que esta prueba detectó un bug

Prueba 7 (negativa) = Failed 201 != 400 , la prueba debió generar un código de error 400 y mandar un mensaje al usuario de que el campo "name" es incorrecto, sin embargo la prueba falló, ya que la solicitud creó el kit a pesar el tener un formato no permitido en el campo "name". Por lo que esta prueba detectó un bug

Prueba 8 (negativa) = Failed 201 != 400 , la prueba debió generar un código de error 400 y mandar un mensaje al usuario de que el campo "name" es incorrecto, sin embargo la prueba falló, ya que la solicitud creó el kit a pesar no contener el campo name. Por lo que esta prueba detectó un bug

Prueba 9 (negativa) = Failed 201 != 400 , la prueba debió generar un código de error 400 y mandar un mensaje al usuario de que el campo "name" es incorrecto, sin embargo la prueba falló, ya que la solicitud creó el kit a pesar el tener un formato no permitido en el campo "name". Por lo que esta prueba detectó un bug

## Las pruebas fallidas representan bugs en el servidor de Urban Grocers ya que no hay errores de código.

Autor del proyecto : Carlos Román Irecta Durán 