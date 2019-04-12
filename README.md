# Python-Simulation
This project will consist of using python programming language in order to control a simulator to display led animation. The advantage of using a simulator is that the programmer does not have any hardware restriction. 

The whole project was written using Python 3.7.3. in order as well to generate the animation, various library has been used. The library used are as stated below;

•	Opc.py

•	Time.py

•	Random.py

•	Nanpy

-------------------------------------------------------------------------------------------------------------------------------------------
OPC.py:
--------
This a library that will allow the code to have access to the led device. Since the project will use simulator to display the led animation. The user has to specify where to run it like shown below:

client = opc.Client('localhost:7890')

Time.py:
--------
In this project we have imported the library for time in order to control the time sleep between the led animations.

Like in this section of the code, we have set the time to a function call time.sleep().

time.sleep(0.08)

Random.py:
----------
Random function is used to be able to generate different RGB colour codes to obtain different led colours during the animations.

red = random.randint(0,256)

green = random.randint(0,256)

blue = random.randint(0,256)

random.randint followed by integers in the brackets. The integer used in the bracket is 0 to 256. These are integer are for RGB value and random will generate a value between this 0 to 255 range as the final value in not taken into account

Nanpy:
------
This library allows the Arduino to act as slave. This would imply that the Arduino will only read the data from the python IDLE. This will also allow communication between the pc and the Arduino. This library is used to allow the microphone to communicate. 
The following code is implemented to communicate with the Arduino from the python IDLE using SerialManager(‘COM6’). COM6 is the port used for Arduino.

The sound sensor is connected to pin 8 on the Arduino.

connection = SerialManager('COM6')

a = ArduinoApi (connection=connection)

soundSensor = 8

a.pinMode(soundSensor, a.INPUT)

-------------------------------------------------------------------------------------------------------------------------------------------
Exception handling and verification
-----------------------------------
In order to avoid a program from crashing, an exception handling and try except are used, along with KeyboardInterrupt Exception.
This will read the user input from the keyboard and will cancel the animation.

As soon as the program is stopped, the menu will show up again. In order for this to happen, the continue function is added. This will keep the program to run again and again until the user decides to exit.

To verify if the user has input a numeric value, the if else has a section where it will verify on the input, if the input is not a numeric value, it will display a message and will prompt the user to input a new value.

-------------------------------------------------------------------------------------------------------------------------------------------

How to run:
-----------
1. Download folder and extract.
2. Open Python IDLE and choose 'Open...' in File menu and choose \Python Simulation\Python code\Coursework.py
3. In Python Simulation folder, open readopcForStrands shortcut.
4. Run python code and click on the simulator.
5. The 'WELCOME' message will appear and then the menu.
6. Different options contains different animations.



