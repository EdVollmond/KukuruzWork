import json

def preview_writer(ITEMS0,ITEMS1):

    with open('JSON/turnprotectiontime.json',  'r', encoding='utf-8') as fr:
        turnprotectiontime = json.load(fr)

    preview0 = ""
    preview1 = ""

    sizcount=0

    if turnprotectiontime == True:
        for partynum in range (0,len(ITEMS0)):
            for rownum in range (0,len(ITEMS0[partynum])):
                if ITEMS0[partynum][rownum][-1] != "> 25":
                    ITEMS0[partynum][rownum].append("> 25")

    for partynum in range (0,len(ITEMS0)):
        for rownum in range (0,len(ITEMS0[partynum])):
            for cellnum in range (0,len(ITEMS0[partynum][rownum])):
                preview0 = preview0 + str(ITEMS0[partynum][rownum][cellnum]).replace("\n"," ") + " | "
            preview0 = preview0 + "\n" 
        sizcount = sizcount + len(ITEMS0[partynum])

    for rownum in range (0,len(ITEMS1)):
        for cellnum in range (0,len(ITEMS1[rownum])):
            preview1 = preview1 + str(ITEMS1[rownum][cellnum]).replace("\n"," ") + " | "

    preview = preview1 + "\n" + "\n" + preview0 + "\n" 

    return(preview)


    print("Полный предпросмотр табличных данных")


def mini_preview_writer(ITEMS0):

    with open('JSON/turnprotectiontime.json',  'r', encoding='utf-8') as fr:
        turnprotectiontime = json.load(fr)

    preview = ""


    if turnprotectiontime == True:
        for partynum in range (0,len(ITEMS0)):
            for rownum in range (0,len(ITEMS0[partynum])):
                if ITEMS0[partynum][rownum][-1] != "> 25":
                    ITEMS0[partynum][rownum].append("> 25")

    for rownum in range (0,len(ITEMS0[-1])):
        for cellnum in range (0,len(ITEMS0[-1][rownum])):
            preview = preview + str(ITEMS0[-1][rownum][cellnum]).replace("\n"," ") + " | "
        preview = preview + "\n" 
    return(preview)

    print("Малый предпросмотр табличных данных")
