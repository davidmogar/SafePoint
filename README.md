# SafePoint

## API

A continuación se muestra una pequeña descripción de los *endpoints* existentes en la API.
La url base de la API es [miw.danimeana.es/safepoint](http://miw.danimeana.es/safepoint).

HTTP Method | Ruta | Descripción
:----------:|------|-------------
GET | /categories | Listado de todas categorias de incidencias.
GET | /categories/**<id>**/reports | Listado con todas las incidencias de la categoría cuyo identificador es **<id>**.
GET | /reports | Listado con todas las incidencias de todas las categorias.
POST | /reports | Crea una incidencia nueva. Los parametros necesarios son: **lat**, **lng**, **description** y **category_id**. Además es necesario estár logeado en el sistema.
GET | /reports/**<id>** | Detalles de la incidencia cuyo identificador es **<id>**.
DELETE | /reports/**<id>** | Elimina la incidencia cuyo identificador es **<id>**.

##  INSTALACIÓN

La aplicación ha sido testeada baja Python3. A continuación se detallan los pasos para su instalación en Ubuntu y Mac OS X y ejecución.

Instalar las herramientas de Python3:

* Ubuntu:
```bash
sudo apt-get update
sudo apt-get -y install python3 python3-pip libffi-dev
sudo pip3 install virtualenv
```
*Nota: Es necesario instalar libffi-dev (usado en el sdk de PayPal)*

* Mac OS X (requiere [brew](http://brew.sh)):
```bash
sudo brew update
brew install python3
sudo pip3 install virtualenv
```

Clonar el repositorio y acceder a él:

```bash
git clone https://github.com/davidmogar/SafePoint
cd SafePoint
```

Crear el entorno virtual:

```bash
virtualenv venv
```

Activamos el entorno virtual:

```bash
. venv/bin/activate
```

Instalar las dependencias:

```bash
pip3 install -r requirements
```

Desactivamos el entorno virtual:

```bash
deactivate
```

## Ejecución

A continuación se detallan los pasos a seguir para ejecutar el servidor web.

Activamos el entorno virtual:

```bash
. venv/bin/activate
```

Ejecutar el servidor:
```bash
python3 run.py
```

La activación del entorno virtual será necesaria cada vez que se quiera ejecutar el servidor. Para desactivar el entorno virtual puede utilizarse el comando:

```bash
deactivate
```
