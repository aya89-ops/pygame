import pandas as pd
data = pd.read_csv("pygame.stats.csv")
mylist= data['connections']
j=0
k=0
points=0
jours_gratuits = 0
nb_jours=30
for i in mylist:
    if(i==1):
        j+=1
    if (j==5) :
        print( 'vous avez gangné 10 points ')
        points+=10
if(points==15):
    nb_jours-=1.5








