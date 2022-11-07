import json, requests, os
import reconhecimento as rec
path_incial = os.path.dirname(__file__)
tipo_comida = 'Fruta'


def Consult(food):
    #função MAIN                
    try:
        #consome API atraves de request                            
        request = requests.get(f"https://api.edamam.com/api/nutrition-data?app_id=345f851a&app_key=0dbb040ae0b77d131e69498dd31dde25&nutrition-type=cooking&ingr=100 g {food}")
        response_info = json.loads(request.content)
        nutrients=response_info['totalNutrients']
    except:
        #retorno caso API não responda
        return -1                   

    def ConsultJson(info): 
        #consulta se valor existe     
        try:
            return {
                'total':nutrients[info]['quantity'],
                'unit': nutrients[info]['unit']
            }
        except:
            #se valor não existir
            return {
                'total':0,
                'unit': 'g'
            }
    #dicionário de saída
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
print(lista_treco) #mostra o resultado
path = path_incial #Salva ele

food = rec.reconhecer(path,lista_treco) #reconhece fruta
print(food)

print(Consult(food))