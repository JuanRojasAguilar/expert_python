from os import system
import sys
from enum import Enum

def borrar_pantalla():
  if sys.platform == "linux" or sys.platform == "darwin":
    system("clear")
  else:
    system("cls")

listado_rutas = {
  "java": {
    "fundamentos": {},
    "web": {},
    "programacion": {},
    "databases": {},
    "backend": {}
  },
}
