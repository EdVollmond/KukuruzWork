from row_editor import row_editor
from party_editor import party_editor
from filtermark_editor import filtermark_editor
import json



def checking(PARTY_SPLITTED_RAW,NUMBERS,ONEOUTLETVALVE,SIZPARTS,SIZTYPES,FILTERSRESIST,JOURNALNUMBERS,SOLUTION_GOOD,SOLUTION_BAD,NOT_SO_OLD,SO_OLD,CURRENTSIZTYPES,INTRO,CHECKSESSION0,CHECKSESSION1,HISTORYNUMBERS,shortyear,daydate,monthdateshort,yeardate):

    PARTY_SPLITTED0 = []
    PARTY_SPLITTED1 = []
    YEARS_OF_MASKS = []

    if "BAD" in PARTY_SPLITTED_RAW:
        partygood = False
        allpartygood = False
        PARTY_SPLITTED_RAW.pop(PARTY_SPLITTED_RAW.index("BAD"))
    else:
        partygood = True
        allpartygood = True
        
    #число изделий в партии
    partysizcount = len(PARTY_SPLITTED_RAW)

    #работаем со строкой
    partynumber = row_editor(PARTY_SPLITTED_RAW,YEARS_OF_MASKS,PARTY_SPLITTED0,partysizcount)
                        
    #работаем с партией
    sizsize = party_editor(PARTY_SPLITTED0,NUMBERS,ONEOUTLETVALVE,SIZPARTS,SIZTYPES,FILTERSRESIST,partysizcount,partygood,allpartygood)

    # вписываем номер партии по порядку
    PARTY_SPLITTED1.insert(0,str(NUMBERS["checkpartynumber"]+1))
    # определяем тип проверяемых изделий
    if PARTY_SPLITTED0[0][6] in SIZTYPES["ADDITIONAL"]:
        if len(PARTY_SPLITTED0) == 1:
            typeofsiz = "дополнительный патрон"
        else:
            typeofsiz = "доп. патроны"

    else:
        if len(PARTY_SPLITTED0) == 1:
            typeofsiz = "противогаз"
        else:
            typeofsiz = "противогазы"

    # разбираем маркировку фильтра
    filtermarkedited = filtermark_editor(PARTY_SPLITTED0,SIZTYPES,YEARS_OF_MASKS,shortyear,partynumber,sizsize)
    sizmodel = filtermarkedited[0]
    yearofparty = filtermarkedited[1]
    quartalofparty = filtermarkedited[2]
    
    sizfullname = typeofsiz + " " + sizmodel
    li = list(typeofsiz)
    li[len(li)-1] = 'ов'
    typeofsiz_vinpadezh = ''.join(li)
    sizfullname_vinpadezh = typeofsiz_vinpadezh + " " + sizmodel
    
    PARTY_SPLITTED1.insert(1,str(sizfullname) + "\n" + "Партия № " + str(partynumber) + ", " + str(yearofparty) + " г., " + str(quartalofparty))


    if PARTY_SPLITTED0[0][6] in SIZTYPES ["ADDITIONAL"]:    
        partyjournalrange0 = JOURNALNUMBERS["journaladditionalnumber"] + 1
        partyjournalrange1 = JOURNALNUMBERS["journaladditionalnumber"] + partysizcount
        with open('JSON/HISTORYNUMBERS.json',  'r', encoding='utf-8') as fr:
            HISTORYNUMBERS = json.load(fr)
        HISTORYNUMBERS["additionalnumbers"].append(partysizcount)
        HISTORYNUMBERS['typeofsiz'].append('additional')
    else: 
        partyjournalrange0 = JOURNALNUMBERS["journalgasmasknumber"] + 1
        partyjournalrange1 = JOURNALNUMBERS["journalgasmasknumber"] + partysizcount
        with open('JSON/HISTORYNUMBERS.json',  'r', encoding='utf-8') as fr:
            HISTORYNUMBERS = json.load(fr)
        HISTORYNUMBERS["gasmasknumbers"].append(partysizcount)
        HISTORYNUMBERS['typeofsiz'].append('gasmasks')
        
    with open('JSON/HISTORYNUMBERS.json', 'w', encoding="utf-8") as fw:
        json.dump(HISTORYNUMBERS, fw, ensure_ascii=False)

    if partysizcount > 1:
        partyjournalrange = str(partyjournalrange0) + "-" + str(partyjournalrange1)
    else:
        partyjournalrange = str(partyjournalrange0)

    
    actdate = str(daydate) + '.' + str(monthdateshort) + '.' + str(yeardate) + ' г.' 

    PARTY_SPLITTED1.insert(2, actdate + " \n" + partyjournalrange)

    if allpartygood == True:
        PARTY_SPLITTED1.insert(3,"Положительные")
        PARTY_SPLITTED1.insert(4,"Соответствует ТУ")
        if sizfullname in SOLUTION_GOOD:
            SOLUTION_GOOD[sizfullname].append(partynumber)
        else:
            SOLUTION_GOOD[sizfullname] = []
            SOLUTION_GOOD[sizfullname].append(partynumber)

        olding_year = int(yeardate) - int(yearofparty)

        if olding_year < 12:
            if sizfullname_vinpadezh in NOT_SO_OLD:
                NOT_SO_OLD[sizfullname_vinpadezh].append(partynumber)
            else:
                NOT_SO_OLD[sizfullname_vinpadezh] = []
                NOT_SO_OLD[sizfullname_vinpadezh].append(partynumber)
        else:
            if sizfullname_vinpadezh in SO_OLD:
                SO_OLD[sizfullname_vinpadezh].append(partynumber)
            else:
                SO_OLD[sizfullname_vinpadezh] = []
                SO_OLD[sizfullname_vinpadezh].append(partynumber)

    else:
        PARTY_SPLITTED1.insert(3,"Отрицательные")
        PARTY_SPLITTED1.insert(4,"Не соответствует ТУ")
        if sizfullname in SOLUTION_BAD:
            SOLUTION_BAD[sizfullname].append(partynumber)
        else:
            SOLUTION_BAD[sizfullname] = []
            SOLUTION_BAD[sizfullname].append(partynumber)


    YEARS_OF_MASKS.clear()

    CURRENTSIZTYPES.append(typeofsiz)
    
    if sizmodel in INTRO:
        INTRO[sizmodel] = INTRO[sizmodel] + partysizcount
    else: 
        INTRO[sizmodel] = partysizcount


    CHECKSESSION0.append(PARTY_SPLITTED0)
    CHECKSESSION1.append(PARTY_SPLITTED1)

    NUMBERS["checkpartynumber"] = NUMBERS["checkpartynumber"] + 1
    NUMBERS["siznumber"] = NUMBERS["siznumber"] + partysizcount

    if PARTY_SPLITTED0[0][6] in SIZTYPES ["ADDITIONAL"]:
        JOURNALNUMBERS["journaladditionalnumber"] = JOURNALNUMBERS["journaladditionalnumber"] + partysizcount
    else:
        JOURNALNUMBERS["journalgasmasknumber"] = JOURNALNUMBERS["journalgasmasknumber"] + partysizcount

    print("Партия обработана")