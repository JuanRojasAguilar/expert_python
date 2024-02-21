from corefiles import AddData, GetStudent, checkFile

def agregar_estudiante():
  titulo = """
    ++++++++++++++++++++++++
    +  AGREGAR ESTUDIANTE  +
    ++++++++++++++++++++++++
    """
  print(titulo + "\n")
  nombre = input("Por favor, ingresa el nombre: ").title()
  apellido = input("Por favor, ingresa el apellido: ").title()
  nombre_completo = f"{nombre} {apellido}"
  edad = int(input(f"Por favor, ingresa la edad de {nombre}: "))
  direccion = input("Ingresa la dirección: ").upper()
  acudiente = input("Ingresa el nombre del acudiente: ")
  t_estudiante = input("Ingresa el numero de telefono del estudiante: ")
  camper = {
    "nombre": nombre_completo,
    "edad": edad,
    "direccion": direccion,
    "acudiente": acudiente,
    "telefono": t_estudiante,
    "estado": "PENDIENTE"
  }
  checkFile(camper)
  print(f"{nombre_completo} ha sido añadido a la lista, quieres añadir un estudiante nuevo? S(si) Enter(no)")
  opcion = input("\n>> ").upper()
  if opcion == "S":
    agregar_estudiante()
  else:
    pass

def calificar_aspirante():
  titulo = """
    ++++++++++++++++++++++++++
    +  CALIFICAR ASPIRANTES  +
    ++++++++++++++++++++++++++
    """
  print(titulo)
  nombre = input("Ingresa el nombre del estudiante: ").title()
  aspirante = GetStudent(nombre)
  if isinstance(aspirante, dict):
    nota_practica = float(input("Ingresa la nota práctica: "))
    nota_teorica = float(input("Ingresa la nota teórica: "))
    nota = (nota_practica + nota_teorica)/2
    if nota >= 60:
      aspirante["estado"] = "APROBADO"
      input(f'Felicidades, {aspirante["nombre"]} ha sido aprobado para entrar a campusland. Presiona ENTER para volver')
    else:
      input("Lo sentimos, no ha alcanzado la nota necesaria para ser camper")
  else:
    input("No se ha encontrado un aspirante con ese nombre. Pulsa ENTER para volver")
