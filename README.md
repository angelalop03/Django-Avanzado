# Django Avanzado (Refugio de animales)
## Introducción 
En este proyecto se ha desarrollado una API Rest utilizando Django y Django REST Framework para la gestión de un refugio de animales. La aplicación permite administrar animales, adoptantes y solicitudes de adopción, aplicando un sistema de autenticación y permisos para controlar a las distintas funcionalidades.

El sistema utiliza MySQL como base de datos y hace uso de vistas genéricas, ViewSets y una vista personalizada que enlaza varios modelos, cumpliendo así los requisitos establecidos.

## Lógica del sistema
El proyecto se basa en la gestión de un *refugio de animales*, donde existen tres entidades principales :
- Animales
- Adoptantes
- Solicitudes de adopcion

### Animales
Los animales representran a los animales disponibles del refugio.
Cada animal contiene información básica como su nombre, edad, estado de vacunación y estado de adopción.

Un animal puede encontrarse en diferentes estados:

- available: el animal está disponible para ser adoptado
- reserved: el animal tiene una solicitud fr adopción pendiente 

Un mismo animal puede tener varias solicitudes de adopción, pero solo peude estar disponible mientras su estado sea available

### Adoptantes
Los adoptantes representan a las personas interesadas en adoptar un animal.
Un adoptante puede realizar una o varias solicitudes de adopción, siempre asociadas a animales existentes en el sistema.

### Solicitudes de adopción 
Las solicitudes de adopción representan la relación entre un animal y un adoptante.l
Cada solicitud enlaza directamente ambos modelos y permite registrar el interes de un adoptante por un animal concreto.

Cuando se crea una solicitud de adopción:
- Se genera una nueva entrada en el modelo de solicitudes.
- El estado del animal cambia automáticamente de available a reserved

### Usuarios, permisos y roles
El sistema incluye un control de acceso basado en ususarios y grupos:
#### Staff del refugio (staff_refugio)
Este grupo representa al personal del refugio y tiene permisos completos para:
- Crear, modificar y eliminar animales
- Gestionar adoptantes.
- Gestionar solicitudes de adopción

Captura 

#### Visitantes (visitantes)
Este grupo representa a usuarios externos o visitantes del sistema.
- Pueden consultar la información disponible (lectura)
No tienen permisos para crear , modificar o eliminar datos

Captura

## Tecnologías utilizadas
- Python
- Django
- Django Rest Framework
- MySQL
- DBeaver
- Postman
- Github

## Creación y configuración inicial
### Creación del entorno virtual e instalación de dependencias
```cmd
python -m venv .venv
.venv\Scripts\activate
pip install django djangorestframework mysqlclient
```
### Creación del proyecto y aplicaciones
Una vez configurado el entorno, se creó el proyecto principal y las aplicaciones necesarias para la gestión del sistema.

```cmd
django-admin startproject api_server .
python manage.py startapp animals
python manage.py startapp adopters
python manage.py startapp adoptions
```

Posteriormente las aplicaciones fueron registradas en el archivo settings.py para que Django pudiera reconocerlas.

### Configuración de la abse de datos MySQL
Para la persistencia de los datos se utilizó MySQL como sistema gestor de bases de datos. La base de datos fue creada manualmente mediante la herramienta Dbeaver, junto con un ususario específico para el proyecto

```sql
CREATE DATABASE refugio_db;
CREATE USER 'django_user'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON refugio_db.* TO 'django_user'@'localhost';
FLUSH PRIVILEGES;
```

La conexión con MySQL se configuró en el archivo settings.py del proyecto:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'refugio_db',
        'USER': 'django_user',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### Migraciones y creación del administrador
Tras la configuración de la abse de datos, se ejecutaron las migraciones para crear las tablas correspondientes a los modelos definidos en el proyecto y se creó un usuario administrador para acceder al panel de administración de Django.

```cmd
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```
## Vistas genéricas y pruebas de funcionamiento
Para la implementación de la API se utilizaron vistas genéricas de Django REST Framework, aplicadas a los modelos Animal y AdoptionRequest. Estas vistas permiten gestionar de forma clara y estructurada las operaciones CRUD del sistema.
cada operación fue probada mediante la herramienta Postman, comprobando el correcto funcionamiento.

### Operaciones implementadas mediante vistas genéricas
Las vistas genéricas utilizadas en el proyecto fueron las siguientes:
- ListAPIView: Listar todos los registros
- CreateAPIView: crear nuevos registros
- RetrieveAPIView: obtener el detalle de un registro concreto
- UpdateAPIView: actualizar un registro existente.
- DestroyAPIView: eliminar un registro
Estas vistas se implementaron para los modelos Animal y AdoptionRequest

