# Antipatrones

Click [aquí](https://github.com/ESTHERRODRIGUEZGARCIA/Antipatrones.git) para ver el enlace del repositorio.

Trabajo hecho por:
1. [Esther Rodríguez García](https://github.com/ESTHERRODRIGUEZGARCIA)

- Identificación de características de "Spaghetti Code":

Falta de modularización: La función calcular tiene múltiples responsabilidades (decidir la operación, realizar la operación y manejar errores), lo que dificulta la comprensión y el mantenimiento del código.

Uso de cadenas de texto para la lógica de control: La elección de operaciones se realiza mediante comparaciones de cadenas (operacion == 'suma'), lo cual es propenso a errores y hace que el código sea menos robusto.

Falta de manejo de errores consistente: Aunque hay un manejo de error para la división por cero, no hay una estructura coherente para manejar otros casos, y se utiliza la impresión directa en lugar de lanzar excepciones.



- Justificación de cambios:

Modularización: Se han creado funciones separadas para cada operación, siguiendo el principio de "una función, una responsabilidad". Esto mejora la legibilidad y facilita la comprensión y el mantenimiento del código.

Eliminación de lógica de control basada en cadenas de texto: Se han reemplazado las cadenas de texto con llamadas directas a funciones, lo que hace que el código sea más robusto y menos propenso a errores.

Mejora del manejo de errores: Se ha utilizado el lanzamiento de excepciones en lugar de imprimir mensajes directamente. Esto proporciona un manejo más consistente y permite a los usuarios del código manejar los errores de manera más efectiva.
