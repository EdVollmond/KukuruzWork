 
from text_normalizer import yearofmask_normalizer

def row_editor(PARTY_SPLITTED_RAW,YEARS_OF_MASKS,PARTY_SPLITTED0,partysizcount):
    for i in range (0,partysizcount):
        #разбитие изделия на параметры
        ROW_SPLITTED_RAW = PARTY_SPLITTED_RAW[i].split(sep = " ") 
        
        ROW_SPLITTED = ROW_SPLITTED_RAW

        if "BAD" in ROW_SPLITTED:
            ROW_SPLITTED.pop(ROW_SPLITTED.index("BAD"))

        #подставляем недостающие значения
        if i > 0:
            lastrow = i - 1
            
            if ROW_SPLITTED[len(ROW_SPLITTED)-1] == "":
                ROW_SPLITTED.pop()
            if ROW_SPLITTED[0] == "-":
                ROW_SPLITTED[0] = PARTY_SPLITTED0[lastrow][0]
            for j in range (1,6):
                if len(ROW_SPLITTED) < j+1:
                    ROW_SPLITTED.append(PARTY_SPLITTED0[lastrow][j])
            for l in range(0, len(ROW_SPLITTED)):
                if ROW_SPLITTED[l] == "-":
                    ROW_SPLITTED[l] = PARTY_SPLITTED0[lastrow][l]
        else:
            partynumber = ROW_SPLITTED[6]
            ROW_SPLITTED.pop()

        if "BAD" in ROW_SPLITTED_RAW:
            ROW_SPLITTED.append("BAD")
        
        yearofmask = yearofmask_normalizer(ROW_SPLITTED[2])
        YEARS_OF_MASKS.append(int(yearofmask))

        PARTY_SPLITTED0.append(ROW_SPLITTED)

    return(partynumber)