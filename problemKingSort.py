class king:
    """
    Classe para definir um objeto do tipo rei, cada objeto terá 3 atributos, são eles:
    nome, o numero em algarismos romanos e o valor daquele número romano em algarismos arábicos
    """
    def __init__(self, name, numberRoman):
        self.name = name
        self.numberRoman = numberRoman                                                      
        romanValue = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}                          #Cálculo do número arábico de acordo com o número romano passado para inicialização
        intValue = 0
        for i in range(len(numberRoman)):
            if i > 0 and romanValue[numberRoman[i]] > romanValue[numberRoman[i-1]]:
                intValue += romanValue[numberRoman[i]] - 2*romanValue[numberRoman[i-1]]
            else:
                intValue += romanValue[numberRoman[i]]
        self.numberInt = intValue
    
    def __repr__(self):
        """
        Sobrecarga do operador __repr__ para que o objeto seja printado no seguinte formato:
        NOME NÚMERO
        """
        return(self.name + " " + self.numberRoman)

class kingSort:                                                                                                 #Classe que contém o método explicitado no PDF
    def getSortedList(self,input):
        """
        Função para ordenar os nomes dos reis dado no vetor input
        """
        kingIn = input
        kingArray = []

        for i in kingIn:
            currName = i.split(" ")[0]
            currNumber = i.split(" ")[1]
            kingArray.append(king(currName, currNumber))                                                        #Criação de um vetor de objetos do tipo rei

        sortedKingsName = sorted(kingArray, key = lambda e:e.name)                                              #Utilização da função lambda como chave para a função sorted ordenar os nomes em ordem alfabética
        
        n = len(sortedKingsName)
        for i in range(n):                                                                                      #Trecho baseado em Bouble Sort para ordenação dos números
            for j in range(0, n-i-1):
                if sortedKingsName[j].name == sortedKingsName[j+1].name:                                        #Somente compara os números quando os nomes são iguais
                    if sortedKingsName[j].numberInt > sortedKingsName[j+1].numberInt:
                        sortedKingsName[j], sortedKingsName[j+1] = sortedKingsName[j+1], sortedKingsName[j]
        return sortedKingsName                                                                                  #Retorna um vetor com os nomes ordenados


if __name__ == "__main__":
    kingDict = {                                                                                                #Dicionário com os exemplos dados dados no PDF
        "Ex0": ["Louis IX", "Louis VIII"],
        "Ex1": ["Louis IX", "Philippe II"],
        "Ex2": ["Richard III", "Richard I", "Richard II"],
        "Ex3": ["John X", "John I", "John L", "John V"],
        "Ex4": ["Philippe VI", "Jean II", "Charles V", "Charles VI", "Charles VII", "Louis XI"],
        "Ex5": ["Philippe II", "Philip II"]
    } 
    k1 = kingSort()
    for i,j in kingDict.items():
        print(f"Lista {i} não ordenada: {j}")
        print(f"Lista {i} ordenada: {k1.getSortedList(j)}")
        print("\n")
