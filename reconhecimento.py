import io
import os
from datetime import datetime
from turtle import width
import cv2 as cv # O famigerado

from google.cloud import vision_v1p3beta1 as vision

#Chave para usar o serviços do Google Vision.
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'chave_cliente.json'

#ATENÇÃO O CAMINHO DA FOTO DEVE SER MUDADO DE ACORDO COM A FOTO QUE O USUARIO QUEIRA UTILIZAR.
path = "C:/Users/ThatWonderfulLife/Desktop/APS6/"

tipo_comida = 'Fruta'


#Carrega os nomes das frutas que estão no arquivo Fruta.dict e retorna uma lista com os nomes.
def carregar_nome_fruta (tipo_comida):
    nomes = [line.rstrip('\n').lower() for line in open(tipo_comida + '.dict')]
    return nomes

def reconhecer(path, lista_frutas):
    t_inicial = datetime.now()
    #Lê img do path
    img = cv.imread(path)
    #define altura e largura da imagem
    height,width = img.shape[:2]
    #deixa a imagem menor
    img = cv.resize(img, (800, int( (height * 800) / width) ) )
    #salva a imagem temporaria no path dado
    cv.imwrite(path + "cortada.jpg", img)
    #definindo onde q fica a foto cortada
    path_foto_cortada = (f"{path}cortada.jpg")
    #Puxa cliente do google Vision
    cliente = vision.ImageAnnotatorClient()

    #Lê imagem
    with io.open(path_foto_cortada, 'rb') as arquivo_imagem:
        conteudo = arquivo_imagem.read()
    #define tipo da imagem como seu proprio conteudo para o Visions (nao entendo como o vision funciona só aceito)
    imagem = vision.types.Image(conteudo = conteudo)
    #Puxa todos os resultados que o Visions deu e salva numa variavel
    resposta = cliente.label_detection(imagem = imagem)
    labels = resposta.anotacoes_label
    #A variavel é uma lista, esse pedaço itera todos os itens da lista e arredonda os valores que vieram de brinde também, depois divide eles em 'label' e 'Pontos' pra cada resultado
    for label in labels:
        descricao = label.description.lower()
        pontos = round(label.score,2)
        #mostra resultados que vieram
        print(f"label -> {descricao} pontos -> {pontos}")
        #se o nome de um dos resultados tiver na lista das frutas ele coloca 1 texto indicando qual fruta é e faz 1 quadrado em volta dela tb. Abre a imagem pra mostrar como ficou
        if (descricao in lista_frutas):
            cv.putText(img,descricao.upper(),(300,150),cv.FONT_HERSHEY_TRIPLEX,1,(50,50,200),2)
            cv.imshow("Fruta",img)
            cv.waitKey(0)

            break #ESSE BREAK SERVE PRA ELE SÒ DAR PRINT NA PRIMEIRA FRUTA

#inicia o algoritimo
lista_treco = carregar_nome_fruta(tipo_comida)
#mostra o resultado
print(lista_treco)
#Salva ele
path = (f'{path}laranja.jpg')
#reconhece fruta
reconhecer(path,lista_treco)
