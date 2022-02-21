import requests
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
from pprint import pprint

# Digite sua chave de API
api_key = "b77e07f479efe92156376a8b07640ced"

# Entra com nome da cidade do usuário
city_name = input("Entre com o nome da cidade: ")

# API url - ex:http://api.openweathermap.org/data/2.5/weather?q=campinas&appid=b77e07f479efe92156376a8b07640ced
weather_url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city_name + '&appid=' + api_key

# Obtenha a resposta do URL do tempo
response = requests.get(weather_url)

# resposta estará no formato json e precisamos alterá-la para o formato pythonic
weather_data = response.json()

# Certifique-se de obter 200 como resposta para prosseguir
# DADOS DE AMOSTRA: {"coord":{"lon":-47.0608,"lat":-22.9056},
# ""weather":[{"id":500,"main":"Chuva","description":"chuva fraca", "icon":"10d"}],
# "base":"estações","main":{"temp":294.4,"feels_like":294.96,"temp_min":290.98,"temp_max":298.77,
# "pressure" :1016,"umidade":91},"visibilidade":10000,"vento":{"velocidade":2.06,
# "graus":20},"chuva":{"1h":0.42},"nuvens": {"all":100},"dt":1643828737,"sys":{"type":1,"id":8393,
# "country":"BR","sunrise":1643791729,"sunset":1643838900 },"fuso horário":-10800,"id":3467865,
# "nome":"Campinas","cod":200} == '404' significa cidade não encontrada

if weather_data['cod'] == 200:
    kelvin = 273.15  # Temperatura mostrada aqui está em Kelvin
    temp = int(weather_data['main']['temp'] - kelvin)

    # print(f"Informações da cidade: {city_name}")
    print(f"Temperatura (Celsius): {temp}°")

    temperatura = int(temp)

    pl_pop = temperatura > 30
    pl_rock = temperatura >= 15 & temperatura <= 30
    pl_classica = temperatura < 14


    # funçaõ que define sua playlist conforme temperatura citadas acima
    def pl (plt):
        if pl_pop:
            return "spotify:playlist:2APVTN27nKIFNMrJ8GXo8U"
            #Playlist POP
        else:
            if pl_rock:
                return 'spotify:playlist:6jmDxyne7FJ3fVA9CkGYpd'
                #"Playlist ROCK

            elif pl_classica:
                return 'spotify:playlist:1h0CEZCm6IbFTbxThn6Xcs'
                #Playlist CLASSICA


else:
    print(f"City Name: {city_name} não foi encontrado!")

# credenciais para acesso spotify
sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id="Cliente ID",
                                                                         client_secret="Secret KEY"))

pl_id = (pl(temperatura))

offset = 0
# funçao para buscar nome da musica conforme temperatura
while True:
    response = sp.playlist_items(pl_id,
                                 offset=offset,
                                 fields='items.track.name',
                                 additional_types=['track'])

    if len(response['items']) == 0:
        break

    offset = offset + len(response['items'])
    for name in response['items']:
        track = name['track']
        print(track)





