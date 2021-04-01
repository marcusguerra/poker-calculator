#Spades = Espada // Hearts = Copas // Diamonds = Ouro // Clubs = paus
#Ace = Ás // Queen = Damas // Jack = Valetes // King = Reis
#s = mesmo naipe // o = naipes diferentes // n.a = indiferente
#ideia pardão de carta = sK = rei de espada
#posições = early / mid / late




def print_tier(tier):
    if tier == 1:
        print("You have a tier 1 opening hand, you should raise")
    elif tier == 2:
        print("You have a tier 2 opening hand, you should consider raising")
    elif tier == 3:
        print("You have a tier 3 opening hand, you should tip in")
    elif tier == 4:
        print("You have a tier 4 opening hand, think before play")
    elif tier == 5:
        print("You have a tier 5 opening hand, watch out")
        print("TIP for tier 5:")
        print("In early positions only play this, if the game is passive")
    elif tier == 6:
        print("You have a tier 6 opening hand, you should probably fold")
        print("TIP for tier 6:")
        print("Only play this tier in mid positions, if the game is passive, and dont play it early")
    elif tier == 7:
        print("You have a tier 7 opening hand, you should probably fold")
        print("TIP for tier 7:")
        print("This opening is only playable in a late position and if the game is passive")
    else:
        print("You have a tier 8 opening hand, you should fold")
    print("--------------------------------------------------------------------------------")
#tranforma os valores das cartas em valores númericos
def atribui_valorc1(carta1):
    # tranforma as cartas em valores inteirtos
    cartas = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A", "0"]
    # botando a carta1 como a de maior valor para facilitar minha vida

    valor1 = cartas.index(carta1[1]) + 2
    return valor1

#cria um vetor com os valores inteiros das cartas(v) e outro com as cartas(c) para ser usado posteriormente
def cria_vetor (carta1, carta2,carta3,carta4,carta5,carta6,carta7):
    v = []
    c = []
    c.append(carta1)
    c.append(carta2)
    c.append(carta3)
    c.append(carta4)
    c.append(carta5)
    c.append(carta6)
    c.append(carta7)
    valor1 = atribui_valorc1(carta1)
    valor2 = atribui_valorc1(carta2)
    valor3 = atribui_valorc1(carta3)
    valor4 = atribui_valorc1(carta4)
    valor5 = atribui_valorc1(carta5)
    valor6 = atribui_valorc1(carta6)
    valor7 = atribui_valorc1(carta7)
    v.append(valor1)
    v.append(valor2)
    v.append(valor3)
    v.append(valor4)
    v.append(valor5)
    v.append(valor6)
    v.append(valor7)
    return (v, c)
def opening_hand(carta1, carta2):
    #iniciando a variavel tier
    tier1 = 9
    # botando a carta1 como a de maior valor para facilitar minha vida
    valor1 = atribui_valorc1(carta1)
    valor2 = atribui_valorc1(carta2)
    if valor2 > valor1:
        valor3 = valor2
        valor2 = valor1
        valor1 = valor3
    # mostrando as aberturas com pares
    if valor1 == valor2:
        if 14 >= valor1 >= 11:
            tier1 = 1
        else:
            # loop para resumir o resto dos pares
            i = 2
            k = 10
            while (i >= 2):
                if valor1 == k or k <= 4:
                    tier1 = i
                    break
                elif k == 6:
                    k -= 1
                else:
                    i += 1
                    k -= 1
    # aberturas de naipes iguais
    elif carta1[0] == carta2[0]:
        # aberturas com Ás
        if valor1 == 14:
            if valor2 == 13:
                tier1 = 1
            elif 12 >= valor2 >= 11:
                tier1 = 2
            elif valor2 == 10:
                tier1 = 3
            else:
                tier1 = 5
        # aberturas com Rei
        elif valor1 == 13:
            # loop para resumir os reis de mesmo naipe
            i = 2
            k = 12
            while (i >= 2):
                if valor2 == k or k <= 8:
                    tier1 = i
                    break
                elif i == 4:
                    i += 2
                    k -= 1
                else:
                    i += 1
                    k -= 1
        #aberturas com rainha
        elif valor1 == 12:
            i = 3
            k = 11
            while (i >= 3):
                if valor2 == k:
                    tier1 = i
                    if  i == 6:
                        tier1 = i+1
                        break
                    break
                else:
                    i+=1
                    k-=1
        #aberturas com valete
        elif valor1 == 11:
            if valor2 == 10:
                tier1 = 3
            elif valor2 == 9:
                tier1 = 4
            elif valor2 == 8:
                tier1 = 6
        #aberturas com 10
        elif valor1 == 10:
            if valor2 == 9:
                tier1 = 4
            elif valor2 == 8:
                tier1 = 5
            elif valor2 == 7:
                tier1 = 7
        #aberturas com 9
        elif valor1 == 9:
            if valor2 == 8:
                tier1 = 4
            elif valor2 == 7:
                tier1 = 5
        # aberturas com 8
        elif valor1 == 8:
            if valor2 == 7:
                tier1 = 5
            elif valor2 == 6:
                tier1 = 6
        #aberturas com 7
        elif valor1 == 7:
            if valor2 == 6:
                tier1 = 5
            elif valor2 == 5:
                tier1 == 6
        # aberturas com 5 ou 4
        elif valor1 == 5 or valor1 == 4:
            if valor2 == 4:
                tier1 = 6
            elif valor2 == 3:
                tier1 = 7

        else:
            tier1 = 8
    elif carta1[0] != carta2 [0]:
        if valor1 == 14:
            i = 2
            k = 13
            while(i >= 2):
                if valor2 == k:
                    if i == 5:
                        tier1 = 6
                        break
                    tier1 = i
                    break
                else:
                    i += 1
                    k -= 1
        elif valor1 == 13:
            if valor2 == 12:
                tier1 = 4
            elif valor2 == 11:
                tier1 = 5
            elif valor2 == 10:
                tier1 = 6
        elif valor1 == 12:
            if valor2 == 11:
                tier1 = 5
            elif valor2 == 10:
                tier1 = 6
        elif valor1 == 11:
            if valor2 == 10:
                tier1 = 5
            elif valor2 == 9:
                tier1 = 7
        elif valor1 == 10 or valor1 == 9:
            if valor2 == 9 or valor2 == 8:
                tier1 = 7
    else:
        tier1 = 8
    print_tier(tier1)
