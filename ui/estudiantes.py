from funciones.globales import Estado, listado_aspirantes

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
        "estado": Estado.PENDIENTE
      }
  listado_aspirantes.append(camper)
  print(f"{nombre_completo} ha sido añadido a la lista, quieres añadir un estudiante nuevo? S(si) Enter(no)")
  opcion = input("\n>> ").upper()
  if opcion == "S":
    agregar_estudiante()
  else:
    pass

