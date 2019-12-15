from tinydb import TinyDB, Query
db = TinyDB('db.json')
#db.insert({'type': 'apple', 'count': 7})
#db.insert({'type': 'peach', 'count': 3})
t = db.all()
print (t)
#for item in db:
#    print(item)

#Fruit = Query()
#o = db.search(Fruit.type == 'peach')
#print (o)