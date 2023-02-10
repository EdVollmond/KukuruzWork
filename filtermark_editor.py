from text_normalizer import markoffilter_normalizer, quartalofparty_normalizer
from tools import nearest

def filtermark_editor(PARTY_SPLITTED0,SIZTYPES,YEARS_OF_MASKS,shortyear,partynumber,sizsize):

    markoffilter = markoffilter_normalizer(PARTY_SPLITTED0[0][7])

    typeoffilter = PARTY_SPLITTED0[0][6]

    MARK_SPLITTED = markoffilter.split(sep = "-") 

    if typeoffilter == "ГП-7КБ":

        MARKIGNORE1 = ["Дата изготовления:","Дата:","Дата изготовления","Дата"]
        if MARK_SPLITTED[0] in MARKIGNORE1:
        
            yearofparty = MARK_SPLITTED[3]
            quartalofparty = MARK_SPLITTED[2]
            quartalofparty = quartalofparty_normalizer(quartalofparty)

        else:
            yearofparty = MARK_SPLITTED[2]
            quartalofparty = MARK_SPLITTED[1]

    else:
        MARKIGNORE0 = ["26","М","M","90","Партия№"]
        if MARK_SPLITTED[0] in MARKIGNORE0:
            MARK_SPLITTED.pop(0)
        
        partynumberindex = MARK_SPLITTED.index(partynumber)

        MARK_SPLITTED.pop(partynumberindex)

        yearofmask_avg = round(sum(YEARS_OF_MASKS) / len(YEARS_OF_MASKS))

        MARK_SPLITTED[0] = int(MARK_SPLITTED[0])
        MARK_SPLITTED[1] = int(MARK_SPLITTED[1])

        yearofparty = nearest(MARK_SPLITTED, yearofmask_avg)

        MARK_SPLITTED.pop(MARK_SPLITTED.index(yearofparty))
        quartalofparty = MARK_SPLITTED[0]

    yearofparty = int(yearofparty)
    if yearofparty > 9:
        if yearofparty > shortyear:
            yearofparty = str(yearofparty)
            yearofparty = "19" + yearofparty
        else:
            yearofparty = str(yearofparty)
            yearofparty = "20" + yearofparty
    else:
        yearofparty = str(yearofparty)
        yearofparty = "200" + yearofparty

    if PARTY_SPLITTED0[0][6] == "ГП-5":
        if PARTY_SPLITTED0[0][1] == "ШМ-62" or "ШМ-62у" or "ШМП":
            sizmodel = "ГП-5"
        if PARTY_SPLITTED0[0][1] == "ШМ-66Му":
            sizmodel = "ГП-5М"
        if PARTY_SPLITTED0[0][1] == "МД-1а":
            if int(sizsize) < 3:
                sizmodel = "ПДФ-Да"
            else:
                sizmodel = "ПДФ-Ша"
        if PARTY_SPLITTED0[0][1] == "МД-3":
            if int(sizsize) < 3:
                sizmodel = "ПДФ-Д"
            else:
                sizmodel = "ПДФ-Ш"

    if PARTY_SPLITTED0[0][6] == "ЕО-62К":
        if PARTY_SPLITTED0[0][1] == "ШМ-62" or "ШМ-62у":
            sizmodel = "ГП-5"
        else:
            sizmodel = "ПМГ-2"

    if PARTY_SPLITTED0[0][6] == "ЕО-18":
        if PARTY_SPLITTED0[0][1] == "ШМ-62" or "ШМ-62у" or "ШМП":
            sizmodel = "ГП-5"
        sizmodel = "ПМГ"


    if PARTY_SPLITTED0[0][6] == "ГП-7К":
        if PARTY_SPLITTED0[0][1] == "МГП":
            sizmodel = "ГП-7"
        if PARTY_SPLITTED0[0][1] == "МГП-В":
            sizmodel = "ГП-7В"
        if PARTY_SPLITTED0[0][1] == "М-80":
            sizmodel = "ГП-7ВМ"
        if PARTY_SPLITTED0[0][1] == "МБ-1-80":
            sizmodel = "ГП-7ВМ"
        if PARTY_SPLITTED0[0][1] == "Бриз-4303":
            sizmodel = "ГП-7ВМ"
        if PARTY_SPLITTED0[0][1] == "Бриз-4304":
            sizmodel = "ГП-7ВМ"
        if PARTY_SPLITTED0[0][1] == "МП-04":
            sizmodel = "ГП-7ВМ"
        if PARTY_SPLITTED0[0][1] == "МП-04В":
            sizmodel = "ГП-7ВМ"
        if PARTY_SPLITTED0[0][1] == "МП-07":
            sizmodel = "ГП-7ВМ"
        if PARTY_SPLITTED0[0][1] == "МП-07В":
            sizmodel = "ГП-7ВМ"
        if PARTY_SPLITTED0[0][1] == "МГУ":
            sizmodel = "ГП-7ВМ"
        if PARTY_SPLITTED0[0][1] == "МГУ-В":
            sizmodel = "ГП-7ВМ"
        if PARTY_SPLITTED0[0][1] == "МД-4":
            if int(sizsize) < 2:
                sizmodel = "ПДФ-2Д"
            else:
                sizmodel = "ПДФ-2Ш"

    if PARTY_SPLITTED0[0][6] == "ГП-7КС":
        if PARTY_SPLITTED0[0][1] == "МГП":
            sizmodel = "ГП-7"
        if PARTY_SPLITTED0[0][1] == "МГП-В":
            sizmodel = "ГП-7В"
        if PARTY_SPLITTED0[0][1] == "МБ-1-80":
            sizmodel = "ГП-7ВМ"
        if PARTY_SPLITTED0[0][1] == "М-80":
            sizmodel = "ГП-7ВМ"
        if PARTY_SPLITTED0[0][1] == "Бриз-4303":
            sizmodel = "ГП-7ВМ"
        if PARTY_SPLITTED0[0][1] == "Бриз-4304":
            sizmodel = "ГП-7ВМ"
        if PARTY_SPLITTED0[0][1] == "МП-04":
            sizmodel = "ГП-7ВМ"
        if PARTY_SPLITTED0[0][1] == "МП-04В":
            sizmodel = "ГП-7ВМ"
        if PARTY_SPLITTED0[0][1] == "МП-07":
            sizmodel = "ГП-7ВМ"
        if PARTY_SPLITTED0[0][1] == "МП-07В":
            sizmodel = "ГП-7ВМ"
        if PARTY_SPLITTED0[0][1] == "МГУ":
            sizmodel = "ГП-7ВМ"
        if PARTY_SPLITTED0[0][1] == "МГУ-В":
            sizmodel = "ГП-7ВМ"
        if PARTY_SPLITTED0[0][1] == "МД-4":
            if sizsize < 2:
                sizmodel = "ПДФ-2Д"
            else:
                sizmodel = "ПДФ-2Ш"

    if PARTY_SPLITTED0[0][6] == "ГП-7КБ": 
        sizmodel = "ГП-7Б"
    if PARTY_SPLITTED0[0][6] == "ГП-7ТК":
        sizmodel = "ГП-7ВМТ"
    if PARTY_SPLITTED0[0][6] == "ВК-600":
        sizmodel = "УЗС ВК"
    if PARTY_SPLITTED0[0][6] == "ВК-320":
        sizmodel = "УЗС ВК"
    if PARTY_SPLITTED0[0][6] == "ЕО-1-08-01":
        sizmodel = "ПМК"
    if PARTY_SPLITTED0[0][6] == "ЕО-1-15-01":
        sizmodel = "ПМК-2"
    if PARTY_SPLITTED0[0][6] in SIZTYPES ["ADDITIONAL"]:
        sizmodel = PARTY_SPLITTED0[0][6]

    return(sizmodel,yearofparty,quartalofparty)