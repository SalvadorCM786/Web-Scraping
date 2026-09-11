import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://en.wikipedia.org/wiki/List_of_best-selling_video_games"
headers = {"User-Agent": "Mozilla/5.0 (compatible; CursoScraping/1.0)"}
response = requests.get(url, headers=headers)
response.encoding = 'utf-8'

soup = BeautifulSoup(response.text, "html.parser")
tabla = soup.find("table", class_="wikitable")
filas = tabla.find_all("tr")[1:]

datos = []
for fila in filas:
    celdas = fila.find_all(["td", "th"])[-8:]

    datos.append({
        "titulo": celdas[0].get_text(strip=True),
        "ventas_millones": celdas[1].get_text(strip=True),
        "serie": celdas[2].get_text(strip=True),
        "plataformas": celdas[3].get_text(strip=True),
        "anio_lanzamiento": celdas[4].get_text(strip=True),
        "desarrollador": celdas[5].get_text(strip=True),
        "editor": celdas[6].get_text(strip=True)
    })

df = pd.DataFrame(datos)
df.to_csv("videojuegos_mas_vendidos.csv", index=False)
print("Archivo videojuegos_mas_vendidos.csv creado.")
