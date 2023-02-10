from PyQt5 import uic
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QApplication

from datetime import datetime
from acts import openact

import json

from text_normalizer import party_normalizer
from checking import checking
from tools import datetofull
from ending import ending
from intro_generator import intro_generator
from solution_generator import solution_generator
from saveall import saveall
from clear import clear
from table_writer import table_writer
from preview_writer import preview_writer, mini_preview_writer

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

with open('JSON/const/SIZTYPES.json',  'r', encoding='utf-8') as fr:
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

with open('JSON/SESSIONHISTORY.json',  'r', encoding='utf-8') as fr:
    SESSIONHISTORY = json.load(fr)

with open('JSON/const/FILTERSRESIST.json',  'r', encoding='utf-8') as fr:
    FILTERSRESIST = json.load(fr)
with open('JSON/const/ONEOUTLETVALVE.json',  'r', encoding='utf-8') as fr:
    ONEOUTLETVALVE = json.load(fr)

with open('JSON/const/SIZPARTS.json',  'r', encoding='utf-8') as fr:
    SIZPARTS = json.load(fr)

with open('JSON/DOCNAMES.json',  'r', encoding='utf-8') as fr:
    DOCNAMES = json.load(fr)

with open('JSON/HISTORYNUMBERS.json',  'r', encoding='utf-8') as fr:
    HISTORYNUMBERS = json.load(fr)

with open('JSON/turnprotectiontime.json',  'r', encoding='utf-8') as fr:
    turnprotectiontime = json.load(fr)

with open('JSON/fromwhere.json',  'r', encoding='utf-8') as fr:
    fromwhere = json.load(fr)

#работа с UI
Form, Window = uic.loadUiType("ui/kukuruzwork.ui")
app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()

def journaldate_save(date):
    JOURNALNUMBERS["current_datetime"] = date
    current_datetime = date
    with open('JSON/JOURNALNUMBERS.json', 'w', encoding="utf-8") as fw:
        json.dump(JOURNALNUMBERS, fw, ensure_ascii=False)
    print("Актуальная дата введена")

def journalgasmask_save():
    number = form.gasmaskcounter.value()
    JOURNALNUMBERS["journalgasmasknumber"] = number
    with open('JSON/JOURNALNUMBERS.json', 'w', encoding="utf-8") as fw:
        json.dump(JOURNALNUMBERS, fw, ensure_ascii=False)
    print("Актуальные данные введены")

def journaladditional_save():
    number = form.additionalcounter.value()
    JOURNALNUMBERS["journaladditionalnumber"] = number
    with open('JSON/JOURNALNUMBERS.json', 'w', encoding="utf-8") as fw:
        json.dump(JOURNALNUMBERS, fw, ensure_ascii=False)
    print("Актуальные данные введены")

def journalact_save():
    
    number = form.actcounter.value()
    JOURNALNUMBERS["journalactnumber"] = number
    with open('JSON/JOURNALNUMBERS.json', 'w', encoding="utf-8") as fw:
        json.dump(JOURNALNUMBERS, fw, ensure_ascii=False)
    print("Актуальные данные введены")

def on_click_calendar():
    print(form.calendarWidget.selectedDate().toString('dd.MM.yyyy'))
    form.checkdate.setDate(form.calendarWidget.selectedDate())
    journaldate_save(form.calendarWidget.selectedDate().toString('dd.MM.yyyy'))

def on_dateedit_change():

    print("Изменение даты")

    print(form.checkdate.dateTime().toString('dd.MM.yyyy'))
    form.calendarWidget.setSelectedDate(form.checkdate.date())
    journaldate_save(form.checkdate.dateTime().toString('dd.MM.yyyy'))

def on_click_preview():
    
    fromwhere = form.fromwheretext.toPlainText()
  
    fullintro = intro_generator(SIZTYPES,INTRO,fromwhere)

    fullsolution = solution_generator(SOLUTION_GOOD, SOLUTION_BAD,NOT_SO_OLD,SO_OLD,CURRENTSIZTYPES,yeardate,daydate,monthdateshort)[0]

    session = preview_writer(CHECKSESSION0,CHECKSESSION1)

    lastpartsolution = solution_generator(SOLUTION_GOOD, SOLUTION_BAD,NOT_SO_OLD,SO_OLD,CURRENTSIZTYPES,yeardate,daydate,monthdateshort)[1]

    print("Превью")

    # for i in range (0,len(CHECKSESSION1)):
    #     form.previewtext.setText("|".join(CHECKSESSION1[i]))
    form.previewtext.setText(fullintro + "\n" + "\n" + session + fullsolution + "\n" + "\n" + lastpartsolution)