#verifica o que o jogador tem de combinações
def player_hand_flop(carta1, carta2,carta3,carta4,carta5,carta6,carta7):
    valor6 = atribui_valorc1(carta6)
    valor7 = atribui_valorc1(carta7)

    carta1_n_pares = 1
    carta2_n_pares = 1
    straight = 0
    carta1_n_suited = 0
    carta2_n_suited = 0
    #v é o vetor com os valores inteiros das cartas
    v = []
    #c é o vetor com as cartas
    c = []
    v, c = cria_vetor(carta1, carta2, carta3, carta4, carta5, carta6, carta7)
    if v[0] == v[1]:
        carta1_n_pares += 1
    if carta1[0] == carta2[0]:
        carta1_n_suited += 1
    #conta o numero de pares que o jogador tem
    for i in range(2, 6):
        if v[0] != v[1]:
            if v[0] == v[i]:
                carta1_n_pares += 1
            if v[1] == v[i]:
                carta2_n_pares += 1
        else:
            if v[0] == v[i]:
                carta1_n_pares += 1
    v.sort()
    v.append(0)
    #verifica se o jogador tem um straight
    i = 0
    for i in range (6):
        if v[i] + 1 == v[i+1]:
            straight += 1
        elif carta6 == "00" and carta7 == "00":
            if i+1 == 5:
                break
        elif carta6 == "00" and carta7 != "00":
            if i+1 == 6:
                break
        elif carta6 != "00" and carta7 != "00":
            if i+1 == 7:
                break
    if straight >= 4:
        straight = 1
    else:
        straight = 0
    #verifica se o jogador tem um flush
    for i in range(1, 6):
        if c[0][0] == c[i][0]:
            carta1_n_suited += 1
        elif c[1][0] == c[i][0]:
            carta2_n_suited += 1
        elif c[0][0] == c[1][0]:
            if c[0][0] == c[i][0]:
                carta1_n_suited += 1
    return (carta1_n_pares,carta2_n_pares,carta1_n_suited,carta2_n_suited,straight)


#calcula a probabilidade do jogador fazer uma sequencia
def sequencia(carta1, carta2,carta3,carta4,carta5,carta6,carta7):
    gaps1 = 0
    k = 0
    #cria um vetor com os valores inteiros para organizar
    v = []
    c = []
    v, c = cria_vetor(carta1, carta2,carta3,carta4,carta5,carta6,carta7)
    v.sort()
    v.append(0)
    #ciclo for verificando se existe a possibilidade de uma sequencia
    for i in range(6):
        if gaps1 >= 2:
            if v[i] + 1 == v[i+1]:
                gaps1 += 1
            elif v[i] +2 == v[i+1]:
                k += 1
            break
        elif v[i+1] == v[i]:
            continue
        elif v[i] + 1 == v[i+1]:
            gaps1 += 1
        elif v[i] +2 != v[i+1]:
            gaps1 = 0
        else:
            k += 1
    #se gaps1 = 3 quer dizer que o jogador precisa de 1 carta em qualquer extremidade do ponto para fazer um straight
    #se gaps1 = 2 e k = 1 quer dizer que falta uma carta no meio para o jogador fazer um straight
    if gaps1 == 3:
        return 8
    elif gaps1 == 2 and k == 1:
        return 4
    elif gaps1 == 2 and k ==0:
        return 1
    else:
        return 0

