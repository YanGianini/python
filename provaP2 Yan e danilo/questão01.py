# Yan Gianini   202011128       Danilo Vasconcellos    202010702

class No:
    def __init__(self, num):
        self.num = num
        self.prox = None
    
    def __str__(self):
        return str(self.num)

    def getNum(self):
        return self.num

    def setNum(self, num):
        self.num = num

    def getProx(self):
        return self.prox

    def setProx(self, prox):
        self.prox = prox

class Lista:
    def __init__(self):
        self.inicio = None
    
    def vazia(self):
        return self.inicio == None

    def IncluirReg(self, val):
        temp = No(val)
        temp.setProx(self.inicio)
        self.inicio = temp

    def consultarReg(self, val):
        atual = self.inicio
        achou = False
        while atual != None and not achou:
            if atual.getNum() == val:
                achou = True
            else:
                atual = atual.getProx()

        return achou

    def excluirReg(self, val):
        atual = self.inicio
        achou = False
        anterior = None

        while atual != None and not achou:
            if atual.getNum() == val:
                achou = True
            else:
                anterior = atual
                atual = atual.getProx()
            
        if anterior == None:
            self.inicio = atual.getProx()
        elif atual != None:
            anterior.setProx(atual.getProx())

        return achou

    def contarReg(self):
        atual = self.inicio
        tam = 0
        while atual != None:
            tam += 1
            atual = atual.getProx()
        return tam

    def imprimirList(self):
        atual = self.inicio
        while atual != None:
            print(atual.getNum())
            atual = atual.getProx()
        return
    
def showMenu():
    print("1-Incluir registro")
    print("2-Consultar registro")
    print("3-Excluir registro")
    print("4-Contar registros")
    print("5-Imprimir lista")
    print("6-Abandonar programa")
    return int(input("Digite a opção desejada:"))

#Programa

lista1 = Lista()
op = 0
while op != 6:
    op = showMenu()
    #incluir
    if op == 1:
        opc = "S"
        while opc == "S":
            lista1.IncluirReg(input("Insira o valor que deseja incluir: "))
            opc = input("Deseja incluir outro valor? [S/N]: ").upper()
        continue

    #Consultar
    elif op == 2:
        opc = "S"
        while opc == "S":
            cons = lista1.consultarReg(input("Insira o valor que deseja consultar: "))
            if cons == True:
                print("Este valor esta na lista")
            else:
                print("Não encontrado")
            opc = input("Deseja consultar outro valor? [S/N]: ").upper()
        continue

    #excluir
    elif op == 3:
        opc = "S"
        while opc == "S":
            cons = lista1.excluirReg(input("Insira o valor que deseja excluir: "))
            if cons == True:
                print("Valor excluido")
            else: 
                print("Valor não encontrado")
            opc = input("Deseja excluir outro valor? [S/N]: ").upper()
        continue

    #contar
    elif op == 4:
        total = lista1.contarReg()
        print("Sua lista possui {} registros".format(total))
        continue

    #imprimir
    elif op == 5:
        if lista1.vazia == True:
            print("lista vazia")
        else:
            lista1.imprimirList()
        continue

    elif op == 6:
        print("---Programa Fechado---")

    else:
        print("Opção não encontrada")
        
        
