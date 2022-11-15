import json, requests, os
import reconhecimento as rec #import reconhecimento.py
from flask import Flask, make_response, jsonify, request
# from werkzeug.utils import secure_filename

path_inicial = os.path.dirname(__file__)
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
    #Dicionario c
    # om as infos nutricionais
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

app = Flask(__name__)

UPLOAD_FOLDER = path_inicial
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

#Define "rota" padrão da API 
@app.route('/', methods=['POST'])

def Main():
    file = request.files['picture'] #chave esperada
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], 'Fruta.jpg')) #salva e renomeia arquivo para "Fruta.jpg"

    list_fruits = rec.carregar_nome_fruta(tipo_comida) #inicia o algoritimo
    path = path_inicial #Salva ele
    food = rec.reconhecer(path,list_fruits) #reconhece fruta
    return make_response(
        jsonify(Consult(food)) #response in json
    )
#Inicia API e define host como sendo IP da máquina onde está hospedado
app.run(host='192.168.1.252')