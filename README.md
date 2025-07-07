# 🚕 Proyecto Python: Taxímetro Digital
![Taxímetro](image.png)

## 📋Enlace al tablero Kanban´

https://trello.com/b/0iNvlW2o/proyecto-taximetro

## 📝Descripción para público no técnico

**¿Cansado de calcular tarifas de taxi manualmente? ¡Nuestro Taxímetro digital es la solución!**

Imagina un sistema sencillo e intuitivo que calcula automáticamente las tarifas de tus viajes en taxi, ¡sin errores ni complicaciones! Simplemente indica si el taxi está parado o en movimiento y las tarifas que se están aplicando, y el programa calcula la tarifa total en base al tiempo transcurrido.

**¿Cómo funciona?**

Es muy fácil de usar. El programa te guiará paso a paso, preguntándote si el taxi está parado o en movimiento. Se basa en tarifas por segundo: una tarifa para cuando el taxi está parado y otra para cuando está en movimiento. Las puedes introducir tú mismo pero también hay unas por defecto. Al finalizar el viaje, el programa te mostrará la tarifa total. 

**Beneficios Clave:**

*  **Precisión:** Olvídate de los cálculos manuales y los errores. ¡Nuestro Taxímetro digital garantiza la precisión en cada tarifa!
*  **Eficiencia:** Calcula las tarifas en segundos, ahorrándote tiempo y esfuerzo.
*  **Fácil de usar:** Su interfaz intuitiva hace que sea accesible para cualquier persona, sin necesidad de conocimientos técnicos.

**¡Nuestro Taxímetro digital es la herramienta perfecta para cualquier taxista que busca optimizar su negocio y mejorar su eficiencia!**

## Descripción técnica

Este programa simula un taxímetro. Permite calcular las tarifas de un trayecto basándose en el tiempo que el taxi está parado o en movimiento.  El programa utiliza el módulo `logging` de Python para registrar eventos y facilitar la depuración.

## Características

*   **Cálculo de tarifas:** Calcula la tarifa total basada en el tiempo transcurrido y el estado del taxi (parado o en movimiento). El usuario puede introducir las tarifas o usar las que están establecidas por defecto.
*   **Interfaz interactiva:**  Permite al usuario simular un trayecto, indicando si el taxi está parado o en movimiento y qué tarifas se deben aplicar.
*   **Registro de eventos (logging):** Utiliza el módulo `logging` para registrar información, advertencias y errores, facilitando el seguimiento del programa.
*   **Menú principal:** Ofrece opciones para iniciar trayectos y salir del programa, mostrando el total recaudado.

## Fortalezas del código

* **Modularidad:** El código está organizado en funciones bien definidas (mostrar_bienvenida, configurar_tarifas, calcular_tarifa, guardar_en_historial, iniciar_trayecto, main), lo que facilita la lectura, el mantenimiento y la reutilización del código. Cada función tiene una responsabilidad específica.
* **Uso de logging:** La integración del módulo logging permite registrar eventos durante la ejecución del programa, facilitando la depuración y el seguimiento del funcionamiento. Esto es especialmente útil para identificar errores o problemas.
* **Manejo de errores:** El código incluye manejo de errores básicos, como la validación de la entrada del usuario.
* **Legibilidad:** El código está bien comentado, lo que facilita su comprensión. Las variables y las funciones tienen nombres descriptivos.
* **Funcionalidad básica:** El programa cumple con su objetivo principal de simular un taxímetro y calcular tarifas de forma básica.
* **Historial de registros:** Se registran los viajes para poder hacer comparaciones.
* **Flexibilidad:** Las tarifas pueden cambiar en función de la demanda.

## Debelidades del código

* **Simulación básica:** La simulación del taxímetro es muy simple. No considera factores reales como el tráfico, las paradas adicionales, diferentes tarifas según la zona, etc.
* **Manejo de errores limitado:** El manejo de errores es básico. Las excepciones se manejan solo en el historial y el cálculo de tarifas.
* **Escalabilidad:** El código no está diseñado para ser escalable. No se considera la posibilidad de gestionar múltiples taxímetros o una gran cantidad de datos.
* **Dependencia del tiempo:** El cálculo de la tarifa se basa en el tiempo real, lo que puede ser impreciso ya que depende de la velocidad de procesamiento del sistema.
* **Seguridad:** No existe ningún sistema de contraseñas para proteger la información.
* **Poca amigabilidad:** El taxímetro carece de una interfaz para interactuar con el usuario.

## Posibles mejoras

* Mejorar el manejo de errores, incluyendo la gestión de excepciones.
* Añadir más funcionalidades para hacer la simulación más realista (tráfico, paradas, diferentes tarifas).
* Mejorar la escalabilidad del código.
* Considerar alternativas al uso del tiempo real para el cálculo de tarifas.
* Crear una base de datos para guardar los registros.
* Implementar un sistema de contraseñas.
* Desarrollar una interfaz gráfica para la web y la aplicación móvil.

## Requisitos

*   Python 3.x

## Instalación

1.  **Clona el repositorio:**
    ```bash
    git clone git@github.com:Factoria-F5-madrid/Proyecto1MariaDunaeva.git
    ```

2.  **No se requiere ninguna instalación adicional de paquetes**, ya que el programa utiliza únicamente la biblioteca estándar de Python.

## Uso

1.  **Ejecuta el programa:**
    ```bash
    python taximetro.py
    ```

2.  **Sigue las instrucciones en pantalla:**
    *   El programa mostrará un mensaje de bienvenida.
    *   En el menú principal, selecciona "I" para iniciar un trayecto o "S" para salir.
    *   Durante un trayecto, introduce "P" para indicar que el taxi está parado, "M" para indicar que está en movimiento, o "f" para finalizar el trayecto.
    *   El programa mostrará la tarifa acumulada en cada paso y el total recaudado al finalizar.

## Autor

*   María Dunaeva

## Licencia

Este proyecto está bajo la licencia [MIT](https://opensource.org/licenses/MIT).

## Contacto

Si tienes alguna pregunta, sugerencia o quieres contactar al autor, puedes hacerlo a través de:

*   mdunaeva308@gmail.com
*   https://github.com/MariaDunaeva1

## Agradecimientos

Agradecemos a todos los que contribuyeron a este proyecto, ya sea reportando errores, sugiriendo mejoras o simplemente utilizando el programa.

## Notas

*   El programa está diseñado para ser una simulación básica de un taxímetro y no está destinado a uso comercial real.
*   Los precios y la lógica de cálculo de tarifas son ejemplos y pueden ser modificados según sea necesario.
*   Se recomienda revisar el archivo `mi_log.log` para obtener información detallada sobre el funcionamiento del programa y para la depuración.

---

**¡Disfruta usando el taxímetro!**

