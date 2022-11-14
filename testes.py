def Consult():
    dict={                          
        "Food":"ee",
        "Kcal": 212,
        "Carb": 333,
        "Protein": 4444,
        "TotalFat": 5555,
        "FatSAT": 66666,
        "Sodium": 77777,
        "VitA": 888888,
        "VitB6": 9999999,
        "VitC": 93939393939
        }       
               
    return dict

dicionario = Consult()

print(f"Informações da Fruta - 100g\nNome: {dicionario['Food']}\nCalorias: {dicionario['Kcal']}\nCaboidratos: {dicionario['Carb']}\nProteinas: {dicionario['Protein']}\nGorduras Totais: {dicionario['TotalFat']}\nGorduras Saturadas: {dicionario['FatSAT']}\nSódio: {dicionario['Sodium']}\nVitamina A: {dicionario['VitA']}\nVitamina B6: {dicionario['VitB6']}\nVitamina C: {dicionario['VitC']}")