#Spades = Espada // Hearts = Copas // Diamonds = Ouro // Clubs = paus
#calcula a probabilidade do jogador fazer um flush
def flush(carta1, carta2,carta3,carta4,carta5,carta6,carta7):
    Spades = 0
    Hearts = 0
    Diamonds = 0
    Clubs = 0
    v= []
    #botando as cartas todas em um vetor para poder fazer os Ifs com mais praticidade
    c = []
    v, c = cria_vetor(carta1, carta2,carta3,carta4,carta5,carta6,carta7)
    for i in range(6):
        if c[i][0] == "S":
            Spades += 1
        elif c[i][0] == "H":
            Hearts += 1
        elif c[i][0] == "D":
            Diamonds += 1
        elif c[i][0] == "C":
            Clubs += 1
    if Spades == 4 or Clubs == 4 or Hearts == 4 or Diamonds == 4:
        return 9
    elif Spades == 3 or Clubs == 3 or Hearts == 3 or Diamonds == 3:
        return 1
    else:
        return 0

def flop(carta1, carta2,carta3,carta4,carta5):
    # avaliar a situação da mesa, dizendo que combo o jogador tem, as outs possiveis, e a chance dele ganhar
    carta6 = "00"
    carta7 = "00"
    royal_flush = 0
    carta1_n_pares,carta2_n_pares,carta1_n_suited,carta2_n_suited,straight = player_hand_flop(carta1, carta2,carta3,carta4,carta5,carta6,carta7)
    flush_outs  = flush(carta1, carta2,carta3,carta4,carta5,carta6,carta7)
    sequencia_outs = sequencia(carta1, carta2,carta3,carta4,carta5,carta6,carta7)
    #diz as probabilidades de outs do jogador
    if carta1_n_suited < 5:
        if flush_outs == 9:
            print("You have a 37% chance to make a flush", end= "")
        elif flush_outs == 1:
            print("You have a 3% chance to make a flush", end= "")
        elif flush_outs == 0:
            print("You have a 0% chance to make a flush", end= "")
        if straight == 1:
            print("")
    if straight != 1:
        if carta1_n_suited >= 5:
            print("You have", end= "")
        else:
            print(" and", end= "")
        if sequencia_outs == 8:
            print(" a 34% chance to make a straight")
        elif sequencia_outs == 4:
            print(" a 18% chance to make a straight")
        elif sequencia_outs == 1:
            print(" a 4% chance to make a straight")
        elif sequencia_outs == 0:
            print(" a 0% chance to make a straight")
    #diz as combinações
    print("Your combinations are:")
    if carta1[1] != carta2[1]:
        if carta1_n_pares >= 2:
            print(carta1_n_pares,"of a kind of", carta1[1])
        if carta2_n_pares >= 2 and carta1_n_pares >= 2:
            print(carta2_n_pares, "of a kind of", carta2[1])
        elif carta2_n_pares >= 2:
            print(carta2_n_pares, "of a kind of", carta2[1])
    elif carta1[1] == carta2[1]:
        if carta1_n_pares >= 2:
            print(carta1_n_pares,"of a kind of", carta1[1])
    if carta1_n_suited >= 5:
        print("flush of", carta1[0])
    if straight == 1:
        print("straight")
    if straight == 1 and carta1_n_suited >= 5 and (carta1[1] == "A" or carta2[1] == "A"or carta3[1] == "A"or carta4[1] == "A"or carta5[1] == "A"):
        royal_flush = 1
        print("***ROYAL FLUSH***")
    if royal_flush == 1:
        print("You win, nothing can beat you")
    elif straight == 1 and carta1_n_suited >= 5:
        print("With your hand, only a royal flush can beat you")
    elif carta1_n_pares == 4 or carta2_n_pares == 4:
        print("With your hand, a straight flush and above can beat you")
    elif carta1_n_suited == 5:
        print("With your hand,a full house and above can beat you")
    elif straight == 1:
        print("With your hand,a flush and above can beat you")
    elif carta1_n_pares == 3 or carta2_n_pares == 3:
        print("With your hand,a straight and above can beat you")
    elif carta1_n_pares == 2 and carta2_n_pares == 2:
        print("With your hand,a three of a kind and above can beat you")
    elif carta1_n_pares == 2 or carta2_n_pares == 2:
        if carta1_n_pares == 2:
            print("With your hand,a pair higher than", carta1[1],"and above can beat you")
        else:
            print("With your hand,a pair higher than", carta2[1], "and above can beat you")
    else:
        print("anything can beat you")
    print("--------------------------------------------------------------------------------")
