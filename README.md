

  SISTEMA DE DETECCIÓN DE MOVIMIENTO DE ROSTRO

[![project.jpg](https://i.postimg.cc/SNBFm1tQ/project.jpg)](https://postimg.cc/56Sk3gVD)

DESCRIPCIÓN

  El proyecto consiste de diseño y construcción de un robot que utiliza una cámara(o tambien un video) mediante OpenCV para detectar rostros humanos. Esta detección de rostros se traduce en movimientos controlados, que son enviados a través de PyFirmata a un Arduino. Este Arduino, a su vez, gestiona dos servomotores SG90 conectados al robot, permitiéndole seguir los movimientos del rostro detectado.

Componentes Principales:

	Detección de Rostro con OpenCV:
    Se utiliza OpenCV para la detección facial, este hace uso de algoritmos de visión por computadora que identifican patrones característicos de un rostro.

  Interfaz con PyFirmata:
  	PyFirmata es una biblioteca de Python que facilita la comunicación con placas Arduino mediante el protocolo Firmata. La podras encontrar en Recursos.
  La interfaz permite enviar comandos desde Python al Arduino, estableciendo una conexión efectiva entre el software de visión por computadora y el hardware de control del robot.
		Para poder utilizar PyFirmata correctamente, se debe subir un software de configuracion al Arduino, que sera accesible en ejemplos > StandardFirmata al instalar la libreria.
  
	Control de Movimientos con Arduino:
  	El Arduino actúa como intermediario entre el robot y el programa de deteccion de rostro, recibiendo datos del programa y con el uso de pyfirmata, se traduce y se envian los          valores correpondientes al robot.

  Servomotores SG90:
  	Estos servomotores son utilizados para controlar los movimientos mecánicos del robot tanto la rotacion del robot con respecto a la base, como el movimiento hacia arriba y hacia      abajo de la parte superior. Son ligeros, eficientes, economicos y muy accesibles, caracteristicas ideales para aplicaciones de bajo peso como un robot de seguimiento facial.
	 	A pesar de las ventajas de estos servos, como futuras mejoras desearía utilizar motores paso a paso, o incluso agregar motores para transformar este pequeño proyecto en un brazo     robotico.

FUNCIONAMIENTO

	Deteccion de rostro : 
 		La utilización de OpenCV para la detección facial implica el uso de una cierta configuración que le dira al algoritmo de deteccion de rostro, que patron identificar, en este         caso un rostro de frente(hay muchas opciones más, las puedes encontrar en la carpeta Recursos), luego se verifica si se encuentra el rostro. Como futuras mejoras, pienso en            utilizar modelos de aprendizaje profundo que entregan una mayor precisión, y mayor flexibilidad para mis requerimientos.

	Conexión con arduino: 
		Se hace uso del módulo pyfirmata. En primer lugar se debe subir el código de configuración de pyfirmata en arduino, luego, en el programa se debe elegir el puerto a utilizar y       los pines requeridos.

	Ciclo de imágenes: Se hace uso de un ciclo infinito, en la que se divide el video en las imágenes correspondientes, y se detecta el rostro en cada una, luego las coordenadas del 				rostro en la imágen, se las entrega a los servos a modo de grados.

	MODELOS 3D
		La elección de SolidWorks 2023 es debido a mis conocimientos intermedios en este mismo, ademas de ser una de las herramientas de diseño asistido por computadora (CAD) más            avanzadas y ampliamente utilizadas. Esto asegura la precisión y la eficiencia en el diseño del robot.

    El diseño consta de tres partes principales: superior, intermedia e inferior. La parte inferior sirve como la base del robot y permite la rotacion. Esta base proporciona 						estabilidad al conjunto del robot. La parte intermedia sive como estructura principal del robot, manteniendo todo en su lugar, y sirviendo como referencia para la parte superior, 			que gracias a un servomotor, permite el movimiento vertical en respuesta a las ordenes del programa

		Criterios de diseño:
			Los diseños fueron hechos con la medida standar del sg90, presente en la hoja de datos del mismo, fue construido con una impresora 3D, con base en el material PETG

Conclusiones
	Mis expectativas del proyecto fueron cumplidas con creces, gracias a la implementacion de OpenCV, logre aprender el funcionamiento de este programa e incluso de Inteligencia Artificial
