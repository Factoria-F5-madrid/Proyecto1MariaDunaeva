# Taxímetro en Python

## Descripción

Este programa simula un taxímetro. Permite calcular las tarifas de un trayecto basándose en el tiempo que el taxi está parado o en movimiento.  El programa utiliza el módulo `logging` de Python para registrar eventos y facilitar la depuración.

## Características

*   **Cálculo de tarifas:** Calcula la tarifa total basada en el tiempo transcurrido y el estado del taxi (parado o en movimiento).
*   **Interfaz interactiva:**  Permite al usuario simular un trayecto, indicando si el taxi está parado o en movimiento.
*   **Registro de eventos (logging):** Utiliza el módulo `logging` para registrar información, advertencias y errores, facilitando el seguimiento del programa.
*   **Menú principal:** Ofrece opciones para iniciar trayectos y salir del programa, mostrando el total recaudado.

## Fortalezas del código

* **Modularidad:** El código está organizado en funciones bien definidas (mostrar_bienvenida, calcular_tarifa, iniciar_trayecto, main), lo que facilita la lectura, el mantenimiento y la reutilización del código. Cada función tiene una responsabilidad específica.
* **Uso de logging:** La integración del módulo logging permite registrar eventos durante la ejecución del programa, facilitando la depuración y el seguimiento del funcionamiento. Esto es especialmente útil para identificar errores o problemas.
* **Manejo de errores:** El código incluye manejo de errores básicos, como la validación de la entrada del usuario.
* **Legibilidad:** El código está bien comentado, lo que facilita su comprensión. Las variables y las funciones tienen nombres descriptivos.
* **Funcionalidad básica:** El programa cumple con su objetivo principal de simular un taxímetro y calcular tarifas de forma básica.

## Debelidades del código

* **Simulación básica:** La simulación del taxímetro es muy simple. No considera factores reales como el tráfico, las paradas adicionales, diferentes tarifas según la zona, etc.
* **Falta de pruebas unitarias:** No se han incluido pruebas unitarias para verificar el correcto funcionamiento de las funciones. Esto aumenta el riesgo de errores y dificulta la detección de problemas.
* **Manejo de errores limitado:** El manejo de errores es básico. No se manejan excepciones ni se implementan mecanismos más robustos para la gestión de errores.
* **Escalabilidad:** El código no está diseñado para ser escalable. No se considera la posibilidad de gestionar múltiples taxímetros o una gran cantidad de datos.
* **Dependencia del tiempo:** El cálculo de la tarifa se basa en el tiempo real, lo que puede ser impreciso y depender de la velocidad de procesamiento del sistema.
* **Falta de registros:** No se registran los viajes por lo que no se puede hacer comparaciones o reutlizar el mismo trayecto.
* **Seguridad:** No existe ningún sistema de contraseñas para proteger la información.
* **Poca flexibilidad:** Los precios no se pueden adaptar a la demanda.
* **Poca amigabilidad:** El taxímetro carece de una interfaz para interactuar con el usuario.

## Posibles mejoras

* Implementar pruebas unitarias para asegurar la calidad del código.
* Mejorar el manejo de errores, incluyendo la gestión de excepciones.
* Añadir más funcionalidades para hacer la simulación más realista (tráfico, paradas, diferentes tarifas).
* Mejorar la escalabilidad del código.
* Considerar alternativas al uso del tiempo real para el cálculo de tarifas.
* Crear una base de datos para guardar los registros.
* Implementar un sistema de contraseñas.
* Crear un sistema de precios flexibles en función de la demanda.
* Desarrollar una interfaz gráfica para la web y la aplicación móvil.g

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

