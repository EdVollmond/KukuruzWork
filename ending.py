from docxtpl import DocxTemplate
import json
import random

def ending(JOURNALNUMBERS,daydate,monthdateshort,yeardate,monthdatefull,fromwhere,fullintro,fullsolution,lastpartsolution):

    seed = daydate + monthdateshort + yeardate
    random.seed(seed)

    temperature = random.normalvariate(20,2)
    while temperature > 22:
        temperature = random.normalvariate(20,2)
    while temperature < 18:
        temperature = random.normalvariate(20,2)
    temperature = round (temperature,1)

    pressure = random.normalvariate(750,2)
    while pressure > 753:
        pressure = random.normalvariate(750,2)
    while pressure < 747:
        pressure = random.normalvariate(750,2)
    pressure = round (pressure,1)

    wet = random.normalvariate(40,5)
    while wet > 45:
        wet = random.normalvariate(45,5)
    while wet < 35:
        wet = random.normalvariate(45,5)
    wet = round (wet,1)



    with open('JSON/turnprotectiontime.json',  'r', encoding='utf-8') as fr:
        turnprotectiontime = json.load(fr)
    if turnprotectiontime == True:
        doc = DocxTemplate("templates/template9.docx")
    else:
        doc = DocxTemplate("templates/template8.docx")
    context = { 'fullintro' : fullintro, 'actnumber' : JOURNALNUMBERS["journalactnumber"], 'daydate': daydate, 'monthdateshort': monthdateshort,
    'monthdatefull': monthdatefull, 'yeardate': yeardate, 'fullsolution': fullsolution,'lastpartsolution': lastpartsolution,'temperature': temperature,
    'pressure': pressure,'wet': wet}

    fromwherename = fromwhere.replace('"', "")

    docname = "АКТ № " + str(JOURNALNUMBERS["journalactnumber"]) + " для " + fromwherename + ".docx"

    doc.render(context)
    doc.save("acts/" + docname)
    print("Акт создан")
    
    return(docname)

