import random


def party_editor(PARTY_SPLITTED0,NUMBERS,ONEOUTLETVALVE,SIZPARTS,SIZTYPES,FILTERSRESIST,partysizcount,partygood,allpartygood):

    for i in range (0,partysizcount):
        
        if "BAD" in PARTY_SPLITTED0[i]:
            PARTY_SPLITTED0[i].pop(PARTY_SPLITTED0[i].index("BAD"))
            sizgood = False
            allpartygood = False
        else:
            sizgood = True

        sizsize = PARTY_SPLITTED0[i][0]

        #совмещаем маркировки лицевой части в одну ячейку
        PARTY_SPLITTED0[i][0] = PARTY_SPLITTED0[i][0] + "\n" + PARTY_SPLITTED0[i][1] + "\n" + PARTY_SPLITTED0[i][2]
        
        PARTY_SPLITTED0[i].insert(0,NUMBERS["siznumber"]+i+1)
        PARTY_SPLITTED0[i].insert(1,PARTY_SPLITTED0[i][5])
        PARTY_SPLITTED0[i].insert(3,"Герм.")

        if sizgood == True and partygood == True:
            if PARTY_SPLITTED0[i][1] in ONEOUTLETVALVE:
                x = random.normalvariate(9,3)
                x = round (x)
                if x > 18:
                    x = 18
                if x < 1:
                    x = 1
                x = x*20
                
                PARTY_SPLITTED0[i].insert(4,str(x))
            elif PARTY_SPLITTED0[i][1] == "-":
                PARTY_SPLITTED0[i].insert(4,"—")
            else:
                x = random.normalvariate(9,3)
                x = round (x)
                if x > 18:
                    x = 18
                if x < 1:
                    x = 1
                x = x*20

                y = random.normalvariate(9,3)
                y = round (y)
                if y > 18:
                    y = 18
                if y < 1:
                    y = 1
                y = y*20

                PARTY_SPLITTED0[i].insert(4,str(x)+"\n"+str(y))


        if sizgood == False and partygood == False:
            if PARTY_SPLITTED0[i][1] in ONEOUTLETVALVE:
                x = random.normalvariate(20,1)
                x = round (x)
                if x < 19:
                    x = 19
                x = x * 20
                PARTY_SPLITTED0[i].insert(4,str(x) + " \n Не более 360!")
            elif PARTY_SPLITTED0[i][1] == "-":
                PARTY_SPLITTED0[i].insert(4,"—")
            else:
                x = random.normalvariate(20,1)
                x = round (x)
                if x < 19:
                    x = 19
                x = x * 20

                y = random.normalvariate(20,1)
                y = round (y)
                if y < 19:
                    y = 19
                y = y * 20

                PARTY_SPLITTED0[i].insert(4,str(x)+"\n"+str(y) + " \n Не более 360!")


        if sizgood == True and partygood == False:
            if PARTY_SPLITTED0[i][1] in ONEOUTLETVALVE:
                x = random.normalvariate(17,2)
                x = round (x)
                x = x * 20
                if x > 360:
                    PARTY_SPLITTED0[i].insert(4,str(x) + " \n Не более 360!")
                else:
                    PARTY_SPLITTED0[i].insert(4,str(x))
            elif PARTY_SPLITTED0[i][1] == "-":
                PARTY_SPLITTED0[i].insert(4,"—")
            else:
                x = random.normalvariate(17,2)
                x = round (x)
                x = x*20

                y = random.normalvariate(17,2)
                y = round (y)
                y = y*20
                if x > 360 or y > 360:
                    PARTY_SPLITTED0[i].insert(4,str(x)+"\n"+str(y) + " \n Не более 360!")
                else:
                    PARTY_SPLITTED0[i].insert(4,str(x)+"\n"+str(y))


        if PARTY_SPLITTED0[i][1] in SIZPARTS["HELMETMASKS"]:
            y = random.normalvariate(25,10)
            y = round (y)
            if y > 40:
                y = 40
            if y < 25:
                y = 25
            x = 1.862 * y
            x = round (x,1)
            PARTY_SPLITTED0[i].insert(5,str(x))
        else:
            PARTY_SPLITTED0[i].insert(5,"—")


        PARTY_SPLITTED0[i].insert(6,PARTY_SPLITTED0[i][10])
        PARTY_SPLITTED0[i].insert(7,PARTY_SPLITTED0[i][9])
        PARTY_SPLITTED0[i].insert(8,"Герм.")

        if partygood == True:
            if PARTY_SPLITTED0[i][6] in FILTERSRESIST['ONESEVENSIX']:
                x = random.normalvariate(15,1)
                x = round (x)
                if x > 17:
                    x = 17
                if x < 13:
                    x = 13
                x = x * 10
                PARTY_SPLITTED0[i].insert(9,str(x))

            if PARTY_SPLITTED0[i][6] in FILTERSRESIST['TWOONEFIVE']:
                x = random.normalvariate(17,1)
                x = round (x)
                if x > 21:
                    x = 21
                if x < 15:
                    x = 15
                x = x * 10
                PARTY_SPLITTED0[i].insert(9,str(x))

            if PARTY_SPLITTED0[i][6] in FILTERSRESIST['ONEONESEVEN']:
                x = random.normalvariate(9,1)
                x = round (x)
                if x > 11:
                    x = 11
                if x < 7:
                    x = 7
                x = x * 10
                PARTY_SPLITTED0[i].insert(9,str(x))

            if PARTY_SPLITTED0[i][6] in FILTERSRESIST['NINEEIGHT']:
                x = random.normalvariate(7.5,1)
                x = round (x)
                if x > 9:
                    x = 9
                if x < 6:
                    x = 6
                x = x * 10
                PARTY_SPLITTED0[i].insert(9,str(x))

        else:
            if PARTY_SPLITTED0[i][6] in FILTERSRESIST['ONESEVENSIX']:
                x = random.normalvariate(17,1)
                x = round (x)
                x = x * 10
                if x > 176:
                    PARTY_SPLITTED0[i].insert(9,str(x) + " \n Не более 176!")
                else:
                    PARTY_SPLITTED0[i].insert(9,str(x))

            if PARTY_SPLITTED0[i][6] in FILTERSRESIST['TWOONEFIVE']:
                x = random.normalvariate(19,1)
                x = round (x)
                x = x * 10
                if x > 215:
                    PARTY_SPLITTED0[i].insert(9,str(x) + " \n Не более 215!")
                else:
                    PARTY_SPLITTED0[i].insert(9,str(x))

            if PARTY_SPLITTED0[i][6] in FILTERSRESIST['ONEONESEVEN']:
                x = random.normalvariate(11,1)
                x = round (x)
                x = x * 10
                if x > 117:
                    PARTY_SPLITTED0[i].insert(9,str(x) + " \n Не более 117!")
                else:
                    PARTY_SPLITTED0[i].insert(9,str(x))

            if PARTY_SPLITTED0[i][6] in FILTERSRESIST['NINEEIGHT']:
                x = random.normalvariate(9,1)
                x = round (x)
                x = x * 10
                if x > 98:
                    PARTY_SPLITTED0[i].insert(9,str(x) + " \n Не более 98!")
                else:
                    PARTY_SPLITTED0[i].insert(9,str(x))

        x = random.normalvariate(3,0.5)
        x = round (x)
        if x > 5:
            x = 3
        if x < 2:
            x = 3
        x = x*4
        if x < 10:
            PARTY_SPLITTED0[i].insert(10,"0,00000"+str(x))
        else:
            PARTY_SPLITTED0[i].insert(10,"0,0000"+str(x))

        while len(PARTY_SPLITTED0[i]) > 11:
            PARTY_SPLITTED0[i].pop()
        
        # PARTY_SPLITTED1.insert(0,str(NUMBERS["checkpartynumber"] + 1))
                                                               
        # определяем тип проверяемых изделий
        if PARTY_SPLITTED0[i][6] in SIZTYPES["ADDITIONAL"]:
            if len(PARTY_SPLITTED0) == 1:
                typeofsiz = "дополнительный патрон"
            else:
                typeofsiz = "доп. патроны"

        else:
            if len(PARTY_SPLITTED0) == 1:
                typeofsiz = "противогаз"
            else:
                typeofsiz = "противогазы"

    return(sizsize)