#Yan Gianini Oliveira   202011128

def showMenuInicial():
    print("==========================================")
    print("   Trabalhando com Estrutura de Dados")
    print("==========================================")
    print("")
    print("1 - Pilha")
    print("2 - Fila")
    print("3 - Fila Circular")
    print("4 - Sair")
    print("")
    opc = int(input("Escolha a opção desejada: "))
    return opc

'''-----PILHA-----'''
def showPilha():
    print("===============================")
    print("           Pilha")
    print("===============================")
    print("1 - Inicializar/Limpar pilha")
    print("2 - Adicionar valor")
    print("3 - Remover valor")
    print("4 - Listar pilha")
    print("5 - Voltar para o menu anterior")
    opc = int(input("Escolha a opção desejada: "))
    return opc

global MAXP
MAXP = 5

def initP():
    global pilha, ponteiro
    pilha = []
    ponteiro = -1
    return

def pushP(valor):
    global pilha, ponteiro
    if ponteiro == MAXP - 1:
        print("Pilha cheia")
        return None

    pilha.append(valor)
    ponteiro = ponteiro + 1
    return

def popP():
    global pilha, ponteiro

    if ponteiro < 0:
        print("\nPilha Vazia")
        return None

    else:
        valor = pilha[ponteiro]
        del (pilha[ponteiro])
        ponteiro = ponteiro - 1
        return (valor)


'''-----FILA-----'''
def showFila():
    print("===============================")
    print("           Fila")
    print("===============================")
    print("1 - Inicializar/Limpar fila")
    print("2 - Adicionar valor")
    print("3 - Remover valor")
    print("4 - Listar fila")
    print("5 - Voltar para o menu anterior")
    opc = int(input("Escolha a opção desejada: "))
    return opc

global fila, sposF, rposF, MAXF

def initF():
    global fila, sposF, rposF, MAXF

    MAXF = 5
    fila = []
    sposF = 0
    rposF = 0

    return

def pushF(valor):
    global sposF, fila 
    
    if sposF == MAXF:
        print("Fila cheia")
        return
    
    fila.append(valor)
    sposF = sposF+1
    return

def popF():
    global rposF, fila 
    
    if rposF == sposF:
        print("Fila Vazia")
        return
    
    rposF = rposF + 1
    return fila[rposF-1]

def listarF():
    global sposF, rposF, fila 
    if rposF == sposF:
        print("Fila vazia")
        return
    
    for i in range(rposF, sposF):
        print(fila[i])
    
    return


'''-----FILA CIRCULAR-----'''
def showFilaCirc():
    print("===============================")
    print("           Fila Circular")
    print("===============================")
    print("1 - Inicializar/Limpar fila")
    print("2 - Adicionar valor")
    print("3 - Remover valor")
    print("4 - Listar fila")
    print("5 - Voltar para o menu anterior")
    opc = int(input("Escolha a opção desejada: "))
    return opc

global filaC, sposC, rposC, MAXC

def initC():
    global filaC, sposC, rposC, MAXC
    
    MAXC = 5
    filaC = []
    for i in range(0,MAXC):
        filaC.append(None)
    
    sposC = 0
    rposC = 0

    
def pushC(valor):
    global filaC, sposC 
    
    if(rposC == sposC and filaC[rposC]!=None) or (sposC+1 == rposC and rposC == 0) or (sposC + 1 == MAXC and rposC == 0):
        print("Fila cheia")
        return
    
    if sposC + 1 == MAXC and rposC != 0:
        sposC = 0
    
    filaC[sposC] = valor
    sposC = sposC + 1
    
    
def popC():
    global filaC, rposC 
    
    if (rposC == sposC and filaC[rposC] == None):
        print("Fila vazia")
        return
    
    if rposC+1 == MAXC:
         rposC = 0   
    
    valor = filaC[rposC]
    filaC[rposC] = None
    rposC = rposC + 1
    return valor
    

def listarC():
    for i in range(0, MAXC-1):
        print(filaC[i])
    return None

'''-----PROGRAMA-----'''
op = 0
while op != 4:
    if op == 0:
        op = showMenuInicial()

    elif op == 1:
        opc = 0
        while opc != 5:
            opc = showPilha()

            if opc == 1:
                initP()
                print("\n\npilha inicializada\n\n")
                break
            
            elif opc == 2:
                pushP(input("Valor: "))
                break

            elif opc == 3:
                popP()
                break

            elif opc == 4:
                if pilha == []:
                    print("\n\nPilha vazia\n\n")
                else:
                    print("\n")
                    print(pilha)
                    print("\n")
                break

            elif opc == 5:
                print("\n\nPilha fechada\n\n")

            else:
                print("\n\n\nNumero invalido\n\n\n")
                
            op = 0

    elif op == 2:
        opc = 0
        while opc != 5:
            opc = showFila()

            if opc == 1:
                initF()
                print("\n\nFila inicializada\n\n")
                break
            
            elif opc == 2:
                pushF(input("Valor: "))
                break

            elif opc == 3:
                popF()
                break

            elif opc == 4:
                print("\n")
                listarF()
                print("\n")
                break

            elif opc == 5:
                print("\n\nFila fechada\n\n") 

            else:
                print("\n\n\nNumero invalido\n\n\n")
 
            op = 0       

    elif op == 3:
        opc = 0
        while opc != 5:
            opc = showFilaCirc()

            if opc == 1:
                initC()
                print("\n\nFila inicializada\n\n")
                break
            
            elif opc == 2:
                pushC(input("Valor: "))
                break

            elif opc == 3:
                popC()
                break

            elif opc == 4:
                print("\n")
                listarC()
                print("\n")
                break

            elif opc == 5:
                print("\n\nFila fechada\n\n")

            else:
                print("\n\n\nNumero invalido\n\n\n")
                  
            op = 0   

    elif op == 4:
        op = 4
        print("obrigado por usar")
    
    else:
        print("\n\n\nNumero invalido\n\n\n")
        op = 0
