#No início, importamos alguns módulos para serem usados no código.
import random #Usamos o random para sortear 'X' ou 'O' no Jogador vs Jogador e para sortear as jogadas da CPU no Jogador vs CPU.
import os #Possibilita a criação da função 'limpar' que limpa o terminal para execução do jogo
import sys #Possibilita encerrarmos o jogo quando desejado
import time #Faz o computador demorar uns segundos para jogar
global limpar
limpar="os.system('cls' if os.name == 'nt' else 'clear')" #Executa um comando no terminal (Shell) para limpá-lo.
#====================================================== JOGADOR VS JOGADOR ======================================================
def jogo_inteiro():
    def escolha(): #Escolhe qual sigla representará tal jogador de forma randômica
        if random.randint(1,2) == 1:
            return jog1
        else:
            return jog2
    jog1='X'
    jog2='O'
    if escolha()==jog1:
            jogador1='X'
            jogador2='O'
    else:
            jogador1='O'
            jogador2='X'
    jogadas1 = 0
    jogadas2 = 0
    ganhou1 = " "
    ganhou2 = " "
    posicoes = [
                [1,2,3],
                [4,5,6],
                [7,8,9]
                        ] #Lista que representa cada coordenada por uma variável
    eval (limpar)
    v1=str(posicoes[0][0]) #Transformamos as casas da matriz anterior em strings e armazenamos em variáveis
    v2=str(posicoes[0][1])
    v3=str(posicoes[0][2])
    v4=str(posicoes[1][0])
    v5=str(posicoes[1][1])
    v6=str(posicoes[1][2])
    v7=str(posicoes[2][0])
    v8=str(posicoes[2][1])
    v9=str(posicoes[2][2])
    def tabuleiro(v1, v2, v3, v4, v5, v6, v7, v8, v9): #Definimos uma função que recebe as variáveis das casas e printa o tabuleiro
        print('|===============================================|')
        print('|   Jogador 1(%s)        |   Jogador 2(%s)        |'%(jogador1, jogador2))
        print('|===============================================|')
        print ('|==========>> Tabuleiro Referencial <<==========|')
        print('|===============================================|')
        print ('|      ''          '"|"'           '"|"'                  |')
        print ('|       ''    %s   '" |"'    %s     '" |"'    %s             |'%(v1,v2,v3))
        print ('|       ''         '"|"'           '"|"'                  |')
        print ('|    ''------------+-----------+------------      |')
        print ('|      ''          '"|"'           '"|"'                  |')
        print ('|       ''    %s   '" |"'    %s     '" |"'    %s             |'%(v4,v5,v6))
        print ('|       ''         '"|"'           '"|"'                  |')
        print ('|    ''------------+-----------+------------      |')
        print ('|      ''          '"|"'           '"|"'                  |')
        print ('|       ''    %s   '" |"'    %s     '" |"'    %s             |'%(v7,v8,v9))
        print ('|       ''         '"|"'           '"|"'                  |')
        print ("|===============================================|")
    tabuleiro(v1, v2, v3, v4, v5, v6, v7, v8, v9)
    start = True
    while start == True:
        start = True
        if start == True:
            print        ('|===============================================|')
            jogou = input("-> Jogador 1: Digite a coordenada de sua jogada: ")  #Pede para o jogador 1 fazer sua jogada          
            def analise(): #Função que analisa se a casa jogada é válida. Se a casa já está ocupada ou se a coordenada inserida é inválida (<1 ou >9) ele retorna falso e não concretiza a jogada
                 if jogou == v1 or jogou == v2 or jogou == v3 or jogou == v4 or jogou == v5 or jogou == v6 or jogou == v7 or jogou == v8 or jogou == v9:
                    return True
                 else:
                    return False
            while analise()==False:
                print ("x_x Coordenada inválida. Tente novamente.")
                jogou = input("-> Jogador 1: Digite a coordenada de sua jogada: ") #Se a validação der negativo, ele pede para inserir novamente a jogada, até que seja um número válido
                analise() 
            while analise()==True: #Se a validação der positiva, ele substitui o número da casa pela sigla que representa o jogador
                jogou=int(jogou[0])
                for l in range(3):
                    for c in range(3):
                        if jogou == posicoes[l][c]:
                            posicoes[l][c] = jogador1 #Substitui o valor da casa jogada pela sigla que representa o jogador ('X' ou 'O')
                            jogadas1 = jogadas1 + 1 #Conta as jogadas do jogador 1, é importante para a definição de vitória
                            eval(limpar)
            v1=str(posicoes[0][0]) #Atualiza as variáveis das casas para as casas com siglas
            v2=str(posicoes[0][1])
            v3=str(posicoes[0][2])
            v4=str(posicoes[1][0])
            v5=str(posicoes[1][1])
            v6=str(posicoes[1][2])
            v7=str(posicoes[2][0])
            v8=str(posicoes[2][1])
            v9=str(posicoes[2][2])
            tabuleiro(v1, v2, v3, v4, v5, v6, v7, v8, v9) #Printa o tabuleiro atualizado
            if v1 == v2 == v3 == jogador1 or\
               v4 == v5 == v6 == jogador1 or\
               v7 == v8 == v9 == jogador1 or\
               v1 == v4 == v7 == jogador1 or\
               v2 == v5 == v8 == jogador1 or\
               v3 == v6 == v9 == jogador1 or\
               v1 == v5 == v9 == jogador1 or\
               v3 == v5 == v7 == jogador1:
                ganhou1=True #Verifica se o jogador 1 ganhou
            else:
                ganhou1=False
            if ganhou1==True: 
                    print ('%s-----------------------%s'%(jogador1,jogador1))
                    print ("| Jogador 1 (%s) ganhou! |" %jogador1)
                    print ('%s-----------------------%s'%(jogador1,jogador1))
                    start=False
            if jogadas1==5 and ganhou2 == False and ganhou1 == False: #Verifica se deu velho. Os requisitos são que o jogador 1 esteja na sua última jogada e ninguém ganhou ainda
                    print('\nX----------------------O')
                    print("| BAH!... DEU VELHA!!! |")
                    print('O----------------------X')
                    start=False
            #==================================================================
            if start == True: #Se ninguém ganhou, o jogo ainda roda, partindo para as jogadas do jogador 2
                print        ('|===============================================|')
                jogou = input("-> Jogador 2: Digite a coordenada de sua jogada: ")
                while analise()==False:
                    print ("x_x Coordenada inválida. Tente novamente.")
                    jogou = input("-> Jogador 2: Digite a coordenada de sua jogada: ")
                    analise()
                while analise()==True:
                    jogou=int(jogou[0])
                    for l in range(3):
                        for c in range(3):
                            if jogou == posicoes[l][c]:
                                posicoes[l][c] = jogador2 #Mesma coisa que no jogador 1, porém altera a coordenada pela sigla que representa o jogador 2
                                jogadas2 = jogadas2 + 1
                                eval(limpar)                
                v1=str(posicoes[0][0])
                v2=str(posicoes[0][1])
                v3=str(posicoes[0][2])
                v4=str(posicoes[1][0])
                v5=str(posicoes[1][1])
                v6=str(posicoes[1][2])
                v7=str(posicoes[2][0])
                v8=str(posicoes[2][1])
                v9=str(posicoes[2][2])
                tabuleiro(v1, v2, v3, v4, v5, v6, v7, v8, v9)
                if v1 == v2 == v3 == jogador2 or\
                    v4 == v5 == v6 == jogador2 or\
                    v7 == v8 == v9 == jogador2 or\
                    v1 == v4 == v7 == jogador2 or\
                    v2 == v5 == v8 == jogador2 or\
                    v3 == v6 == v9 == jogador2 or\
                    v1 == v5 == v9 == jogador2 or\
                    v3 == v5 == v7 == jogador2:
                        ganhou2=True
                else:
                    ganhou2=False #Verifica se o jogador 2 ganhou
                if ganhou2==True:
                    print ('%s----------------------%s'%(jogador2,jogador2))
                    print ("| Jogador 2(%s) ganhou! |" %jogador2)
                    print ('%s----------------------%s'%(jogador2,jogador2))
                    start=False
        while start==False:
            restart=input("\nJogar novamente?(S/N): ") #Quando alguém ganha ou dá velha, o jogo para, pedindo se vai querer reinicar ou ir para o menu
            print('\n')
            if restart=='S' or restart=='s':
                jogo_inteiro() #Reproduz o jogo novamente
            elif restart=='N' or restart=='n':
                break
                JOGO=False #Volta ao menu
            else:
                start=False
