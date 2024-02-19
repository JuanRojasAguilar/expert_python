import os
import json

MY_DATABASE = "data/camper.json"

def NewFile(*param):
  with open(MY_DATABASE, "w") as wf:
    json.dump(param[0],wf,indent=4)

def checkFile(*param):
  data = list(param)
  if(os.path.isfile(MY_DATABASE)):
    if(len(param)):
      pass
      data[0].update(ReadFile())
    else:
      if(len(param)):}
        NewFile(data[0])

def AddDate(*param):
  with open(MY_DATABASE, "r+") as rwf:
  data_file = json.load(rwf)
  if (len(param)>1):
    data_file[param[0]].update(param[1])
  else:
    data_file.update({param[0]}
  rwf.seek(0)
  json.dump(data_file,rwf,indent=4)
  rwf.close()
