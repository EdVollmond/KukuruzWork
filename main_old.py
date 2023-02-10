import json

from text_normalizer import party_normalizer
from checking import checking
from tools import datetofull
from ending import ending

with open('JSON/FROMWHERE.json',  'r', encoding='utf-8') as fr:
    FROMWHERE = json.load(fr)

with open('JSON/INTRO.json',  'r', encoding='utf-8') as fr:
    INTRO = json.load(fr)
with open('JSON/CHECKSESSION0.json',  'r', encoding='utf-8') as fr:
    CHECKSESSION0 = json.load(fr)
with open('JSON/CHECKSESSION1.json',  'r', encoding='utf-8') as fr:
    CHECKSESSION1 = json.load(fr)
with open('JSON/JOURNALNUMBERS.json',  'r', encoding='utf-8') as fr:
    JOURNALNUMBERS = json.load(fr)
with open('JSON/NUMBERS.json',  'r', encoding='utf-8') as fr:
    NUMBERS = json.load(fr)

with open('JSON/SIZTYPES.json',  'r', encoding='utf-8') as fr:
    SIZTYPES = json.load(fr)
with open('JSON/CURRENTSIZTYPES.json',  'r', encoding='utf-8') as fr:
    CURRENTSIZTYPES = json.load(fr)
with open('JSON/SOLUTION_BAD.json',  'r', encoding='utf-8') as fr:
    SOLUTION_BAD = json.load(fr)
with open('JSON/SOLUTION_GOOD.json',  'r', encoding='utf-8') as fr:
    SOLUTION_GOOD = json.load(fr)
with open('JSON/NOT_SO_OLD.json',  'r', encoding='utf-8') as fr:
    NOT_SO_OLD = json.load(fr)
with open('JSON/SO_OLD.json',  'r', encoding='utf-8') as fr:
    SO_OLD = json.load(fr)

with open('JSON/FILTERSRESIST.json',  'r', encoding='utf-8') as fr:
    FILTERSRESIST = json.load(fr)

with open('JSON/ONEOUTLETVALVE.json',  'r', encoding='utf-8') as fr:
    ONEOUTLETVALVE = json.load(fr)

with open('JSON/SIZPARTS.json',  'r', encoding='utf-8') as fr:
    SIZPARTS = json.load(fr)


SIZCHECK0=[]
SIZPUT=[]

partysizcount = 0

sizgood = True
partygood = True
allpartygood = True


current_datetime = JOURNALNUMBERS["current_datetime"]
DATETIME_SPLITTED = current_datetime.split(".")
shortyear = int(DATETIME_SPLITTED[2]) - 2000
monthdateshort = str(DATETIME_SPLITTED[1])
daydate = str(DATETIME_SPLITTED[0])
yeardate = str(DATETIME_SPLITTED[2])
monthdatefull = datetofull(monthdateshort)

msg_raw = input()

msg = msg_raw.upper()

if msg == 'END':
    
    ending(NUMBERS,FROMWHERE,JOURNALNUMBERS,SIZTYPES,INTRO,SOLUTION_GOOD,SOLUTION_BAD,NOT_SO_OLD,SO_OLD,CHECKSESSION0,CHECKSESSION1,CURRENTSIZTYPES,daydate,monthdateshort,yeardate,monthdatefull)


    with open('JSON/FROMWHERE.json', 'w', encoding="utf-8") as fw:
        json.dump(FROMWHERE, fw, ensure_ascii=False)

    with open('JSON/SOLUTION_BAD.json', 'w', encoding="utf-8") as fw:
        json.dump(SOLUTION_BAD, fw, ensure_ascii=False)
    with open('JSON/SOLUTION_GOOD.json', 'w', encoding="utf-8") as fw:
        json.dump(SOLUTION_GOOD, fw, ensure_ascii=False)


    with open('JSON/JOURNALNUMBERS.json', 'w', encoding="utf-8") as fw:
        json.dump(JOURNALNUMBERS, fw, ensure_ascii=False)
    with open('JSON/INTRO.json', 'w', encoding="utf-8") as fw:
        json.dump(INTRO, fw, ensure_ascii=False)
    with open('JSON/NUMBERS.json', 'w', encoding="utf-8") as fw:
        json.dump(NUMBERS, fw, ensure_ascii=False)

    with open('JSON/CURRENTSIZTYPES.json', 'w', encoding="utf-8") as fw:
        json.dump(CURRENTSIZTYPES, fw, ensure_ascii=False)
    with open('JSON/NOT_SO_OLD.json', 'w', encoding="utf-8") as fw:
        json.dump(NOT_SO_OLD, fw, ensure_ascii=False)
    with open('JSON/SO_OLD.json', 'w', encoding="utf-8") as fw:
        json.dump(SO_OLD, fw, ensure_ascii=False)
    
    with open('JSON/CHECKSESSION1.json', 'w', encoding="utf-8") as fw:
        json.dump(CHECKSESSION1, fw, ensure_ascii=False)
    with open('JSON/CHECKSESSION0.json', 'w', encoding="utf-8") as fw:
        json.dump(CHECKSESSION0, fw, ensure_ascii=False)  

    print(id,"Ввод закончен")

else:
    party = party_normalizer(msg)

    PARTY_SPLITTED_RAW = party.split(sep="\n") #разделение на строки

    checking(PARTY_SPLITTED_RAW,NUMBERS,ONEOUTLETVALVE,SIZPARTS,SIZTYPES,FILTERSRESIST,JOURNALNUMBERS,SOLUTION_GOOD,SOLUTION_BAD,NOT_SO_OLD,SO_OLD,CURRENTSIZTYPES,INTRO,CHECKSESSION0,CHECKSESSION1,shortyear,daydate,monthdateshort,yeardate)

    with open('JSON/SOLUTION_BAD.json', 'w', encoding="utf-8") as fw:
        json.dump(SOLUTION_BAD, fw, ensure_ascii=False)
    with open('JSON/SOLUTION_GOOD.json', 'w', encoding="utf-8") as fw:
        json.dump(SOLUTION_GOOD, fw, ensure_ascii=False)

    with open('JSON/SO_OLD.json', 'w', encoding="utf-8") as fw:
        json.dump(SO_OLD, fw, ensure_ascii=False)
    with open('JSON/NOT_SO_OLD.json', 'w', encoding="utf-8") as fw:
        json.dump(NOT_SO_OLD, fw, ensure_ascii=False)

    with open('JSON/INTRO.json', 'w', encoding="utf-8") as fw:
        json.dump(INTRO, fw, ensure_ascii=False)

    with open('JSON/CHECKSESSION1.json', 'w', encoding="utf-8") as fw:
        json.dump(CHECKSESSION1, fw, ensure_ascii=False)
    with open('JSON/CHECKSESSION0.json', 'w', encoding="utf-8") as fw:
        json.dump(CHECKSESSION0, fw, ensure_ascii=False)    
    
    with open('JSON/NUMBERS.json', 'w', encoding="utf-8") as fw:
        json.dump(NUMBERS, fw, ensure_ascii=False)  
    with open('JSON/JOURNALNUMBERS.json', 'w', encoding="utf-8") as fw:
        json.dump(JOURNALNUMBERS, fw, ensure_ascii=False)  
    with open('JSON/CURRENTSIZTYPES.json', 'w', encoding="utf-8") as fw:
        json.dump(CURRENTSIZTYPES, fw, ensure_ascii=False)                              
    
    
    print(id,"Данные партии введены. Введи еще или закончи ввод")
    print(CHECKSESSION0)