#============================================================== JOGO VS PC ==================================================#
def jogo_versus(): 
        jogadas1 = 0
        ganhou1 = " "
        ganhoupc = " "
        posicoes = [
                    [1,2,3],
                    [4,5,6],
                    [7,8,9]
                            ] #Define as posições, como no Jogador vs Jogador
        jogador1='X' #Define o usuário como X e a CPU como O
        computador='O'
        eval (limpar)
        v1=str(posicoes[0][0])
        v2=str(posicoes[0][1])
        v3=str(posicoes[0][2])
        v4=str(posicoes[1][0])
        v5=str(posicoes[1][1])
        v6=str(posicoes[1][2])
        v7=str(posicoes[2][0])
        v8=str(posicoes[2][1])
        v9=str(posicoes[2][2])
        def tabuleiro(v1, v2, v3, v4, v5, v6, v7, v8, v9):
            print('|===============================================|')
            print('|   Jogador(%s)        |   Computador(%s)         |'%(jogador1, computador))
            print('|===============================================|')
            print ('|==========>> Tabuleiro Referencial <<==========|')
            print('|===============================================|')
            print ('|      ''          '"|"'           '"|"'                  |')
            print ('|       ''    %s   '" |"'    %s     '" |"'    %s             |'%(v1,v2,v3))
            print ('|       ''         '"|"'           '"|"'                  |')
            print ('|    ''------------+-----------+------------      |')
            print ('|      ''          '"|"'           '"|"'                  |')
            print ('|       ''    %s   '" |"'    %s     '" |"'    %s             |'%(v4,v5,v6))
            print ('|       ''         '"|"'           '"|"'                  |')
            print ('|    ''------------+-----------+------------      |')
            print ('|      ''          '"|"'           '"|"'                  |')
            print ('|       ''    %s   '" |"'    %s     '" |"'    %s             |'%(v7,v8,v9))
            print ('|       ''         '"|"'           '"|"'                  |')
            print ("|===============================================|")
        tabuleiro(v1, v2, v3, v4, v5, v6, v7, v8, v9)
        start = True
        while start == True:
            start = True
            if start == True:
                print ('|===============================================|')
                jogou = input("-> Jogador, digite a coordenada de sua jogada: ")
                def analise(): 
                     if jogou == v1 or jogou == v2 or jogou == v3 or jogou == v4 or jogou == v5 or jogou == v6 or jogou == v7 or jogou == v8 or jogou == v9:
                        return True
                     else:
                        return False
                while analise()==False: 
                    print ("x_x Coordenada inválida. Tente novamente.")
                    jogou = input("-> Jogador, digite a coordenada de sua jogada: ")
                    analise() 
                while analise()==True: 
                    jogou=int(jogou[0])
                    for l in range(3):
                        for c in range(3):
                            if jogou == posicoes[l][c]:
                                posicoes[l][c] = jogador1
                                jogadas1 = jogadas1 + 1
                                eval(limpar)                                           
                v1=str(posicoes[0][0])
                v2=str(posicoes[0][1])
                v3=str(posicoes[0][2])
                v4=str(posicoes[1][0])
                v5=str(posicoes[1][1])
                v6=str(posicoes[1][2])
                v7=str(posicoes[2][0])
                v8=str(posicoes[2][1])
                v9=str(posicoes[2][2])
                tabuleiro(v1, v2, v3, v4, v5, v6, v7, v8, v9)
                if v1 == v2 == v3 == jogador1 or\
                   v4 == v5 == v6 == jogador1 or\
                   v7 == v8 == v9 == jogador1 or\
                   v1 == v4 == v7 == jogador1 or\
                   v2 == v5 == v8 == jogador1 or\
                   v3 == v6 == v9 == jogador1 or\
                   v1 == v5 == v9 == jogador1 or\
                   v3 == v5 == v7 == jogador1:
                    ganhou1=True
                else:
                    ganhou1=False
                if ganhou1==True:
                        print ('%s-----------------------%s'%(jogador1,jogador1))
                        print ("| Jogador (%s) ganhou!   |" %jogador1)
                        print ('%s-----------------------%s'%(jogador1,jogador1))
                        start=False
                if jogadas1==5 and ganhoupc == False and ganhou1 == False:
                        print('\nX----------------------O')
                        print("| BAH!... DEU VELHA!!! |")
                        print('O----------------------X')
                        start=False
                if start == True:
                    jogou=random.randint(1, 9) #Sorteia a jogada da CPU
                    jogou=str(jogou)
                    analise() #Analisa a jogada da CPU da mesma forma que do jogador
                    while analise()==False: #Se a análise for negativa, ele repete o sorteio até que a saída seja um número válido
                          jogou=random.randint(1, 9)
                          jogou=str(jogou)
                          analise()
                    while analise()==True:
                        jogou=int(jogou[0])
                        for l in range(3):
                            for c in range(3):
                                if jogou == posicoes[l][c]:
                                    posicoes[l][c] = computador #Substitui a coordenada sorteada pela sigla do computador
                                    eval(limpar)
                    v1=str(posicoes[0][0])
                    v2=str(posicoes[0][1])
                    v3=str(posicoes[0][2])
                    v4=str(posicoes[1][0])
                    v5=str(posicoes[1][1])
                    v6=str(posicoes[1][2])
                    v7=str(posicoes[2][0])
                    v8=str(posicoes[2][1])
                    v9=str(posicoes[2][2])
                    tabuleiro(v1, v2, v3, v4, v5, v6, v7, v8, v9)
                    print('|Bolando uma estratégia para vencer você...     |')#Printa uma fala para o computador antes do time.sleep
                    time.sleep(1)# Serve para esperar 1 segundos antes do computador printar sua jogada
                    print ("|Eu joguei no %d, tente me vencer!               |"%jogou) #Printa a jogada do computador, para facilitar o entendimento 
                    if v1 == v2 == v3 == computador or\
                        v4 == v5 == v6 == computador or\
                        v7 == v8 == v9 == computador or\
                        v1 == v4 == v7 == computador or\
                        v2 == v5 == v8 == computador or\
                        v3 == v6 == v9 == computador or\
                        v1 == v5 == v9 == computador or\
                        v3 == v5 == v7 == computador:
                            ganhoupc=True
                    else:
                        ganhoupc=False
                    if ganhoupc==True:
                        print ('%s-----------------------------------%s'%(computador, computador))
                        print ("| Eu ganhei! Mais sorte na próxima! |")
                        print ("| Computador ganhou.                |")
                        print ('%s-----------------------------------%s'%(computador, computador))
                        start=False
            while start==False:
                restart=input("\nJogar novamente?(S/N):")
                print('\n')
                if restart=='S' or restart=='s':
                    jogo_versus()
                elif restart=='N' or restart=='n':
                    break
                    JOGO=False
                else:
                    start=False
#========================================================== DEFINIÇÃO DO MENU ==============================================
JOGO=False #Define como falso para assim que o jogo seja executado, o menu apareça
while JOGO==False:
    eval(limpar) #Limpa todo o terminal antes do jogo começar, deixando uma interface limpa
    print('X===============================================O')
    print('|   SEJA BEM-VINDO AO JOGO DA VELHA EM PYTHON!  |\n|                   DIVIRTA-SE                  |')
    print('|===============================================|')
    print('|=================>> MENU <<====================|')
    print('|                                               |')
    print('| 1 - Versus (Jogador contra Jogador)           |')
    print('| 2 - Jogador contra CPU (Fácil)                |')
    print('| 3 - Sair                                      |')
    print('|                                               |')
    print('O===============================================X')
    jogo=input(" Digite a opção de jogo (1/2/3): ") #Pede para o jogador o que ele quer fazer
    if jogo == '1':
        JOGO=True
        jogo_inteiro() #Executa o jogo Jogador vs Jogador
    elif jogo == '2':
        JOGO=True
        jogo_versus() #Executa o jogo Jogador vs Computador
    elif jogo=='3':
        sys.exit() #Encerra o programa
    else:
        JOGO=False
    JOGO=False
