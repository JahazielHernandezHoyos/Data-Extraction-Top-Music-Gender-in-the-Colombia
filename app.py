import csv
from typing import List

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Credenciales de cliente de Spotify
CLIENT_ID = "f192c0e218c848eab5bce98c315dbd64"
CLIENT_SECRET = "01026e68676f4d398e22df92d4cd2753"

client_credentials_manager = SpotifyClientCredentials(
    client_id=CLIENT_ID, client_secret=CLIENT_SECRET
)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


def obtener_generos() -> List[str]:
    """
    Obtiene todos los géneros posibles de Spotify 🎶.

    Returns:
        List[str]: Una lista de strings con los géneros disponibles en Spotify.
    """
    genres = sp.recommendation_genre_seeds()["genres"]
    return genres


def exportar_datos() -> bool:
    """
    Exporta los datos de las canciones más populares de cada género en Colombia a archivos CSV 📊.

    Returns:
        bool: True si la exportación de datos fue exitosa, False en caso contrario.
    """
    generos = obtener_generos()
    for genero in generos:
        results = sp.search(q=f'top colombia genre:"{genero}"', type="track", limit=50)
        tracks = results["tracks"]["items"]
        if tracks == []:
            print(f"No se encontraron canciones para el género {genero} 🤷‍♂️")
            continue
        with open(f"{genero}.csv", "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Artista", "Canción", "Popularidad"])
            for track in tracks:
                artist = track["artists"][0]["name"]
                name = track["name"]
                popularity = track["popularity"]
                writer.writerow([artist, name, popularity])
        print(f"Se ha guardado el archivo {genero}.csv ✅")
    return True


if __name__ == "__main__":
    exportar_datos()
