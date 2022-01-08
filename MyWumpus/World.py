import Config
# ===================================================================================
# C O N C E I T O  da existencia de um item numa coordenada
# --> Representação:
#    a) Uma representação extensa
#        holes=[False,False,False,False,False,False,False,False,
#               False,True,False,False,False,False,False,False,
#               False,False,True,False,False,False,False,False,
#               False,False,False,False,False,False,False,False,
#               False,False,False,False,False,False,False,False,
#               False,False,False,True,False,False,False,False,
#               False,False,False,False,False,False,False,False,
#               False,False,False,False,False,False,False,False]
#    b)  A representação resumida
#       monster=[(1,1),(2,2),(5,3)]
# --> Pesquisa sobre a existência de um buraco na posição (3,4)
#    a) Na representação extensa há uma resposta imediata:
#               return(holes[3][4]
#    b) Na representação resumida temos verificar para todas entradas
#       se forem identicas com as coordenadas procuradas:       
#               for i in range(0,len(holes)):
#                  if coordenates[0]==holes[i][0] and coordenates[1]==holes[i][1]:
#                      return(True)
#               return(False)

# Resposta sobre se os items (buraco/monstro/oiro) se encontram num determinado sitio
def haveHole(coordenates):
        for i in range(0,len(Config.holes)):
           if coordenates[0]==Config.holes[i][0] and coordenates[1]==Config.holes[i][1]:
                return(True)
        return(False)
def haveMonster(coordenates):
        for i in range(0,len(Config.monster)):
           if coordenates[0]==Config.monster[i][0] and coordenates[1]==Config.monster[i][1]:
                return(True)
        return(False)
def haveGold(coordenates):
        for i in range(0,len(Config.gold)):
           if coordenates[0]==Config.gold[i][0] and coordenates[1]==Config.gold[i][1]:
                return(True)
        return(False)

# ===================================================================================
# C O N C E I T O  da  D I R E Ç Ã O:
#      -->  Representação: 0=cima    1=esquerda    2=baixo     3=esquerda 
#      -->  Mudança de 90 grau em direção relogio: 0 -> 1 -> 2 -> 3 -> 0
#                                                  novaDireção=(velhaDireção+1)%4
#      -->  Mudança de 90 grau em direção relogio: 0 -> 3 -> 2 -> 1 -> 0
#                                                  novaDiração=(velhaDireção+3)%4

# -------------------------------------------------------------------------------------------------------
# FUNÇÃO: "rotate" --> Calcula a partir da actual direção "direction" e da desejada orientação "clockwise"
#                      a nova direção após da rotação em 90 grau
# ENTRADA: clockwise --> Valor do típo boolean: True=orientação de relógio / False=orientação contrário
#          direction --> Valor do típo inteiro entre 0 e 3 (cima/esqueirda/baixa/direita) da direção atual
# SAÍDA:             --> Valor do típo inteiro entre 0 e 3 da nova direção após da rotação desejada 
# EFEITOS SEGUNDÁRIOS: ---
# COMMENTÁRIO: necessita se este função quer para a execução da acção rotaçao quer para o planeamento da mesma
def rotate(clockwise,direction):
        if clockwise==True:
            return((direction+1)%4)
        else:
            return((direction+3)%4)

# ===================================================================================
# C O N C E I T O  da  V I Z I N H A Ç A adjacente:
#                           (x,y-1)
#                              ^
#                    direção=0 | vizinho em cima
#                              |
#                          ---------
#          vizinho direito |       | vizinho esquerdo
# (x-1,y) <--------------- | (x,y) | ----------------> (x+1,y)
#             direção=3    |       |    direção=1
#                          ---------
#                              |
#                    direção=1 | vizinho em baixo
#                              v
#                           (x,y+1)
def neighbour(coordenates,direction):
        if (direction%2)==0:                          # Direção par ou é para cima ou para baixo
            dx=0                                      # --> não há mudanças na direção x
            dy=1                                      # --> há mudanças de uma a unidade para direção y
        else:                                         # Direção pares são ou para esquerda ou direita
            dx=1                                      # --> há mudanças de uma a unidade na direção x
            dy=0                                      # --> não há mudanças na direção y
        if direction==3: dx=-1                        # para direita a unidade de mudânca é negativa
        if direction==0: dy=-1                        # para cima a unidade de mudânca é negativa
        return((coordenates[0]+dx,coordenates[1]+dy)) # Retorna a Posição nova

# Uma coordenada de um vizinho se pode encontrar fora do plano daí a necessidade de verificcção seguinte:
def inside(coordenates):
        if coordenates[0]<0 or coordenates[1]<0:return(False)        # Esta fora ou de cima ou a direita?
        if coordenates[0]<Config.column and coordenates[1]<Config.row:return(True) # Esta dentro tanto na esquerda tanto em baixo?
        return(False)                                                # Fora ou da esquerda ou da baixa!
    
# ========================================================================================================
# Modificar o E S T A D O  do  M U N D O
def killMonster(coordenates):
        if haveMonster(coordenates)==True:
                Config.monster.remove(coordenates)
                return(True)
        return(False)

def takeGold(coordenates):
        if haveGold(coordenates)==True:
            Config.gold.remove(coordenates)
            return(True)
        return(False)
    
# T E S T E do Módul World
if __name__=="__main__": pass
# Test função "haveHole"
#    for i in range(0,Config.row):
#        for j in range(0,Config.column):
#           if haveHole((j,i)):print("Hole in "+str((j,i)))
# Test função "haveMonster"
#    for i in range(0,Config.row):
#        for j in range(0,Config.column):
#           if haveMonster((j,i)):print("Monster in "+str((j,i)))
# Test função "haveGold"
#    for i in range(0,Config.row):
#        for j in range(0,Config.column):
#           if haveGold((j,i)):print("Gold in "+str((j,i)))
# Test função "rotate"
#    for i in range(0,4):
#        print("Rotate em direção relogio:"+str(i)+" --> "+str(rotate(True,i)))
#        print("Rotate em direção contra-relogio:"+str(i)+" --> "+str(rotate(False,i)))
# Test função "neighbour"
#    for i in range(0,4):
#        print("(3,7) tem vizinho"+str(neighbour((3,7),i))+" in direção:"+str(i))
# Test função "inside"
#    for i in range(0,4):
#        print("(3,7) tem vizinho ("+str(inside(neighbour((3,7),i)))+") "+str(neighbour((3,7),i))+" in direção:"+str(i))
# Test função "killMonster"
#    for i in range(0,Config.row):
#        for j in range(0,Config.column):
#           if killMonster((j,i)):print("Foi matado um monstro em "+str((j,i)))
#    for i in range(0,Config.row):           # segunda passagem para ver se realmente desapareceu
#        for j in range(0,Config.column):
#           if killMonster((j,i)):print("Foi matado um monstro em "+str((j,i)))
# Test função "takeGold"
#    for i in range(0,Config.row):
#        for j in range(0,Config.column):
#           if takeGold((j,i)):print("Foi tirado o oiro em "+str((j,i)))
#    for i in range(0,Config.row):           # segunda passagem para ver se realmente desapareceu
#        for j in range(0,Config.column):
#           if takeGold((j,i)):print("Foi tirado o oiro em "+str((j,i)))




