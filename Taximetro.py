import logging
import time

logging.basicConfig(
    level=logging.DEBUG,  # Nivel de logging (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format='%(asctime)s - %(levelname)s - %(message)s',  # Formato del mensaje
    filename='mi_log.log',  # Archivo donde se guardarán los logs
    filemode='a'  # Modo de apertura del archivo ('a' para agregar, 'w' para sobrescribir)
)
"""
DEBUG: Información detallada, típicamente de interés solo para desarrolladores.
INFO: Confirmación de que las cosas están funcionando como se esperaba.
WARNING: Indica que algo inesperado ocurrió, o que hay un problema en el futuro (por ejemplo, ‘poco espacio en disco’).
ERROR: Debido a un problema más serio, el software no ha podido realizar una función.
CRITICAL: Un error muy grave, que puede impedir que el programa continúe ejecutándose.
"""


def mostrar_bienvenida():
    #Muestra un mensaje de bienvenida y explica el funcionamiento del programa.
    logging.info("Mostrando mensaje de bienvenida.")  # Registro de información
    print("¡Bienvenido a nuestro Taxímetro! 🚕")
    print("-" * 30)
    #Imprime una línea de guiones
    print("Este programa simula un taxímetro.")
    print("Puedes calcular las tarifas de tu trayecto.")
    print("Las tarifas son:")
    print(" - Parado: 0,02 euros por segundo")
    print(" - En movimiento: 0,05 euros por segundo")
    print("-" * 30)
    logging.debug("Mensaje de bienvenida mostrado correctamente.")  # Registro de depuración

def calcular_tarifa(tiempo_segundos, en_movimiento):
    #Calcula la tarifa en base del tiempo y el estado
    logging.debug(f"Calculando tarifa. Tiempo: {tiempo_segundos}, En movimiento: {en_movimiento}")  # Registro de depuración
    if en_movimiento:
        tarifa_por_segundo = 0.05
    else: 
        tarifa_por_segundo = 0.02
    tarifa_total = tiempo_segundos * tarifa_por_segundo
    logging.debug(f"Tarifa calculada: {tarifa_total}")  # Registro de depuración
    return tarifa_total

def iniciar_trayecto():
    #Inicia un trayecto y calcula la tarifa
    tiempo_inicio = time.time()
    #Guardamos la hora del inicio en la variable
    en_movimiento = False #Al principio, el taxi está parado
    tarifa_acumulada = 0
    logging.info("Trayecto iniciado.")  # Registro de información

    while True:
        estado = input ("¿El taxi está (P)arado o en (M)ovimiento? (o 'f' para finalizar): ").upper()
        #.upper convierte las letras introducidas en mayúsculas
        logging.debug(f"Estado introducido: {estado}")  # Registro de depuración
        
        if estado == 'F':
            tiempo_transcurrido == time.time() - tiempo_inicio
            tarifa_acumulada += calcular_tarifa(tiempo_transcurrido, en_movimiento)
            print(f"Trayecto finalizado. Tarifa total: {tarifa_acumulada:.2f} euros")
            # .2f formatea el valor de la variable tarifa_acumulada para que se muestre con dos dígitos decimales. 
            logging.info(f"Trayecto finalizado. Tarifa total: {tarifa_acumulada:.2f} euros")  # Registro de información
            return tarifa_acumulada
        
        if estado == 'P':
            en_movimiento = False
            tiempo_transcurrido == time.time() - tiempo_inicio
            tarifa_acumulada += calcular_tarifa(tiempo_transcurrido, en_movimiento)
            tiempo_inicio = time.time() #Reiniciar el tiempo de inicio para la tarifa parada
            print(f"Taxi parado. Tarifa acumulada: {tarifa_acumulada: .2f} euros")
            logging.info(f"Taxi parado. Tarifa acumulada: {tarifa_acumulada:.2f} euros")  # Registro de información
        
        elif estado == 'M':
            en_movimiento = True
            tiempo_transcurrido = time.time() - tiempo_inicio
            tarifa_acumulada += calcular_tarifa(tiempo_transcurrido, en_movimiento)
            tiempo_inicio = time.time() #Reiniciar el tiempo de inicio para la tarifa en movimniento
            print(f"Taxi en movimiento. Tarifa acumulada: {tarifa_acumulada:.2f} euros")
            logging.info(f"Taxi en movimiento. Tarifa acumulada: {tarifa_acumulada:.2f} euros")  # Registro de información
        
        else:
            print("Opción inválida. Por favor, introduce 'P', 'M' o 'f'.")
            logging.warning("Opción inválida en el estado del taxi.")  # Registro de advertencia

def main():
    #Función principal que controla el flujo del programa
    logging.info("Iniciando la función main().")  # Registro de información
    mostrar_bienvenida()
    total_recaudado = 0

    while True:
        opcion = input("¿Qué deseas hacer? (I)niciar trayecto, (S)alir: ").upper()
        logging.debug(f"Opción seleccionada en el menú principal: {opcion}")  # Registro de depuración

        if opcion == 'I':
            total_trayecto = iniciar_trayecto()
            total_recaudado += total_trayecto
            logging.info(f"Trayecto iniciado. Total recaudado hasta ahora: {total_recaudado:.2f} euros")  # Registro de información
        elif opcion == 'S':
            print(f"Total recaudado hoy: {total_recaudado: .2f} euros")
            print("¡Gracias por usar nuestro Taxímetro!")
            logging.info(f"Saliendo del programa. Total recaudado: {total_recaudado:.2f} euros")  # Registro de información
            break
        else:
            logging.warning("Opción inválida en el menú principal.")  # Registro de advertencia
    logging.info("Finalizando la función main().")  # Registro de información

if __name__ == "__main__":
    main()


