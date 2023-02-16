# Django Rest Framework Tutorial
Django REST Framework es un marco de software libre y de código abierto que se utiliza para crear **API RESTful** para aplicaciones web modernas. Al utilizar este marco, los desarrolladores pueden crear API rapidamente por medio de recursos existentes y estructuras predefinidas. Estas API se pueden utilizar para comunicar aplicaciones web con el servidor, para llevar a cabo interacciones en tiempo real, como el chat de un sitio web, y para sincronizar los datos entre las diferentes plataformas de aplicaciones móviles.
## Instalación
Para iniciar a trabajar con django rest framework, seguiermos los siguientes pasos:
* Crear una carpeta (No importa la ruta) donde alojes tus projecto dentro del directorio creaemos un directorio con el nombre de nuestro proyecto y navegamos hacía el
* CReamos nuestro ambiente virtual ejecutando el siguiente comando 
```
    python3 m venv <name-enviroment>
``` 
* Activamos el ambiente virtual. Si estás en linux el comando sería:
```
    source <name-enviroment>/bin/activate
```
Si trabajas desde windows tienes dos opciones:
```
    # Desde el CMD
    cd <name-enviroment>\scripts\activate

    # Desde Powershell
    .\<name-enviroment>\scripts\activate
```

* Una vez tengamos creado y activado el entorno virtual, procedemos a instalar el paquete de django rest framework. Para ello ejecutamos:
```
    pip install djangorestframework
```
Por defecto se instalan otros paquetes que son requeridos para restframework pueda ejecutarse entre ellos el paquete de django. Si ejecutas el comando  `pip freeze` Tendrías un resultado como éste: 
```
asgiref==3.6.0
Django==4.1.6
djangorestframework==3.14.0
pytz==2022.7.1
sqlparse==0.4.3
```

## Creación del proyecto


## Viewsets
Una ViewSetclase es simplemente un tipo de Vista basada en clases, que no proporciona ningún controlador de métodos como .get()o .post(), sino que proporciona acciones como .list()y .create(). Un viewset a diferencia de las clases genéricas, proporciona otros métodos (Acciones) para realizar sus tareas. Algunos métodos son: list(), create()