from tools import dict_to_solution

def solution_generator(SOLUTION_GOOD, SOLUTION_BAD,NOT_SO_OLD,SO_OLD,CURRENTSIZTYPES,yeardate,daydate,monthdateshort):

    SHORTCURRENTSIZTYPES = list(set(CURRENTSIZTYPES))
    
    if len(SHORTCURRENTSIZTYPES) > 1:
        shortcurrentsiztypes = " и ".join(SHORTCURRENTSIZTYPES)
    else: 
        shortcurrentsiztypes = "".join(SHORTCURRENTSIZTYPES)

    itemsgood = dict_to_solution(SOLUTION_GOOD)
    itemsbad = dict_to_solution(SOLUTION_BAD)

    shortcurrentsiztypes = shortcurrentsiztypes.capitalize()

    firstpartsolution = shortcurrentsiztypes + " проверены по утвержденным методическим указаниям. В результате проведенных лабораторных испытаний установлено, что: "

    if len(SOLUTION_GOOD) > 0:
        goodpartsolution = itemsgood + " – соответствуют техническим условиям и подлежат дальнейшему хранению."
    else:
        goodpartsolution = ""

    if len(SOLUTION_BAD) > 0:
        badpartsolution =  itemsbad + " – не соответствуют техническим условиям и подлежат списанию установленным порядком."
    else:
        badpartsolution = ""


    yeardate_next_old = int(yeardate) + 2
    yeardate_next = int(yeardate) + 5

    itemsnew = dict_to_solution(NOT_SO_OLD)
    itemsold = dict_to_solution(SO_OLD)

    if len(SOLUTION_GOOD) > 0:
        if len(NOT_SO_OLD) == 0 and len(SO_OLD) > 0:
            lastpartsolution = "Акт выдан сроком на: два года.\nДата следующей проверки: " + str(daydate) + "." + str(monthdateshort) + "." + str(yeardate_next_old) + " г."
        if len(NOT_SO_OLD) > 0 and len(SO_OLD) == 0:
            lastpartsolution = "Акт выдан сроком на: пять лет.\nДата следующей проверки: " + str(daydate) + "." + str(monthdateshort) + "." + str(yeardate_next) + " г."
        if len(NOT_SO_OLD) > 0 and len(SO_OLD) > 0:
            lastpartsolution = "Для " + itemsnew + " выдан сроком на: пять лет.\nДата следующей проверки: " + str(daydate) + "." + str(monthdateshort) + "." + str(yeardate_next) + " г." + "\n" "Для " + itemsold + " выдан сроком на: два года.\nДата следующей проверки: " + str(daydate) + "." + str(monthdateshort) + "." + str(yeardate_next_old) + " г."
    else:
        lastpartsolution = ""
    
    fullsolution = firstpartsolution + goodpartsolution + badpartsolution

    return(fullsolution, lastpartsolution)