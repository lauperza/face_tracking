

  SISTEMA DE DETECCIÓN DE MOVIMIENTO DE ROSTRO

[![project.jpg](https://i.postimg.cc/SNBFm1tQ/project.jpg)](https://postimg.cc/56Sk3gVD)

DESCRIPCIÓN

  El proyecto consiste de diseño y construcción de un robot que utiliza una cámara(o tambien un video) mediante OpenCV para detectar rostros humanos. Esta detección de rostros se traduce en movimientos controlados, que son enviados a través de PyFirmata a un Arduino. Este Arduino, a su vez, gestiona dos servomotores SG90 conectados al robot, permitiéndole seguir los movimientos del rostro detectado.

Componentes Principales:

	Detección de Rostro con OpenCV:
    La utilización de OpenCV para la detección facial implica el uso de una cierta configuración que le dira al algoritmo de visión por computadora, que patron identificar, en este caso un rostro de frente( hay muchas opciones más, las puedes encontrar en la carpeta Recursos), luego, se verifica si se encuentra el rostro. Como futuras mejoras, se podria utilizar modelos de aprendizaje profundo que entregan una mayor precisión, y mayor flexibilidad para sus requerimientos.

    Interfaz con PyFirmata:
        PyFirmata es una biblioteca de Python que facilita la comunicación con placas Arduino mediante el protocolo Firmata.
        La interfaz permite enviar comandos desde Python al Arduino, estableciendo una conexión efectiva entre el software de visión por computadora y el hardware de control del robot.

    Control de Movimientos con Arduino:
        El Arduino actúa como el cerebro del sistema, recibiendo datos de Python y traduciéndolos en comandos para los servomotores.
        La programación del Arduino debe incluir la lógica necesaria para interpretar las señales y controlar los servomotores de manera precisa.

    Servomotores SG90:
        Estos servomotores son utilizados para controlar los movimientos mecánicos del robot.
        Son ligeros y eficientes, ideales para aplicaciones de bajo peso como un robot de seguimiento facial.

    Mecánica del Robot:
        Descripción de la estructura mecánica del robot que aloja los servomotores. Esto podría incluir detalles sobre cómo se implementó el sistema de seguimiento facial en términos de conexión mecánica entre los servomotores y las partes móviles del robot.

FUNCIONAMIENTO

Deteccion de rostro : El programa utiliza OpenCV para identificar el rostro, en el que se puede usar distintas configuraciones, el utilizado en este programa y más se encuentran en Recursos. Dependiendo de la configuracion elegida(en este caso, un rostro de frente), se buscara en la imágen, esta se puede obtener a través de una cámara, o en un video pregrabado, si se encuentra el rostr

Conexión con arduino: Se hace uso del módulo pyfirmata. En primer lugar se debe subir el código de configuración de pyfirmata en arduino, que lo encontrarás en la librería de arduino ide, luego, se configura el puerto y pines que se utilizaran en el programa.

Ciclo de imágenes: Se hace uso de un ciclo infinito, en la que se divide el video en las imágenes correspondientes, y se detecta el rostro en cada una, luego las coordenadas del rostro en la imágen, se las entrega a los servos a modo de grados.

MODELOS 3D

Estos modelos fueron diseñados en la plataforma SolidWorks 2023, tanto la parte superior, intermedia e inferior.

La parte inferior hace de base para girar en el eje X a la parte intermedia con uso de los servos g90, luego el servomotor restante es utilizado para mover la parte superior en el eje Y.