### Pruebas de listado (GET)
Se comprobó el correcto funcionamiento de las vistas de listado accediendo a los endpoints correspondientes sin necesidad de autenticación. Estas peticiones permiten consultar la información disponible en el sistema.

Captura de Postman – GET /animals/
![alt text](images/getAnimal.png)

Captura de Postman – GET /adoptions/
![alt text](images/getAdoptionRequest.png)


Resultado esperado:
- Respuesta con código 200 OK
- Devolución de un listado en formato JSON

### Pruebas de creación (POST)
Las operaciones de creación se probaron utilizando autenticación por token, verificando que solo los ususarios con permisos adecuados pueden crear nuevos registros.


Captura de Postman – POST /animals/create/ con token válido
Captura de Postman – POST /adoptions/create/ con token válido

Resultado esperado:
- Respuesta con código 201 Created
- Registro creado correctamente en la base de datos

### Pruebas consulta individual (GET por id)
Se comprobó la obtención del detalle de un registro concreto utilizando su identificador

Captura de Postman – GET /animals/{id}/
![alt text](image.png)

Resultado esperado:
- Respuesta con código 200 OK
- Información detallada del animal solicitado

### Pruebas de actualización (PUT/PATCH)
Las vistas de actualización permiten modificar los datos de un registro existente, siempre que el usuario esté autenticado y tenga los permisos necesarios.

Captura de Postman – PUT /animals/{id}/update/ con token

Resultado esperado:
- Respuesta con código 200 OK
- Datos actualizados correctamente

### Pruebas de eliminación (DELETE)
Se realizaron pruebas para comprobar que la eliminación de registros está restringida a ususarios con permisos adecuados.

Captura de Postman – DELETE /animals/{id}/delete/ con usuario autorizado
 Captura de Postman – DELETE /animals/{id}/delete/ con usuario sin permisos (403 Forbidden)

Resultado esperado:
- Usuario autorizado: eliminación correcta
- Usuario sin permisos: respuesta 403 Forbidden

## ViewSet 
Para la gestión del modelo Adopter se utilizó un ViewSet. El uso del mismo permite centralizar en una única clase todas las operaciones CRUD.

Las operaciones disponibles a través del ViewSet incluyen:
- Listado de adoptantes 
- Creación de nuevos adoptantes
- Consulta del detalle de un adoptante.
- Actualización de la información de un adoptante.
- Eliminación de adoptantes

### Pruebas del viewSet
El correcto funcionamiento del ViewSet se verificó mediante pruebas realizadas con la herramienta Postman, accediendo a los endpoints generados automáticamente.

Captura de Postman – GET /adopters/
Captura de Postman – POST /adopters/ con token válido

Resultados esperados:

En la petición GET se obtiene un listado de adoptantes en formato JSON.

En la petición POST se crea correctamente un nuevo adoptante cuando el usuario dispone de los permisos necesarios.

## Api_View
Además de las vistas genéricas y el ViewSet, se implementó una vista personalizada utilizando el decorador @api_view. Esta vista se creó para cumplir el requisito de disponer de una funcionalidad propia que enlace varios modelos y aplique una lógica de negocio específica.

En este proyecto , la vista personalizada gestiona el proceso de solicitud de adopción de un animal. Para ello, enlaza los siguientes modelos:

- Animal 
- Adopter 
- AdoptionRequest

### Lógica implementada
Cuando un adoptante solicita adoptar un animal, el sistema realiza los siguientes pasos:
1. Comprueba que el animal existe y que su estado es available.
2. Comprueba que el adoptante existe.
3. Crea una nueva entrada en AdoptionRequest enlazando el animal con el adoptante.
4. Actualiza el estado del animal automáticamente a reserved, evitando que otro adoptantes puedan solicitar el mismo animal como disponible.

### Endpoint
La vista se expone mediante el endopint:
- POST /adoptions/animal/<animal_id>/request/
El cuerpo de la petición incluye el identificador del adoptante:
```json
{
  "adopter_id": 1
}
```

### Pruebas realizadas
El correcto funcionamiento de esta vista se verificó mediante pruebas en Postman:

Captura de Postman – POST /adoptions/animal/{id}/request/ creando una solicitud de adopción
Captura de Postman – GET /animals/{id}/ mostrando el estado del animal actualizado a reserved

Resultados esperados:
- Respuesta con código 201 Created cuando la solicitud se crea correctamente.
- El animal cambia de estado de available a reserved.
- En caso de que el animal no exista o no esté disponible, se devuelve un error controlado (404 o 400 según corresponda).