def turn(carta1, carta2,carta3,carta4,carta5,carta6):
    carta7 = "00"
    royal_flush = 0
    v = []
    c = []
    v, c= cria_vetor(carta1, carta2,carta3,carta4,carta5,carta6, carta7)
    flush_outs = flush (carta1, carta2, carta3, carta4, carta5, carta6, carta7)
    sequencia_outs = sequencia(carta1, carta2, carta3, carta4, carta5, carta6, carta7)
    carta1_n_pares, carta2_n_pares, carta1_n_suited, carta2_n_suited, straight =player_hand_flop(carta1, carta2,carta3,carta4,carta5,carta6,carta7)
    if carta1_n_suited < 5 and carta2_n_suited < 5:
        if flush_outs == 9:
            print("You have a 17% chance to make a flush", end="")
        elif flush_outs == 1:
            print("You have a 1.5% chance to make a flush", end="")
        elif flush_outs == 0:
            print("You have a 0% chance to make a flush", end="")
        if straight == 1:
            print("")
    if straight != 1:
        if carta1_n_suited >= 5 or carta2_n_suited >=5:
            print("You have", end="")
        else:
            print(" and", end="")
        if sequencia_outs == 8:
            print(" a 18% chance to make a straight")
        elif sequencia_outs == 4:
            print(" a 9% chance to make a straight")
        elif sequencia_outs == 1:
            print(" a 2% chance to make a straight")
        elif sequencia_outs == 0:
            print(" a 0% chance to make a straight")
    print("Your combinations are:")
    if carta1[1] != carta2[1]:
        if carta1_n_pares >= 2:
            print(carta1_n_pares, "of a kind of", carta1[1])
        if carta2_n_pares >= 2 and carta1_n_pares >= 2:
            print(carta2_n_pares, "of a kind of", carta2[1])
        elif carta2_n_pares >= 2:
            print(carta2_n_pares, "of a kind of", carta2[1])
    elif carta1[1] == carta2[1]:
        if carta1_n_pares >= 2:
            print(carta1_n_pares, "of a kind of", carta1[1])
    if carta1_n_suited >= 5 or carta2_n_suited >=5:
        if carta1_n_pares >=5:
            print("flush of", carta1[0])
        else:
            print("flush of", carta2[0])
    if straight == 1:
        print("straight")
    if straight == 1 and (carta1_n_suited >= 5 or carta2_n_suited >= 5):
        if (v[0] == 10 and v[4] == 14) or (v[1] == 10 and v[5] == 14):
            royal_flush = 1
            print("***ROYAL FLUSH***")
    if royal_flush == 1:
        print("You win, nothing can beat you")
    elif straight == 1 and (carta1_n_suited >= 5 or carta2_n_suited >= 5):
        print("With your hand, only a royal flush can beat you")
    elif carta1_n_pares == 4 or carta2_n_pares == 4:
        print("With your hand, a straight flush and above can beat you")
    elif carta1_n_suited == 5 or carta2_n_suited >=5:
        print("With your hand,a full house and above can beat you")
    elif straight == 1:
        print("With your hand,a flush and above can beat you")
    elif carta1_n_pares == 3 or carta2_n_pares == 3:
        print("With your hand,a straight and above can beat you")
    elif carta1_n_pares == 2 and carta2_n_pares == 2:
        print("With your hand,a three of a kind and above can beat you")
    elif carta1_n_pares == 2 or carta2_n_pares == 2:
        if carta1_n_pares == 2:
            print("With your hand,a pair higher than", carta1[1], "and above can beat you")
        else:
            print("With your hand,a pair higher than", carta2[1], "and above can beat you")
    else:
        print("anything can beat you")
    print("--------------------------------------------------------------------------------")
