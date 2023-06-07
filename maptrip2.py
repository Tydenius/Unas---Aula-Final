import osmnx as ox
import networkx as nx
from geopy.geocoders import Nominatim
import folium

print("Digite nova da Rua(ou Avenida) e número separados por vírgula, como o exemplo abaixo \n Nome da Rua, número \n")
nome = "Seu input aqui"
end_or = "Seu input aqui"
end_dest = "Seu input aqui"
place_check = input("Você esta em São Paulo? responda s/n \n")

if(place_check == "s"):
  place = 'São Paulo, Brazil'
  meu_uber = Nominatim(user_agent = nome)
else:
  place = input("Digite seu Estado" + ", Brazil")

meu_uber = Nominatim(user_agent = nome)

mode = "Seu input aqui: Dica: o Usuário só pode digitar walk,drive ou bike, qualquer outro texto deve ser rejeitado e fazer o usuário digitar novamente"
if(mode != "Valide aqui o mode"):
  print("preencha com suas linhas")
else:
  otimizar = 'time'
  caminho = ox.graph_from_place(place, network_type = mode)

  origem = meu_uber.geocode(end_or, timeout=None)
  destino = meu_uber.geocode(end_dest, timeout=None)

  origem_rota = (origem.latitude, origem.longitude)
  destino_rota = (destino.latitude, destino.longitude)

  onde_estou = ox.distance.nearest_nodes(caminho,
                                      origem_rota[1],
                                      origem_rota[0])

  onde_vou = ox.distance.nearest_nodes(caminho,
                                    destino_rota[1],
                                    destino_rota[0])

  caminho_corrida = nx.shortest_path(caminho,
                                  onde_estou,
                                  onde_vou,
                                  weight=otimizar)
  
  mapa = ox.plot_route_folium(caminho, caminho_corrida)

  ponto_verde = folium.Marker(
  location = origem_rota,
  popup = origem,
  icon = folium.Icon(color='green'))

  ponto_vermelho = folium.Marker(
  location = destino_rota,
  popup = destino,
  icon = folium.Icon(color='red'))

  ponto_verde.add_to(mapa)
  ponto_vermelho.add_to(mapa)
  mapa.show_in_browser() #vai abrir no navegador o seu mapa