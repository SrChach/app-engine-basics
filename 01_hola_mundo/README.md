# Hola mundo con Google Cloud

## Requerimientos

- Una cuenta en google Cloud
- Tener el SDK de google `"gcloud"` instalado

## Instrucciones

### Local

- Crear un archivo `app.yaml` para decirle a Google App Engine como tratar nuestra App
- Declarar en `app.yaml/handlers` cómo manejar las peticiones a nuestro servicio. Redireccionar a un módulo/funcion (`main.py/app`, en este caso)
- Testear como sería el deploy con `dev_appserver.py app.yaml`

### Deploy

- Autenticarnos a google cloud desde el SDK con `gcloud auth login`
- Setear el proyecto actual con `gcloud config set project <PROJECT-ID>`
- Hacer el deploy con `gcloud app deploy -v 1`. Seguir la configuracion. *NOTA: '-v' es para la versión*
- Checar que el deploy se haya realizado correctamente con `gcloud app browse`

### Versiones

- Hacemos un cambio a nuestra app
- Hacemos un segundo deploy, con otra version: `gcloud app deploy -v 1.0.1`
- Vamos a la consola de Google, en nuestro proyecto seleccionamos "versiones"
- Seleccionamos nuestras versiones y luego "dividir tráfico"

