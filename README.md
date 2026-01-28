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
#### Visitantes (visitantes)
Este grupo representa a usuarios externos o visitantes del sistema.
- Pueden consultar la información disponible (lectura)
No tienen permisos para crear , modificar o eliminar datos

## Tecnologías utilizadas
- Python
- Django
- Django Rest Framework
- MySQL
- DBeaver
- Postman
- Github

## Creación y configuración inicial