import Config
from World import *
from Agent import changeLifeEnergy,changeDirAgent,destroySpear,initMap,infoAgent,report
from Sensor import *


# A C Ç Õ E S:
#================================================================================================================

def rotating(clockwise):
    changeLifeEnergy(-Config.costRotating)                            # Consumo de energia em rodar
    print(changeDirAgent(rotate(clockwise,Config.dirAgent)))          # Defina a nova direção após da rotação 
    print("rotating"+str(Config.dirAgent)+" "+str(Config.lifeEnergy))
def grabGold():
    changeLifeEnergy(-Config.costGrabbing)
    if takeGold(Config.posAgent)==True:
        changeLifeEnergy(Config.valueGold)            # Transforma o valor da oiro em energia da vida do jogador
        return(True)
    return(False)

def throwSpear():
    changeLifeEnergy(-Config.costThrowSpear)          # Lançar a lança custa energia independemente se houver lança
    if Config.spears<1: return(False)                 # Se hão houver uma lança não há mais implicações
    destroySpear()                                    # Já se pode destruir a lança em antecipação
    newCord=neighbour(Config.posAgent,Config.dirAgent)
    while inside(newCord):
        if killMonster(newCord)==True:                # Vamos tentar matar o monstro no sitio da lança, no caso de sucesso:
            return(True)                              # Saimos reclamando o sucesso
        newCord=neighbour(newCord,Config.dirAgent)    # Tendo nenhum sucesso verificamos se tiver no proximo quadrado
    return(False)                                     # A lança já ultrapassou o plano, assim não tivemos sucesso


def going():
    changeLifeEnergy(-Config.costGoing)                            # Consumo de energia em andar para frente
    pos=neighbour(Config.posAgent,Config.dirAgent)                 # Calcula a nova posição virtual
    if inside(pos)==True:                                          # Verifique se a posição virtual pode ser real
        Config.posAgent=pos                                        # Caso sim: 1. constui como nova posição do jogador
        if haveHole(pos):changeLifeEnergy(-Config.costFalling)     #           2. calcule os danos pela possivel
                                                                   #              presênça de um buraco
        if haveMonster(pos):                                       #           3. calcule os danos pela possivel
            changeLifeEnergy(-Config.costFight)                    #              presênça de um monstro
            if Config.living==True:killMonster(pos)                #              e mata o monstro se subviveu                                                       
        return(True)                                               #           3. Retorna que o passo teve sucesso
    return(False)                                                  # Caso não: Reporta o fracasso no andamento

def menu():

    initMap(Config.column,Config.row)
    while Config.living==True:
        infoAgent()
        print("Escolhe uma das seguintes letras para determinar a sua opções de agir:")
        print("   a --> Rota 90 grau em sentido do relógio [custo 1]")
        print("   b --> Rota 90 grau em sentido contrário do relógio [custo 1]")
        print("   c --> Tentar em pegar num pedaço de oiro [custo 1]")
        print("   d --> Lançar a lança para frente [custos 2]")
        print("   e --> Avança [custos 2]")
        print("   x --> Finalizar o jogo")
        report(textSensor(sensorData(Config.posAgent)))
        interact=input()
        if interact=="a":rotating(True)
        elif interact=="b":rotating(False)
        elif interact=="c":grabGold()
        elif interact=="d":throwSpear()
        elif interact=="e":going()
        elif interact=="x":break
        else:print("A letra "+interact+" não foi uma escolha válida. Por favor, escolhe mais uma vez!")


# lifeEnergy
# posAgent
# dirAgent
# spears
# living
        
if __name__=="__main__":
#    global lifeEnergy,dirAgent
# T E S T E do Módulo Interactions
# Teste da função "rotating"
#    for i in range(0,10):
#        print("Antes da rotação: i) Energia:"+str(Config.lifeEnergy)+" ii) Direção:"+str(Config.dirAgent))
#        if i<5:rotating(True)
#        else: rotating(False)
#        print("Depois da rotação: i) Energia:"+str(Config.lifeEnergy)+" ii) Direção:"+str(Config.dirAgent))
# Teste da função "grabGold"
#    for i in range(0,Config.row):
#        for j in range(0,Config.column):
#            Config.posAgent=(j,i)            
#            if grabGold(): print("Tirou oiro em:"+str((j,i))+"Há ainda? "+str(haveGold((j,i))))
# Teste da
# função "throwSpear"
#    Config.monster.append((3,2))
#    Config.spears=100
#    for i in range(0,Config.row):
#        for j in range(0,Config.column):
#            Config.posAgent=(j,i)            
#            if throwSpear(): print("Matou monstro em:"+str((j,i))+"Há ainda? "+str(haveMonster((j,i))))
    
# Teste da função "going"
#    Config.monster.append((3,2))
#    for i in range(0,Config.row):
#        for j in range(0,Config.column):
#            Config.posAgent=(j,i)            
#            if going(): print("Em "+str(Config.posAgent)+"tem energia de "+str(Config.lifeEnergy))
#            else: print("Batou na porta em "+str(Config.posAgent))
# Teste da função "menue"
    menu()

