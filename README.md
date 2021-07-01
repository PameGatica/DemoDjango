# DemoDjango
<<<<<<< HEAD
Proyecto Demo Django Framework de apoyo a la Experiencia N°3 de la Asignatura Programación Web 

## Parte 1:  Configuración del entorno
1. Verificar que Python 3 esté instalado en el equipo

```console
c:\> python --version
```
> Si python no está instalado, instalar según instrucciones de clase 
[Descargar instalador desde sitio oficial de Python](http://www.python.org)


1. Verificar que PIP esté instalado en el equipo
```console
c:\> py -m pip --version
```
>Si PIP está desactualizado, actualizar.

```console
c:\> py -m pip install --upgrade pip
```

3. Instalar Django
```console
c:\> pip install django
```
>Puedes verificar la instalación con:
```console
c:\> py -m django --version
```

## Parte 2:  Crear proyecto Django
>Debes crear un directorio donde almacenarás el proyecto. Si trabajarás enlazado a un repo, éste es un buen momento para clonarlo.
En esta demo, se asumirá que los proyectos se almacenarán en<code> __C:/ProyectosDjango__ </code>

_Para crear el directorio y acceder a él desde el cmd_
```console
c:\>Users\yo> cd\
c:\>md ProyectosDjango
c:\>cd ProyectosDjango 

c:\ProyectosDjango>
```
_Para acceder al directorio desde el cmd_
```console
c:\>cd c:\ProyectosDjango
c:\ProyectosDjango>
```

### Creando proyecto django
```console
c:\ProyectosDjango>django-admin startproject nombre_proyecto
```

## Parte 3:  Enlazar proyecto django a Visual Studio Code
>Abrir directorio del proyecto django creado en el paso anterior con Visual Studio Code. Ésta será la raiz de nuestro proyecto.

## Parte 4:  Crear Aplicación
>Éste será nuestro sitio web. Desde el terminal de VSCODE, escribir:
```console
c:\ProyectosDjango\Proyecto>py manage.py startapp nombre_aplicacion
```

## Parte 5:  Agregar aplicación al proyecto
>En el archivo <code>settings.py </code> agregar el nombre de la aplicación a __INSTALLED_APPS__

```python
    INSTALLED_APPS = [
    #LIBRERIAS DJANGO
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #MI APP
    'nombre_app',
]
```

## Parte 6:  Iniciar servidor 
>En la terminal de VS CODE iniciar el servidor de pruebas. __No olvidar que el servidor debe mantenerse corriendo durante todo el uso de la aplicación__.

```console
c:\ProyectosDjango\Proyecto>py manage.py runserver
```
Puedes ver los resultados en <code>http://127.0.0.1:8000/</code>


# Conectar a BD Oracle
>1. Instalar paquete Oracle para Django mediante pip

```console
>pip install cx_oracle
```

>2. En Oracle local crear un nuevo usuario y conectar con SQL Developer para checkear posteriormente

>3. Editar <code>settings.py</code> para apuntar el proyecto a Oracle

```python
    # Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.oracle',
        'NAME': '127.0.0.1:1521/xe',
        'USER': 'django_user', #nombre del usuario oracle
        'PASSWORD':'django', #contraseña del usuario oracle
        'TEST':{
            'USER':'default_test',
            'TBLSPACE':'default_test_tbls',
            'TBLSPACE_TMP':'default_test_tbls_tmp'
        }
    }
}
]
```

>4. Crear los modelos en <code> core/models.py </code> En el ejemplo de la clase, usamos los modelos Vehículo y Categoría
```python
from django.db import models

#Clase Categoria

class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True,verbose_name='Id Categoría')
    nombreCategoria = models.CharField(max_length=50, verbose_name="Nombre Categoría")

    def __str__(self):
        return self.nombreCategoria

#Clase Vehículo

class Vehiculo(models.Model):
    patente = models.CharField(primary_key=True,max_length=6, verbose_name='Patente')
    marca = models.CharField(max_length=25, verbose_name="Marca Vehículo")
    modelo = models.CharField(max_length=20, null=True, blank=True, verbose_name="Modelo")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.patente
```

>5. Propagar los cambios en el modelo a la base de datos.

Crear nuevas migraciones basadas en los cambios que ha realizado en los modelos.
```console
c:\ProyectosDjango\Proyecto>py manage.py makemigrations 
```
Aplicar  las migraciones en la Base de Datos
```console
c:\ProyectosDjango\Proyecto>py manage.py migrate 
```

> En este punto, puedes verificar con SQL Developer que las tablas Categoría y Vehículo se hayan creado exitosamente.


# Habilitar panel de administración
>Una de las ventajas de trabajar con Django es que este framework permite crear de forma automática un panel de administración, tanto para las tablas como para los usuarios creados en el servidor de base de datos.

>1. Lo primero que debemos hacer es crear un súper usuario para el panel de administración.

```console
c:\ProyectosDjango\Proyecto>py manage.py createsuperuser 
```
=======
Proyecto Ayuda a un Peludo en Django
>>>>>>> main
