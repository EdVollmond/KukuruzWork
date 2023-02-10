import json

def saveall(SOLUTION_BAD,SOLUTION_GOOD,SO_OLD,NOT_SO_OLD,INTRO,CHECKSESSION1,CHECKSESSION0,NUMBERS,JOURNALNUMBERS,CURRENTSIZTYPES,SESSIONHISTORY,HISTORYNUMBERS):
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
    
    with open('JSON/SESSIONHISTORY.json', 'w', encoding="utf-8") as fw:
        json.dump(SESSIONHISTORY, fw, ensure_ascii=False)   
    with open('JSON/HISTORYNUMBERS.json', 'w', encoding="utf-8") as fw:
        json.dump(HISTORYNUMBERS, fw, ensure_ascii=False)   