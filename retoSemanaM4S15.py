import requests

# Tu API Key de OpenWeather  
api_key = "********769e4f68b7c1e502bb8e43c"

# Coordenadas de tu localidad (latitud y longitud)
lat = "**.**63422"
lon = "****.**70988888889"

# URL para la petición
url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"

# Hacemos la petición GET
response = requests.get(url)
data = response.json()

# Verifica si la respuesta tiene "main" y "weather"
if "main" in data and "weather" in data:
    temp = data["main"]["temp"]
    description = data["weather"][0]["description"]
    print(f"Clima actual: {temp}°C, {description}")
else:
    print("Error en la respuesta:", data)
