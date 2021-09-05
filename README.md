# Rutismo

Es un software educativo para niños con autismo, permite crear rutinas mediante imágenes las cuales ayudan al niño con las tareas diarias 

## Instalacion

Instalar [python3](https://www.python.org/) desde su web oficial

una vez instalado python abrimos la terminal y usando el manejador de paquequetes de python instalamos virtualenv

```bash
pip install virtualenv
```
creamos un nuevo entorno virtual
```bash
virtualenv env
```
accedemos a la carpeta env 

```bash
cd env/script
```
activamos entorno virtual

```bash
activate
cd ..
```

luego clnamos el repositorio

```bash
gh repo clone emanueld92/rutismo
```


navegamos con en comando CD a la carpeta rutismo
y instalamos los requeriientos con el comando

```bash
pip install -r requirements.txt
```
una vez instalados todos nuestro requerimientos, creamos nuestra base datos MySql con el nombre rutismo

modificamos el archivo ejemplo.env con nuestras crendenciales de mysql

### migrando modelos

```bash
python3 manage.py makemigrations
python3 manage.py migrate
```
#### Creando usuario admin

```bash
python3 manage.py createsuperuser
```

## Poner en marcha servidor de django en el puerto 8000 

```
python3 manage.py runserver

```

## Contribuciones:

## License
[MIT](https://choosealicense.com/licenses/mit/)
