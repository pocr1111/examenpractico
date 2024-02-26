import os

def crear_carpeta(nombre_carpeta):
    try:
        os.makedirs(nombre_carpeta, exist_ok=True)
    except FileExistsError:
        pass

def crear_carpetas_y_ficheros():
    for i in range(1, 6):
        nombre_carpeta = f"folder{i}"
        crear_carpeta(nombre_carpeta)

        for j in range(1, 11):
            nombre_fichero = f"{nombre_carpeta}/fichero{j}.txt"
            contenido = f"Este es el contenido del fichero {j}"

            with open(nombre_fichero, 'w') as archivo:
                archivo.write(contenido)

def main():
    for _ in range(5):
        crear_carpetas_y_ficheros()

if __name__ == "__main__":
    main()

