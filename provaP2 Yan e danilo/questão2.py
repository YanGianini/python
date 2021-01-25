#Yan Gianini        20201118    Danilo Vasconcellos       202010702

class No:
    def __init__(self, chave = None, esquerda = None, direita = None):
        self.chave = chave
        self.esquerda = esquerda 
        self.direita = direita 
        
    def __repr__(self):
        return "%s <- %s -> %s" % (self.esquerda and self.esquerda.chave,
                                   self.chave,
                                   self.direita and self.direita.chave)

def Ordem(raiz):
    if not raiz:
        return
    
    Ordem(raiz.esquerda)
    print(raiz)
    Ordem(raiz.direita)
    
def incluir(raiz, no):
    if raiz is None:
        raiz = no
    
    elif raiz.chave < no.chave:
        if raiz.direita is None:
            raiz.direita = no
        else:
            incluir(raiz.direita, no)
    
    else:
        if raiz.esquerda is None:
            raiz.esquerda = no
        else:
            incluir(raiz.esquerda, no)

def consultar(raiz, chave):
    if raiz is None:
        return None 
    
    if raiz.chave == chave:
        return raiz
    
    if raiz.chave < chave:
        return consultar(raiz.direita, chave)
    
    return consultar(raiz.esquerda, chave)

def maior(raiz):
    no = raiz
    while no.direita is not None:
        no = no.direita
    return no.chave

def menor(raiz):
    no = raiz
    while no.esquerda is not None:
        no = no.esquerda
    return no.chave

def showMenu():
    print("---Árvore binária---")
    print("1-Incluir nó")
    print("2-Consultar nó")
    print("3-Maior nó")
    print("4-Menor nó")
    print("5-Imprimir lista")
    print("6-Gravar árvore em disco")
    print("7-Abandonar programa")
    return int(input("Digite a opção desejada: "))

def em_ordem(raiz, arq):
    if not raiz:
        return
    em_ordem(raiz.esquerda, arq)
    arq.write(str(raiz.chave)+"\n")
    em_ordem(raiz.direita, arq)


def gravarArq(raiz):
    nome = input("Insira o nome do arquivo: ")+".txt"
    arq = open(nome, "w")
    em_ordem(raiz, arq)
    arq.close()
    return nome

#Programa

raiz = No()
op = 0
while op != 7:
    op = showMenu()
    #Incluir nó
    if op == 1:
        opc = "S"
        while opc == "S":
            if raiz.chave == None:
                raiz = No(int(input("Insira o Nó que deseja incluir: ")))
            else:
                incluir(raiz, No(int(input("Insira o Nó que deseja incluir: "))))

            opc = input("Deseja incluir outro nó? [S/N]: ").upper()
        continue

    #Consultar nó
    elif op == 2:
        opc = "S"
        while opc == "S":
            busc = consultar(raiz, int(input("Digite o valor que deseja consultar: ")))
            if busc == None:
                print("Valor não encontrado")
            else:
                print(busc)
            
            opc = input("Deseja consultar outro valor? [S/N]: ").upper()
        continue

    #Maior nó
    elif op == 3:
        val = maior(raiz)
        if val == None:
            print("Arvore sem valores")
        else: 
            print("O maior valor é: ", val)

    #Menor nó
    elif op == 4:
        val = menor(raiz)
        if val == None:
            print("Arvore sem valores")
        else: 
            print("O menor valor é: ", val)

    #Imprimir lista
    elif op == 5:
        if raiz.chave == None:
            print("Arvore vazia")
        else:
            Ordem(raiz)
        continue

    #Gravar árvore em disco
    elif op == 6:
        print("A sua arvore foi salva em", gravarArq(raiz))

    #Abandonar programa
    elif op == 7:
        print("---Programa Fechado---")

    else:
        print("Opção não encontrada")
        
