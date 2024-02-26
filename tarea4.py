import logging
import psutil

# Configurar el sistema de logging
logging.basicConfig(filename='/home/juan/logs/espacio.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s: %(message)s')

def analizar_espacio():
    # Obtener información sobre el espacio en la partición raíz
    disk_info = psutil.disk_usage("/")

    # Calcular el porcentaje de espacio utilizado
    percentage_used = disk_info.percent

    # Definir umbrales
    error_threshold = 80
    warning_threshold = 60

    # Analizar el espacio y generar mensajes de logging
    if percentage_used > error_threshold:
        logging.error(f"Espacio ocupado superior al {error_threshold}% - ¡Intervención necesaria!")
    elif percentage_used > warning_threshold:
        logging.warning(f"Espacio ocupado superior al {warning_threshold}% - Se recomienda revisar el espacio disponible.")
    else:
        logging.info(f"Espacio ocupado: {percentage_used:.2f}% - Todo en orden.")

# Llamada a la función por si se ejecuta el script directamente
if __name__ == "__main__":
    analizar_espacio()

