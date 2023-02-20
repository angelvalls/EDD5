#Àngel Valls Segura Endevinar un número aleatori entre 1 i 100.
import random
#Inicializacio de part dels contadors
nsecret= random.randint(1,100)
cont_intents=0
intentnumero=1
premis=0
intents_de_acert=0
joc = True
cont_partides=0
intentsmax=0
intentsmin=0
#Inicializació del bucle while 
while joc: 

    n_max= 100
    n_min=1
    intentstotal= int(input("En quants intents creus que endevinaras el numero: "))
    cont_intents +=1
    cont_partides+=1
    #Comença el procés de trobar el número aleatori
    for intentnumero in range(1,intentstotal+1):
        num_intent= int(input("Dis-me el numero que creus que es, el secret es troba entre " + str( n_min ) +" i " + str ( n_max )+""))
        intents_de_acert+=1
        if nsecret==num_intent:
            print ("Molt bé has encertat el numero que era el ", nsecret," en ", intents_de_acert, " intents")
            print ("Premi")
            premis+=1
            break
        elif num_intent<nsecret:
            n_min=num_intent
            print ("El numero es menor,es troba entre",(n_min),"i",(n_max))
        elif num_intent>nsecret:
            n_max=num_intent
            print  ("El numero es major,es troba entre",(n_min),"i",(n_max))
        elif intentnumero ==intentstotal:
            print("No ho has encertat en els intents que has introduït el numero secret era el: ",nsecret)
            break
    #Fem comprobacions de quin es el número més gran de intents que hem fet 
    intentsmax= cont_intents
    intentsmin=cont_intents
    if intentsmax>intentsmax:
        intentsmax=intentsmax
    elif intentsmin<intentsmin:
        intentsmin=intentsmin

    #Preguntem si volen tornar a jugar 
    tornarjuar=input("Vols tornar a jugar s/S o n/N ")

    if tornarjuar == "S" or tornarjuar == "s":
        joc == True
    elif tornarjuar=="n" or tornarjuar=="N":
        joc == False
        break  
    
    #Eixida de dades finals com a cantitat de partides jugades, premis obtinguts, intents màxims i mínims i per últim la mitja de intents. 
print ("Has jugat estes partides: ", cont_partides)
print ("Premi"*premis)
print ("La mitja de intents ha segut de: ", cont_intents/cont_partides )
print ("La partida guanyada amb més intents ha segut de", intentsmax )
print ("La partida guanyada amb menys intents ha segut de", intentsmin )