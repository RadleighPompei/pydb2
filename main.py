from replit import db

definput = input()


def AddToDataBase():
  name = input("What is your name: ")
  name = name
  db[name] = name


def DeleteTestFromDataBase():
  del db["test"]


def DelNameFromDataBase():
  delname = input("What name do you want to delete: ")
  del db[delname]


def ViewDataBase():
  for key in db.keys():
    print(key)


if definput == "del":
  DelNameFromDataBase()
  ViewDataBase()

if definput == "view":
  ViewDataBase()

if definput == "add":
  AddToDataBase()
  ViewDataBase()

if definput == "test":
  DeleteTestFromDataBase()
  ViewDataBase()

if definput == "":
  while True:
    search = input("search: ")
    print(search)
    print(db.prefix(search))

if definput == "addall":
  db["Cameron"] = "Cameron"
  db["Radleigh"] = "Radleigh"
  db["Samuel"] = "Samuel"
  db["George Pitts"] = "George Pitts"
  db["Zachary"] = "Zachary"
  db["Buddy"] = "Buddy"
  db["Felicity"] = "Felicity"
  db["Mr V"] = "Mr V"
  db["Carl"] = "Carl"
  db["Jay"] = "Jay"
  db["Nathaniel"] = "Nathaniel"
