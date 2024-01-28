

SISTEMA DE DETECCIÓN DE MOVIMIENTO DE ROSTRO

DESCRIPCIÓN

Este proyecto consta de un programa que detecta el rostro con uso de OpenCV, y con esa información, mueve unos servomotores sg90.

FUNCIONAMIENTO

Deteccion de rostro : El programa utiliza OpenCV para identificar el rostro, a través de una cámara, o en un video pregrabado.

Conexión con arduino: Se hace uso del módulo pyfirmata. En primer lugar se debe subir el código de configuración de pyfirmata en arduino, que lo encontrarás en la librería de arduino ide, luego, se configura el puerto y pines que se utilizaran en el programa.

Ciclo de imágenes: Se hace uso de un ciclo infinito, en la que se divide el video en las imágenes correspondientes, y se detecta el rostro en cada una, luego las coordenadas del rostro en la imágen, se las entrega a los servos a modo de grados.

MODELOS 3D

Estos modelos fueron diseñados en la plataforma SolidWorks 2023, tanto la parte superior, intermedia e inferior.

La parte inferior hace de base para girar en el eje X a la parte intermedia con uso de los servos g90, luego el servomotor restante es utilizado para mover la parte superior en el eje Y.