def on_click_next():

    print("Вперед")

    party_raw = form.inputtext.toPlainText()
    form.inputtext.setPlainText("")

    if party_raw != "":
        SESSIONHISTORY.append(party_raw)
        with open('JSON/SESSIONHISTORY.json', 'w', encoding="utf-8") as fw:
            json.dump(SESSIONHISTORY, fw, ensure_ascii=False)   

        party = party_normalizer(party_raw.upper())
        
        PARTY_SPLITTED_RAW = party.split(sep="\n") #разделение на строки

        checking(PARTY_SPLITTED_RAW,NUMBERS,ONEOUTLETVALVE,SIZPARTS,SIZTYPES,FILTERSRESIST,
        JOURNALNUMBERS,SOLUTION_GOOD,SOLUTION_BAD,NOT_SO_OLD,SO_OLD,CURRENTSIZTYPES,
        INTRO,CHECKSESSION0,CHECKSESSION1,HISTORYNUMBERS,shortyear,daydate,
        monthdateshort,yeardate)

        form.additionalcounter.setValue(JOURNALNUMBERS["journaladditionalnumber"])
        form.gasmaskcounter.setValue(JOURNALNUMBERS["journalgasmasknumber"])
    
    preview = mini_preview_writer(CHECKSESSION0)

    form.previewtext.setText(preview)

    fromwhere = form.fromwheretext.toPlainText()
    with open('JSON/fromwhere.json', 'w', encoding="utf-8") as fw:
        json.dump(fromwhere, fw, ensure_ascii=False)

    saveall(SOLUTION_BAD,SOLUTION_GOOD,SO_OLD,NOT_SO_OLD,INTRO,
    CHECKSESSION1,CHECKSESSION0,NUMBERS,JOURNALNUMBERS,CURRENTSIZTYPES,
    SESSIONHISTORY,HISTORYNUMBERS)

def on_click_back():
    
    print("Назад")

    if len(SESSIONHISTORY) > 2:
        form.inputtext.setPlainText(SESSIONHISTORY[-2])
        SESSIONHISTORY.pop()
    if len(CHECKSESSION1) > 0: 
        CHECKSESSION1.pop()
    if len(CHECKSESSION0) > 0: 
        CHECKSESSION0.pop()

    with open('JSON/HISTORYNUMBERS.json',  'r', encoding='utf-8') as fr:
        HISTORYNUMBERS = json.load(fr)

    TYPES = HISTORYNUMBERS['typeofsiz']
    ADDITIONAL = HISTORYNUMBERS['additionalnumbers']
    GASMASKS = HISTORYNUMBERS['gasmasknumbers']
        
    if len(TYPES) > 0:
        if len(ADDITIONAL) > 0:
            lastadditionalnumber = ADDITIONAL[-1]
            form.additionalcounter.setValue(JOURNALNUMBERS["journaladditionalnumber"] - lastadditionalnumber)
            HISTORYNUMBERS['additionalnumbers'].pop(-1)
        if len(GASMASKS) > 0:
            lastgasmasksnumber = GASMASKS[-1]
            form.gasmaskcounter.setValue(JOURNALNUMBERS["journalgasmasknumber"] - lastgasmasksnumber)
            HISTORYNUMBERS['gasmasknumbers'].pop(-1)
        HISTORYNUMBERS['typeofsiz'].pop(-1)

    saveall(SOLUTION_BAD,SOLUTION_GOOD,SO_OLD,NOT_SO_OLD,INTRO,CHECKSESSION1,CHECKSESSION0,NUMBERS,JOURNALNUMBERS,CURRENTSIZTYPES,SESSIONHISTORY,HISTORYNUMBERS)

