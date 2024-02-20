import sys
from tabulate import tabulate
from funciones.globales import borrar_pantalla
from .estudiantes import agregar_estudiante

def wrapper(func):
  def inner():
    borrar_pantalla()
    func()
    menu_principal()
  return inner

def menu_principal():
  titulo = """
    ++++++++++++++++++++++++
    +  SISTEMA CAMPUSLAND  +
    ++++++++++++++++++++++++
    """
  print(titulo)
  menu = [["1.","Agregar estudiante"],["2.","Calificar estudiante"],["3.","Registro areas de entrenamiento"],["4.","Registrar nuevas rutas"],["5.","Salir"]]
  print(tabulate(menu,tablefmt="grid"))
  opcion = input("\n>> ")

  if opcion == "1":
    wrapper(menu_agregar_estudiantes())
  elif opcion == "2":
    pass
  elif opcion == "5":
    sys.exit("Vuelva pronto!")
  else:
    menu_principal()

def menu_agregar_estudiantes():
  titulo = """
  ++++++++++++++++++++++++++
  +  REGISTRO ESTUDIANTES  +
  ++++++++++++++++++++++++++
  """
  print(titulo)
  menu = [["1.", "Agregar estudiante"], ["2.", "Eliminar estudiante"], ["3.", "Mostrar listado de estudiantes"], ["4","Salir"]]
  print(tabulate(menu,tablefmt="grid"))
  opcion = input("\n>> ")
  if opcion == "1":
    agregar_estudiante()    
  elif opcion == "4":
    menu_principal()
  else:
    menu_agregar_estudiates()