def river(carta1, carta2,carta3,carta4,carta5,carta6,carta7):
    royal_flush = 0
    v = []
    c = []
    v, c = cria_vetor(carta1, carta2, carta3, carta4, carta5, carta6, carta7)
    flush_outs = flush(carta1, carta2, carta3, carta4, carta5, carta6, carta7)
    sequencia_outs = sequencia(carta1, carta2, carta3, carta4, carta5, carta6, carta7)
    carta1_n_pares, carta2_n_pares, carta1_n_suited, carta2_n_suited, straight = player_hand_flop(carta1, carta2,carta3,carta4,carta5,carta6,carta7)


    print("Your combinations are:")
    if carta1[1] != carta2[1]:
        if carta1_n_pares >= 2:
            print(carta1_n_pares, "of a kind of", carta1[1])
        if carta2_n_pares >= 2 and carta1_n_pares >= 2:
            print(carta2_n_pares, "of a kind of", carta2[1])
        elif carta2_n_pares >= 2:
            print(carta2_n_pares, "of a kind of", carta2[1])
    elif carta1[1] == carta2[1]:
        if carta1_n_pares >= 2:
            print(carta1_n_pares, "of a kind of", carta1[1])
    if carta1_n_suited >= 5 or carta2_n_suited >= 5:
        if carta1_n_suited >= 5:
            print("flush of", carta1[0])
        else:
            print("flush of", carta2[0])
    if straight == 1:
        print("straight")
    if straight == 1 and (carta1_n_suited >= 5 or carta2_n_suited >= 5):
        if (v[0] == 10 and v[4] == 14) or (v[1] == 10 and v[5] == 14) or (v[2] == 10 and v[6]):
            royal_flush = 1
            print("***ROYAL FLUSH***")
    if royal_flush == 1:
        print("You win, nothing can beat you")
    elif straight == 1 and (carta1_n_suited >= 5 or carta2_n_suited >= 5):
        print("With your hand, only a royal flush can beat you")
    elif carta1_n_pares == 4 or carta2_n_pares == 4:
        print("With your hand, a straight flush and above can beat you")
    elif carta1_n_suited == 5 or carta2_n_suited >= 5:
        print("With your hand,a full house and above can beat you")
    elif straight == 1:
        print("With your hand,a flush and above can beat you")
    elif carta1_n_pares == 3 or carta2_n_pares == 3:
        print("With your hand,a straight and above can beat you")
    elif carta1_n_pares == 2 and carta2_n_pares == 2:
        print("With your hand,a three of a kind and above can beat you")
    elif carta1_n_pares == 2 or carta2_n_pares == 2:
        if carta1_n_pares == 2:
            print("With your hand,a pair higher than", carta1[1], "and above can beat you")
        else:
            print("With your hand,a pair higher than", carta2[1], "and above can beat you")
    else:
        print("anything can beat you")
    print("--------------------------------------------------------------------------------")

#menu

a = 0
b = 2
digito = 0
print("Welcome to poker helper")
while(digito==0):
    a = int(input("1 - start a new game \n2 - help\n3 - credits\n0 - exit\n"))
    if a == 1:
        while(digito == 0):
            print("Type you hand:")
            carta1 = str(input("card 1:"))
            carta2 = str(input("card 2:"))
            opening_hand(carta1, carta2)
            b = int(input("1- go to flop\n2- opening hand again\n"))
            if b == 1:
                break
        while (digito == 0):
            print("Type the three community cards")
            carta3 = str(input("card 3:"))
            carta4 = str(input("card 4:"))
            carta5 = str(input("card 5:"))
            flop(carta1, carta2, carta3, carta4, carta5)
            c = int(input("1- go to turn\n2- flop again\n"))
            if c == 1:
                break
        while (digito == 0):
            print("Type the next community card")
            carta6 = str(input("card 6:"))
            turn(carta1, carta2, carta3, carta4, carta5, carta6)
            d = int(input("1- go to river\n2- turn again\n"))
            if d == 1:
                break
        while (digito == 0):
            print("Type the last community card")
            carta7 = str(input("card 7:"))
            river(carta1, carta2, carta3, carta4, carta5, carta6,carta7)
            e = int(input("1- finish \n2- river again\n"))
            if e == 1:
                break
    elif a == 2:
        print("To type a card just put the suit(in capslock) first and then the value(in capslock), ex:")
        print("Clubs Ten = CT")
        print("(note the only number that you have to put the letter instead of the number itself its ten)")
        print("Diamond 4 = D4\nHearts Ace = HA\nSpades Queen = SQ\norder of the cards by value:")
        print("A>K>Q>J>T>9>8>7>6>5>4>3>2")
        print("order of the combinations better to worse:")
        print("Royal flush>straight flush>4 of a kind>Full house>Flush>3 of a kind>2 pairs>pair>highest card")
        print("")
    elif a == 3:
        print("My twitter account @marcao137")
    elif a == 0:
        break
