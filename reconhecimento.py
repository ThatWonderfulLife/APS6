import io
import os
import cv2 as cv
from google.cloud import vision_v1p3beta1 as vision


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.path.dirname(__file__) + '\\chave.json' #Chave para usar o serviços do Google Vision.

#pega o path atual do arquivo 'reconhecimento.py'
path_inicial = os.path.dirname(__file__)
tipo_comida = 'Fruta'

#Carrega os nomes das frutas que estão no arquivo Fruta.dict
def carregar_nome_fruta (tipo_comida):
    nomes = [line.rstrip('\n').lower() for line in open(f"{path_inicial}\\{tipo_comida}.dict")]
    return nomes

def reconhecer(path_inicial, lista_frutas):
    print(f'{path_inicial}\\Fruta.png')
    img = cv.imread(f'{path_inicial}\\Fruta.jpg')  #Lê img do path
    height,width = img.shape[:2] #define altura e largura da imagem
    img = cv.resize(img, (800, int( (height * 800) / width) ) ) #deixa a imagem menor
    
    cv.imwrite(path_inicial + "\\cortada.jpg", img) #salva a imagem temporaria no path dado
    path_foto_cortada = (f"{path_inicial}\\cortada.jpg") #definindo onde q fica a foto cortada
    
    cliente = vision.ImageAnnotatorClient() #puxa cliente do google Vision

    with io.open(path_foto_cortada, 'rb') as arquivo_imagem: #Lê imagem
        conteudo = arquivo_imagem.read()
    
    imagem = vision.types.Image(content = conteudo) #define tipo da imagem como seu proprio conteudo para o Visions (nao entendo como o vision funciona só aceito)
   
    resposta = cliente.label_detection(image = imagem) #puxa todos os resultados que o Visions deu e salva
    labels = resposta.label_annotations
    
    for label in labels: #A variavel é uma lista, esse pedaço itera todos os itens da lista e arredonda os valores que vieram de brinde também, depois divide eles em 'label' e 'Pontos' pra cada resultado
        descricao = label.description.lower()
        # pontos = round(label.score,2)
        
        if (descricao in lista_frutas): #valida se descrição recebida está na lista de frutas
            # cv.putText(img,descricao.upper(),(300,150),cv.FONT_HERSHEY_TRIPLEX,1,(50,50,200),2)
            # cv.waitKey(0)
            return descricao #retorna nome da fruta

list_fruits = carregar_nome_fruta(tipo_comida) #inicia o algoritmo
path = path_inicial #Salva ele

food = reconhecer(path,list_fruits) #reconhece fruta