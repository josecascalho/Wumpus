# World
row=8                            # Número das linhas no plano
column=8                         # Número das coluna no plano
monster=[(3,3)]                  # A posição do(s) monstro(s) esta indicado pelo um tuplo da coordenada (x,y)
holes=[(1,1),(2,2),(5,3)]         # A posição do(s) buraco(s) esta indicado pelo um tuplo da coordenada (x,y)
gold=[(1,2),(2,1),(5,5)]         # A posição do(s) pedaço(o) de oiro esta indicado pelo um tuplo da coordenada (x,y)

# Interaction
valueGold=1000
costRotating=1
costGrabbing=1
costThrowSpear=2
costGoing=2
costFalling=500
costFight=2000

# Agent
nameAgent="Spider"
lifeEnergy=100       # Começa o jogo com 100 pontos de Energia
posAgent=(0,0)       # Começa o jogo na posição (x,y)=(0,0)
dirAgent=1           # Começa o jogo direcionada para esquerda
spears=2             # Começa o jogo com 2 lanças
living=True          # O jogador vive e tenta se manter vivend o
map=[]               # A função "initMap" vai preencher este mapa com cellulas de "???"
