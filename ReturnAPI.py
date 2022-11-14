import json, requests, os
import reconhecimento as rec
path_incial = os.path.dirname(__file__)
tipo_comida = 'Fruta'

#Consulta a fruta na API e retorna um dicionario com as informações nutricionais
def Consult(food):    
    #Conecta a API. Retorna -1 caso a conexão falhe       
    try:                          
        request = requests.get(f"https://api.edamam.com/api/nutrition-data?app_id=345f851a&app_key=0dbb040ae0b77d131e69498dd31dde25&nutrition-type=cooking&ingr=100 g {food}")
        response_info = json.loads(request.content)
        nutrients=response_info['totalNutrients']
    except:
        return -1                   

    #Verifica se a fruta possui o nutriente
    def ConsultJson(info): 
        try:
            return {
                'total':nutrients[info]['quantity'],
                'unit': nutrients[info]['unit']
            }
        except:
            return {
                'total':0,
                'unit': 'g'
            }

    #Dicionario com as infos nutricionais
    dict={                          
        "Food":food,
        "Kcal": ConsultJson('ENERC_KCAL'),
        "Carb": ConsultJson('CHOCDF'),
        "Protein": ConsultJson('PROCNT'),
        "TotalFat": ConsultJson('FAT'),
        "FatSAT": ConsultJson('FASAT'),
        "Sodium": ConsultJson('NA'),
        "VitA": ConsultJson('VITA_RAE'),
        "VitB6": ConsultJson('VITB6A'),
        "VitC": ConsultJson('VITC')
        }       
               
    return dict

lista_treco = rec.carregar_nome_fruta(tipo_comida) #inicia o algoritimo
path = path_incial #Salva ele
food = rec.reconhecer(path,lista_treco) #reconhece fruta

dicionario = Consult(food)

print(f"Informações da Fruta - 100g\nNome: {dicionario['Food']}\nCalorias: {dicionario['Kcal']}\nCaboidratos: {dicionario['Carb']}\nProteinas: {dicionario['Protein']}\nGorduras Totais: {dicionario['TotalFat']}\nGorduras Saturadas: {dicionario['FatSAT']}\nSódio: {dicionario['Sodium']}\nVitamina A: {dicionario['VitA']}\nVitamina B6: {dicionario['VitB6']}\nVitamina C: {dicionario['VitC']}")