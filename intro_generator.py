def intro_generator(SIZTYPES,INTRO,fromwhere):
    
    GASMASKINTROLIST=[]

    for i in range (0,len(SIZTYPES["GASMASKS"])):
        if SIZTYPES["GASMASKS"][i] in INTRO.keys():
            numberpartofintrolist = INTRO[SIZTYPES["GASMASKS"][i]]
            partofintrolist = "противогазы " + SIZTYPES["GASMASKS"][i] + " в количестве " + str(numberpartofintrolist)
            if numberpartofintrolist == 1:
                partofintrolist = partofintrolist + " комплекта"
            else:
                partofintrolist = partofintrolist + " комплектов"
            GASMASKINTROLIST.append(partofintrolist)
    for i in range (0,len(SIZTYPES["ADDITIONAL"])):
        if SIZTYPES["ADDITIONAL"][i] in INTRO.keys():
            numberpartofintrolist = INTRO[SIZTYPES["ADDITIONAL"][i]]
            partofintrolist = "дополнительные патроны" + SIZTYPES["ADDITIONAL"][i] + " в количестве " + str(numberpartofintrolist)
            if numberpartofintrolist == 1:
                partofintrolist = partofintrolist + " комплекта"
            else:
                partofintrolist = partofintrolist + " комплектов"
            GASMASKINTROLIST.append(partofintrolist)
    
    gasmaskintrolist = ", ".join(GASMASKINTROLIST)

    fullintro = "Составлен в лаборатории СИЗ ООО «ЛабораторияСИЗ» о том, что от " + fromwhere + " в лабораторию для испытания поступили " + gasmaskintrolist + " со следующей маркировкой:"

    return (fullintro)