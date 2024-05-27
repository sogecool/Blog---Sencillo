import requests
from bs4 import BeautifulSoup
import csv

# URL de la página web
url = 'http://localhost/BlogPW/index.html'

# Enviar una solicitud GET
response = requests.get(url)

# Verificar que la solicitud fue exitosa
if response.status_code == 200:
    page_content = response.content

    # Crear un objeto BeautifulSoup
    soup = BeautifulSoup(page_content, 'html.parser')
    
    # Extraer todos los títulos de artículos (suponiendo que están en <h2> tags)
    titulos = soup.find_all('h2', class_='titulo-articulo')

    # Imprimir los títulos extraídos para depuración
    if titulos:
        print("Títulos extraídos:")
        for titulo in titulos:
            print(titulo.get_text())
    else:
        print("No se encontraron títulos con la clase 'titulo-articulo'.")

    # Abrir un archivo CSV para escribir
    with open('titulos_articulos.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Titulo'])
        
        # Escribir cada título en una nueva fila
        for titulo in titulos:
            writer.writerow([titulo.get_text()])
else:
    print('Error al acceder a la página')
