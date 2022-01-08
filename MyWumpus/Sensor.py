import Config
from World import haveGold,haveMonster,haveHole,neighbour,inside

# ===================================================================================
# C O N C E I T O  do S E N S O R
# --> Representação: Como a presesença dos items oiro/monstro/buraco é sentido de acordo
#                    como informações sensoriais brilho/cheiro/vento resumimos este informação
#                    num tuple (Brilho?,Cheiro?,Vento?) onde cada componente responde se senta a presença ou não

def sensorData(coordenates):
    B=False                           # Inicialização do data=(Brilho?,Cheiro?,Vento?)=(False,False,False)
    C=False
    V=False          
    if inside(coordenates)==True:     # Só tem uma resposta viável se as coordenadas pertencem ao plano
                                      # Neste caso temos as seguintes alterações:
        B=haveGold(coordenates)       # 1) Há Brilho se há oiro no sitio das coordenadas
        for i in range(0,4):          # 2) Há Cheiro/Vento se há um Monstro/Buraco num dos (no max) 4 vizinhos
            pos=neighbour(coordenates,i)         # a) Determino o vizinho em direcao do valor i in {0,..,3}
            if inside(pos)==True:                # b) Caso que o vizinho faz parte do plano
                if haveMonster(pos)==True:C=True #    i) Há Cheiro se o vizinho contem um monstro
                if haveHole(pos)==True:V=True    #   ii) Há Vento se o vizinho contem um buraco
    return((B,C,V))                      # Retorno os dados sensoriais recolhidos

# Representação dos dados sensoriais para uma triplex de letras: "---","B--","-C-","--V","BC-","B-V","-CV" ou "BCV"
def textSensor(data):
    if data[0]==True:B="B"        # Caso se sento um "Brilho" usa a letra "B"
    else:B="-"                    #      senão usa "-"
    if data[1]==True:C="C"        # Caso se sento um "Cheiro" usa a letra "C"
    else:C="-"                    #      senão usa "-"
    if data[2]==True:V="V"        # Caso se sento um "Vento" usa a letra "V"
    else:V="-"                    #      senão usa "-"
    return(B+C+V)                 # Retorna o resultado textual dos dados sensoriais


# T E S T E do Módulo Sensor
if __name__=="__main__":
    plan=[]
    for i in range(0,Config.row):
        line=""
        for j in range(0,Config.column-1):
            line=line+textSensor(sensorData((i,j)))+":"
        line=line+textSensor(sensorData((i,Config.column-1)))
        plan.append(line)
    for i in range(0,len(plan)):print(plan[i])