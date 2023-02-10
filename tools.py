def datetofull(monthdateshort):
   if monthdateshort == "01":
      monthdatefull = "января"
   if monthdateshort == "02":
      monthdatefull = "февраля"
   if monthdateshort == "03":
      monthdatefull = "марта"
   if monthdateshort == "04":
      monthdatefull = "апреля"  
   if monthdateshort == "05":
      monthdatefull = "мая"
   if monthdateshort == "06":
      monthdatefull = "июня"
   if monthdateshort == "07":
      monthdatefull = "июля"
   if monthdateshort == "08":
      monthdatefull = "августа"
   if monthdateshort == "09":
      monthdatefull = "сентября"
   if monthdateshort == "10":
      monthdatefull = "октября"
   if monthdateshort == "11":
      monthdatefull = "ноября"
   if monthdateshort == "12":
      monthdatefull = "декабря"
   return(monthdatefull)

def dict_to_solution(dict):
   listkeys = list(dict.keys())

   for i in range(0, len(listkeys)):
      
      key = listkeys[i]

      listsiz = dict[key]

      if dict[key][0] != " партии № " and dict[key][0] != " партий № ":
         if len(listsiz) > 1:
            dict[key].insert(0," партий № ")
         else:
            dict[key].insert(0," партии № ")


   items = dict.items()

   items = str(items)

   items = items.replace("'","")
   items = items.replace("dict_items(","")


   items = items.replace(", [","")


   items = items.replace("[(","")
   items = items.replace("])","")
   items = items.replace(", (","; ")
   items = items.replace("№ ,","№")



   return(items)

def nearest(lst, target):
  return min(lst, key=lambda x: abs(x-target))