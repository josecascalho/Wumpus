import Config
from World import inside

# ==============================================================================================
# Modificar o E S T A D O  do  A G E N T E
def destroySpear():
    if Config.spears<1: return(False) 
    Config.spears-=1
    return(True)

def changeLifeEnergy(value):
    Config.lifeEnergy+=value
    if Config.lifeEnergy<0:
        Config.living=False
        return(False)
    return(True)

# !!!! necessita acesso para World porque usa aqui a função "inside"
def changePosAgent(coordinates):
    if inside(coordinates)==True:
        Config.posAgent=coordinates
        return(True)
    return(False)

def changeDirAgent(direction):
    if direction>=0 and direction<=3:
        Config.dirAgent=direction
        return(True)
    return(False)

# ==============================================================================================
# I N F O R M A Ç Ã O do Agente
def infoDir():
    if Config.dirAgent==0:return("^")
    if Config.dirAgent==1:return(">")
    if Config.dirAgent==2:return("v")
    if Config.dirAgent==3:return("<")
    return("Direção invalida")

def infoAgent():
    print("A Agent "+Config.nameAgent+" tem "+str(Config.lifeEnergy)+" Energia e "+str(Config.spears)+" lanças encontrando se no quadrado "+str(Config.posAgent)+" virado para "+infoDir()+".")
    

def initMap(x,y):
    Config.map=[]
    cell="???"
    for i in range(0,y):
        line=""
        for j in range(0,x-1):
            line=line+cell+":"
        line=line+cell
        Config.map.append(line)
        
def report(text):
    swap=Config.map[Config.posAgent[1]]
    line=""
    for k in range(0,4*Config.posAgent[0]):line=line+swap[k]
    line=line+text
    for k in range(4*Config.posAgent[0]+3,len(Config.map[0])):
        line=line+swap[k]
    Config.map[Config.posAgent[1]]=line    
    for i in range(0,len(Config.map)):
        print(Config.map[i])
    
#=======================================================================
# T E S T E do Módulo Agent
if __name__=="__main__": pass
# Teste da função "destroySpear"
#    for i in range(0,5):
#        print("Tinha "+str(Config.spears)+ " lanças antes do atiro")
#        print(str(destroySpear()))
#        print("Tem "+str(Config.spears)+ " lanças depois do atiro")
# Teste da função "changeLifeEnergy"
#    for i in range(0,5):
#        print("Tinha "+str(Config.lifeEnergy)+ " energias antes da ação")
#        print(str(changeLifeEnergy(-44)))
#        print("Tem "+str(Config.lifeEnergy)+ " depois da acção")
# Teste da função "changePosAgent"
#    for i in range(0,10):
#        print("Tinha a posição "+str(Config.posAgent)+ " antes da ação")
#        print(str(changePosAgent((Config.posAgent[0]+1,Config.posAgent[1]))))
#        print("Tem a posição "+str(Config.posAgent)+ " depois da acção")
# Teste da função "changeDirAgent"
#    for i in range(0,10):
#        print("Tinha a dir "+str(Config.dirAgent)+ " antes da ação")
#        if i<6: print(str(changeDirAgent((Config.dirAgent+1)%6)))
#        else:print(str(changeDirAgent((Config.dirAgent-1)%6)))
#        print("Tem a posição "+str(Config.dirAgent)+ " depois da acção")
# Teste da função "infoDir"
#    for i in range(0,10):
#        print("Tinha a dir "+str(infoDir())+ " antes da ação")
#        if i<6: print(str(changeDirAgent((Config.dirAgent+1)%6)))
#        else:print(str(changeDirAgent((Config.dirAgent-1)%6)))
#        print(str(infoDir())+ " depois da acção")
# Teste da função "infoAgent"
#    infoAgent()
# Teste da função "infoInit"
#    initMap(8,8)
# Teste da função "report"
#    initMap(8,8)
#    for i in range(0,10):
#        report("-F-")
#        print(i)
#        changePosAgent((Config.posAgent[0]+1,Config.posAgent[1]))
