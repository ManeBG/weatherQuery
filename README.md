# Consulta de Clima 

Este proyecto, parte del curso "Fundamentos de Python", muestra cómo usar APIs para obtener datos externos. En este caso, consultamos la API de OpenWeather para recibir el clima actual de una ubicación.
Lo que Aprendí 

Peticiones HTTP y APIs: Aprender a conectarse con APIs para obtener datos en tiempo real.
Manejo de JSON: Extraer y trabajar con datos en JSON, el formato estándar de las APIs.



#####################
# Código

import requests

api_key = "TU_API_KEY"
lat = "LATITUD"
lon = "LONGITUD"

url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
response = requests.get(url)
data = response.json()

if "main" in data and "weather" in data:
    temp = data["main"]["temp"]
    description = data["weather"][0]["description"]
    print(f"Clima actual: {temp}°C, {description}")
else:
    print("Error en la respuesta:", data)

    print("Error en la respuesta:", data)
##################################



# Ejecución
Instala requests con pip install requests.
Corre el programa y obtén el clima de cualquier ubicación ingresando las coordenadas deseadas.

Se nesesita crear una cuenta en Openweather pora optener tu API_KEY