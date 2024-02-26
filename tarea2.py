import psutil


def obtener_porcentaje_espacio(particion):
    espacio = psutil.disk_usage(particion.mountpoint)
    porcentaje_ocupado = espacio.percent
    return porcentaje_ocupado

def mostrar_porcentajes():
    particiones = psutil.disk_partitions(all=True)
    print("Porcentaje de espacio ocupado en cada partición:")

    for particion in particiones:
        if particion.fstype and particion.device.startswith('/dev/'):
            porcentaje = obtener_porcentaje_espacio(particion)
            print(f"{particion.device} {porcentaje:.1f}%")

if __name__ == "__main__":
    mostrar_porcentajes()

