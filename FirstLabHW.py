f = open("aaavvv.txt",'r')
valid = 0
Sigma = []
x= f.readline()
x= f.readline().rstrip()
while x != "End":
    litera = [x[i] for i in range(4,len(x))]
    litera= ''.join(litera)
    Sigma += litera
    x = f.readline()
    x = x.rstrip()

y= f.readline()
States = []
y= f.readline().rstrip()

while y != "End":
    stare = [y[i] for i in range(4,len(y)) if y[i]!=' ']
    stare = ''.join(stare)
    if ',' in stare:
        stare = stare.split(',')
        if stare[1] == 'F':
            F = stare[0]
            if len(stare) == 3:
                S = stare[0]
        else:
            S = stare[0]
            if len(stare) == 3:
                F = stare[0]    
        States.append(stare[0])
        y = f.readline().rstrip()
        continue
    States.append(stare)
    y = f.readline().rstrip()

z=f.readline()
Transitions = {}
z=f.readline().rstrip()

while z!='End':
    trans = [z[i] for i in range(4,len(z))]
    trans = ''.join(trans)
    trans = trans.split(',')
    if trans[0] not in States or trans[2] not in States:
        print('nasol')
        valid = 1
        break
    if trans[1] not in Sigma:
        print('nasol')
        valid = 1
        break
    if trans[0] not in Transitions:
        Transitions.update({trans[0]:{trans[1]:[trans[2]]}})
    else:
        if trans[1] not in Transitions[trans[0]]:
            Transitions[trans[0]].update({trans[1]:[trans[2]]})
        else:
            Transitions[trans[0]][trans[1]] += [trans[2]]
            if len(Transitions[trans[0]][trans[1]]) == 2:
                valid = 1  
    z = f.readline().rstrip()

if valid == 1:
    print("Automatul dat nu este un Automat Finit Determinat")
else:
    print("Automatul dat este un Automat Finit Determinat")           
    print(Sigma)
    print(States)
    print(Transitions)
    print(F)
    print(S)
    
    
Cuvant = input("Introduceti cuvantul pentru validare: ")

stare_curenta = Transitions[S][Cuvant[0]][0]

for i in range(1,len(Cuvant)):
    stare_viitoare = Transitions[stare_curenta][Cuvant[i]][0]
    stare_curenta = stare_viitoare

if stare_curenta == F:
    print("Es bueno, muchas gracias senor")
else:
    print("No es bueno")