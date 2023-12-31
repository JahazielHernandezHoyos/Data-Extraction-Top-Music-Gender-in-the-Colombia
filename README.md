# 🎶 Data-Extraction-Top-Music-Gender-in-the-Colombia 🎵
Este código es un script de Python que utiliza la API de Spotify para obtener los géneros de música disponibles en la plataforma y exportar los datos de las canciones más populares de cada género en Colombia a archivos CSV. 🚀

## 📝 Descripción

El script comienza importando las bibliotecas necesarias, incluyendo la biblioteca spotipy, que es una biblioteca Python para la API de Spotify. Luego, se definen las credenciales del cliente de Spotify, que se utilizan para autenticar la conexión con la API. 🔑

La función obtener_generos() utiliza la API de Spotify para obtener una lista de todos los géneros posibles en la plataforma. La función exportar_datos() utiliza la función obtener_generos() para iterar sobre cada género y buscar las canciones más populares de ese género en Colombia. Luego, los datos de cada canción se escriben en un archivo CSV con el nombre del género correspondiente. 📊

Finalmente, el script verifica si se está ejecutando como el programa principal y, si es así, llama a la función exportar_datos() para comenzar el proceso de exportación de datos. 🎉

## 📦 Dependencias

- spotipy
- pandas

## 🚀 Cómo ejecutar el Script

Para utilizar este script simplemente ejecuta python app.py, se deben proporcionar las credenciales del cliente de Spotify y ejecutar el archivo en un entorno de Python. Los archivos CSV resultantes se guardarán en el mismo directorio que el archivo del script. De igual forma dejo mis credenciales sin problemas con que se le haga un uso 📂