def on_click_generate():

    print("Генерировать")

    fromwhere = form.fromwheretext.toPlainText()
    
    JOURNALNUMBERS["journalactnumber"] = int(JOURNALNUMBERS["journalactnumber"]) + 1
  
    fullintro = intro_generator(SIZTYPES,INTRO,fromwhere)

    fullsolution = solution_generator(SOLUTION_GOOD, SOLUTION_BAD,NOT_SO_OLD,SO_OLD,
    CURRENTSIZTYPES,yeardate,daydate,monthdateshort)[0]

    lastpartsolution = solution_generator(SOLUTION_GOOD, SOLUTION_BAD,NOT_SO_OLD,SO_OLD,
    CURRENTSIZTYPES,yeardate,daydate,monthdateshort)[1]

    docname = ending(JOURNALNUMBERS,daydate,monthdateshort,yeardate,monthdatefull,
    fromwhere,fullintro,fullsolution,lastpartsolution)
    
    DOCNAMES.append(docname)
    with open('JSON/DOCNAMES.json', 'w', encoding="utf-8") as fw:
        json.dump(DOCNAMES, fw, ensure_ascii=False)   

    table_writer(CHECKSESSION0,CHECKSESSION1,docname)
    clear(CHECKSESSION0,CHECKSESSION1,CURRENTSIZTYPES,SOLUTION_BAD,SOLUTION_GOOD,
    INTRO,NUMBERS,SESSIONHISTORY,NOT_SO_OLD,SO_OLD,JOURNALNUMBERS,HISTORYNUMBERS)
    saveall(SOLUTION_BAD,SOLUTION_GOOD,SO_OLD,NOT_SO_OLD,INTRO,
    CHECKSESSION1,CHECKSESSION0,NUMBERS,JOURNALNUMBERS,CURRENTSIZTYPES,
    SESSIONHISTORY,HISTORYNUMBERS)

    form.inputtext.setPlainText("")

    form.actcounter.setValue(JOURNALNUMBERS["journalactnumber"])

def on_click_clear():

    print("Очистить")

    form.inputtext.setPlainText("")
    form.previewtext.setText("")
    clear(CHECKSESSION0,CHECKSESSION1,CURRENTSIZTYPES,SOLUTION_BAD,SOLUTION_GOOD,
    INTRO,NUMBERS,SESSIONHISTORY,NOT_SO_OLD,SO_OLD,JOURNALNUMBERS,HISTORYNUMBERS)

def on_click_turnprotectiontime():
    turnprotectiontime = form.turnprotectiontime.isChecked()
    with open('JSON/turnprotectiontime.json', 'w', encoding="utf-8") as fw:
        json.dump(turnprotectiontime, fw, ensure_ascii=False)   


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



form.checkdate.setDate(QDate(int(yeardate),int(monthdateshort),int(daydate)))
form.calendarWidget.setSelectedDate(QDate(int(yeardate),int(monthdateshort),int(daydate)))
form.gasmaskcounter.setMaximum(9999)
form.additionalcounter.setMaximum(9999)
form.gasmaskcounter.setValue(JOURNALNUMBERS["journalgasmasknumber"])
form.additionalcounter.setValue(JOURNALNUMBERS["journaladditionalnumber"])
form.actcounter.setMaximum(9999)
form.actcounter.setValue(JOURNALNUMBERS["journalactnumber"])
if len(SESSIONHISTORY) > 0:
    form.inputtext.setPlainText(SESSIONHISTORY[-1])

form.gasmaskcounter.valueChanged.connect(journalgasmask_save)
form.additionalcounter.valueChanged.connect(journaladditional_save)
form.actcounter.valueChanged.connect(journalact_save)

form.calendarWidget.clicked.connect(on_click_calendar)
form.checkdate.dateChanged.connect(on_dateedit_change)
	
form.turnprotectiontime.setChecked(turnprotectiontime)
form.turnprotectiontime.stateChanged.connect(on_click_turnprotectiontime)

form.previewbutt.clicked.connect(on_click_preview)
form.backbutt.clicked.connect(on_click_back)
form.nextbutt.clicked.connect(on_click_next)
form.generatebutt.clicked.connect(on_click_generate)
form.clearbutt.clicked.connect(on_click_clear)
form.openbutt.clicked.connect(openact.on_click_openact)
form.fromwheretext.setPlainText(fromwhere)

app.exec_()