import io
import os
from datetime import datetime
from turtle import width
import cv2 as cv # O famigerado

from google.cloud import vision_v1p3beta1 as vision

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.path.dirname(__file__) + '\\chave.json' #Chave para usar o serviços do Google Vision.

# pega o path atual do arquivo 'reconhecimento.py'
path_incial = os.path.dirname(__file__)

tipo_comida = 'Fruta'


#Carrega os nomes das frutas que estão no arquivo Fruta.dict e retorna uma lista com os nomes.
def carregar_nome_fruta (tipo_comida):
    nomes = [line.rstrip('\n').lower() for line in open(f"{path_incial}\\{tipo_comida}.dict")]
    return nomes

def reconhecer(path_incial, lista_frutas):
    print("Passou 1")
    img = cv.imread(f'{path_incial}\\Fruta.jpg')  #Lê img do path
    print("Passou 2")
    height,width = img.shape[:2] #define altura e largura da imagem
    print("Passou 3")
    img = cv.resize(img, (800, int( (height * 800) / width) ) ) #deixa a imagem menor
    print("Passou 4")
    cv.imwrite(path_incial + "\\cortada.jpg", img) #salva a imagem temporaria no path dado
    print("Passou 5")
    path_foto_cortada = (f"{path_incial}\\cortada.jpg") #definindo onde q fica a foto cortada
    print("Passou 6")
    cliente = vision.ImageAnnotatorClient()  #Puxa cliente do google Vision
    print("Passou 7")
    
    with io.open(path_foto_cortada, 'rb') as arquivo_imagem: #Lê imagem
        conteudo = arquivo_imagem.read()
    
    imagem = vision.types.Image(content = conteudo) #define tipo da imagem como seu proprio conteudo para o Visions (nao entendo como o vision funciona só aceito)
   
    resposta = cliente.label_detection(image = imagem)  #Puxa todos os resultados que o Visions deu e salva numa variavel
    labels = resposta.anotacoes_label
    
    for label in labels: #A variavel é uma lista, esse pedaço itera todos os itens da lista e arredonda os valores que vieram de brinde também, depois divide eles em 'label' e 'Pontos' pra cada resultado
        descricao = label.description.lower()
        pontos = round(label.score,2)
        
        print(f"label -> {descricao} pontos -> {pontos}") #mostra resultados que vieram
        
        if (descricao in lista_frutas): #se o nome de um dos resultados tiver na lista das frutas ele coloca 1 texto indicando qual fruta é e faz 1 quadrado em volta dela tb. Abre a imagem pra mostrar como ficou
            cv.putText(img,descricao.upper(),(300,150),cv.FONT_HERSHEY_TRIPLEX,1,(50,50,200),2)
            cv.imshow("Fruta",img)
            cv.waitKey(0)

            break #ESSE BREAK SERVE PRA ELE SÒ DAR PRINT NA PRIMEIRA FRUTA

lista_treco = carregar_nome_fruta(tipo_comida) #inicia o algoritimo
print(lista_treco) #mostra o resultado
path = path_incial #Salva ele

reconhecer(path,lista_treco) #reconhece fruta
