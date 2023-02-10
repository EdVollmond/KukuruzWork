

def party_normalizer(text):
    text = text.replace("ШМ-62У", "ШМ-62у")
    text = text.replace("ШМ-66МУ", "ШМ-66Му")
    text = text.replace("@", "Ф")
    text = text.replace("#", "Т")
    text = text.replace("&amp;", "С")
    text = text.replace("₽", "М")
    text = text.replace("*", "Я")
    text = text.replace("?", "О")
    text = text.replace("Y", "У")
    text = text.replace("C", "С")
    text = text.replace("M", "М")
    text = text.replace("O", "О")
    text = text.replace("T", "Т")
    text = text.replace("N", "№")
    text = text.replace("ПАРТИЯ", "Партия")
    return (text)

def yearofmask_normalizer(text):
    text = text.replace("Т","")
    text = text.replace("Я","")
    text = text.replace("С","")
    text = text.replace("М","")
    text = text.replace("О","")
    return (text)

def markoffilter_normalizer(text):
    text = text.replace("IV","4")
    text = text.replace("III","3")
    text = text.replace("II","2")
    text = text.replace("I","1")
    return (text)

def quartalofparty_normalizer(text):
    quartalofparty = quartalofparty.replace("янв","01")
    quartalofparty = quartalofparty.replace("фев","02")
    quartalofparty = quartalofparty.replace("мар","03")
    quartalofparty = quartalofparty.replace("апр","04")
    quartalofparty = quartalofparty.replace("май","05")
    quartalofparty = quartalofparty.replace("мая","05")
    quartalofparty = quartalofparty.replace("июн","06")
    quartalofparty = quartalofparty.replace("июн","07")
    quartalofparty = quartalofparty.replace("авг","08")
    quartalofparty = quartalofparty.replace("сен","09")
    quartalofparty = quartalofparty.replace("окт","10")
    quartalofparty = quartalofparty.replace("ноя","11")
    return(text)
