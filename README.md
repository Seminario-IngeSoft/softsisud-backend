# SoftSiUD - Backend

Proyecto realizado en Django para el proyecto final de Seminario de ingeniería, se hace uso de los template tag pero se construye con servicios REST con Django REST Framework para posteriormente separar el frontend del backend e incorporar cualquiér otro tipo de framewoks como Angular, React, Svelte o Vue.

Proyecto completamente funcional para la gestión de usuarios, posts, servicios REST entre otros.

### Ejecutar proyecto

```
$ python manage.py makemigrations
```

```
$ python manage.py migrate
```

```
$ python manage.py runserver
```

### Crear usuarios o superususarios

```
$ python manage.py createsuperuser
```
```
$ python manage.py createuser
```



# Lista de rutas

| Sección  |  Ruta |
| ------------ | ------------ |
| API |  /users/api/list_profiles/ |
| Users | login/ |
| Users | logout/ |
| Users | signup/view/ |
| Users | signup/ |
| Users | me/profile/ |
| Users | <str:username>/ |
| Users | Middlewares | me/profile |
| Admin | admin/ |


# Usuaros de prueba

| usuario  |  contraseña |
| ------------ | ------------ |
| admin | admin |

# Información

| Nombre  |  Rol |  Email |
| ------------ | ------------ | ------------ |
|  Arthur David Sanchez Lopez |   | adsanchezl@correo.udistrital.edu.co |
|  Juan Esteban Olaya García |   | jeolayag@correo.udistrital.edu.co |
|  Cristian Camilo Méndez Trujillo |   | ccmendezt@correo.udistrital.edu.co |
|  Sebastián Salinas Rodríguez |   | ssalinasr@correo.udistrital.edu.co |
|  Cristhian Mauricio Yara Pardo |   | cmyarap@correo.udistrital.edu.co |


