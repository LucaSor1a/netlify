import requests

import requests
pagina = 'https://corona-stats.online?source=1'
page = requests.get(pagina)
texto = page.text
texto = texto.split("\n")
estadisticas = {}
for linea in texto:
    if linea.startswith("║"):
        linea = linea.replace("║ ","")
        if linea[0].isdigit():
            #print(linea)
            valores = linea.split("│")
            estadisticas[valores[1].strip()]={'pos':valores[0].strip(),
                                              'pais': valores[1].strip(),
                                              'confirmado': valores[2].strip(),
                                              'muertes': valores[3].strip(),
                                              'cfr': valores[4].strip(),
                                              '1dia': valores[5].strip(),
                                              '1semana': valores[6].replace(" ║","")}

pais = input("Pais que le interesa(Ej: Argentina (AR)): ")

for clave in estadisticas.keys():
    if estadisticas[clave]['pais'] == pais:
        print("\nPais: {pais} - Confirmados: {conf}".format(pais=estadisticas[clave]['pais'],
                                                          conf=estadisticas[clave]['confirmado']))
