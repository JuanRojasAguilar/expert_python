import os
import json

MY_DATABASE = "data/campus.json"

def NewFile(*param):
  with open(MY_DATABASE, "w") as file:
    json.dump(param[0],file,indent=4)

def ReadFile():
  with open(MY_DATABASE, "r") as file:
    return json.load(file)

def checkFile(*param):
  data = list(param[0])
  if(os.path.isfile(MY_DATABASE)):
    if(len(param)):
      data.update(data)
    else:
      NewFile(data)

def AddData(*param):
  with open(MY_DATABASE, "r+") as rwf:
    data_file = json.load(rwf)
  if (len(param)>1):
    data_file[param[0]].update(param[1])
  else:
    data_file.update({param[0]})
  rwf.seek(0)
  json.dump(data_file,rwf,indent=4)
  rwf.close()

def GetStudent(nombre:str)->dict:
  listado = ReadFile()
  for estudiante in listado.values():
    if estudiante["nombre"] == nombre:
      return estudiante
    break
