<p align="center">
  <img width="200" height="200" src="https://github.com/rohan-bhautoo/Python-Simulation/blob/master/Screenshots/Daco_4428823.png">
</p>
<h1 align="center">Python Simulation</h1>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-1.2.0-brightgreen.svg" />
  <img alt="Python" src="https://img.shields.io/badge/Python_>=3.7.2-3776AB?logo=python&logoColor=white" />
  <img alt="Arduino" src="https://img.shields.io/badge/Arduino-038C8C?logo=arduino&logoColor=white" />
</p>

## Description
> This project consists of controlling a simulator called *readopcForStrands* to display led animation by using Python.
> 
> See other images of the project in the [Screenshot](/Screenshots) folder.

### 🏠 [Homepage](/Python%20Simulation/Python%20code/Coursework.py)
<p align="center">
  <img width="600" src="https://github.com/rohan-bhautoo/Python-Simulation/blob/master/Screenshots/welcome_animation.png">
</p>

> A menu will then be displayed on the Shell command prompt to allow the user to select different animations.
<p align="center">
  <img src="https://github.com/rohan-bhautoo/Python-Simulation/blob/master/Screenshots/Menu.png">
</p>

## Prerequisite

### IDLE Python
> Python is a programming language that lets you work more quickly and integrate your systems more effectively. Download it [here](https://www.python.org/downloads/).

### Arduino UNO R3 Board
> Arduino Uno is a microcontroller board based on the ATmega328P (datasheet). It has 14 digital input/output pins (of which 6 can be used as PWM outputs), 6 analog inputs, a 16 MHz ceramic resonator (CSTCE16M0V53-R0), a USB connection, a power jack, an ICSP header and a reset button. Buy it [here](https://store.arduino.cc/products/arduino-uno-rev3/).

### Breadboard
> A breadboard is a solderless construction base used for developing an electronic circuit and wiring for projects with microcontroller boards. Buy it [here](https://www.aliexpress.com/item/32845516827.html?aff_fcid=0810a3482d99482cb204845fdf406717-1644774917577-09852&aff_fsk&aff_platform=api-new-product-detail&sk&aff_trace_key=0810a3482d99482cb204845fdf406717-1644774917577-09852&terminal_id=ba6fbd5591524f96930b577c93b7f7fa).

### Microphone Sound Sensor
> The Microphone Sound Sensor will be used to detech sound and display random animation on the simulator based on the sound intensity. Buy it [here](https://www.amazon.com/dp/B0173OAWE4?tag=makeradvisor-20&linkCode=ogi&th=1&psc=1).

## Libraries
> A library is a set of method and function that is declared at the beginning of the program, this will prevent the programmer from writing long section of codes. Below is how different libraries were implemented in this project.
```python
import opc
import time
import random
from nanpy import ArduinoApi
from nanpy import SerialManager
```

### OPC.py
> OPC.py library allows the python code to have access to the LED simulator to display the animation. It will also act as the local server host.
```python
client = opc.Client('localhost:7890')
```

### Time.py
> The Time library is used in order to control the time sleep between the LED animations.
```python
led_coulour[181] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_coulour[240] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_coulour[241] = colour
time.sleep(0.08)
client.put_pixels(led_colour)
```

### Random.py
> Random function is used to be able to generate different RGB colour codes to obtain different led colours during the animations.
```python
red = random.randint(0,256)
green = random.randint(0,256)
blue = random.randint(0,256)
colour = (red,green,blue)
```
> *random.randint* followed by integers in the brackets. The integer used in the bracket is 0 to 256. These are integer are for RGB value and random will generate a value between this 0 to 255 range as the final value in not taken into account
<p align="center">
  <img height="300" src="https://github.com/rohan-bhautoo/Python-Simulation/blob/master/Screenshots/random_animation.png">
</p>

### Nanpy.py
> Nanpy is a library that use your Arduino as a slave, controlled by a master device where you run your scripts, such as a PC, a Raspberry Pi etc. This would imply that the Arduino will only read the data from the python IDLE. Nanpy will allow communication between the PC, Arduino and Mircrophone sensor.
```sh
pip install nanpy
```

> The following code is implemented to communicate with the Arduino from the python IDLE using SerialManager(‘COM6’). COM6 is the port used for Arduino.
> 
> The sound sensor is connected to pin 8 on the Arduino.

```python
connection = SerialManager('COM6')
a = ArduinoApi (connection=connection)
soundSensor = 8
a.pinMode(soundSensor, a.INPUT)

#reading values from sound sensor
SensorData = a.digitalRead(soundSensor)
print(SensorData)

led_colour1=[(255,0,0)]*360
led_colour2=[(0,0,0)]*360

#condition for intensity of SensorData
if(SensorData == 0):
  client.put_pixels(led_colour1)
elif(SensorData == 1):
  client.put_pixels(led_colour2)
```

## Exception handling and verification
> In order to avoid a program from crashing, an exception handling and try except are used, along with KeyboardInterrupt Exception. This will read the user input from the keyboard and will cancel the animation. As soon as the program is stopped, the menu will show up again. In order for this to happen, the continue function is added. This will keep the program to run again and again until the user decides to exit.
<p align="center">
  <img height="300" src="https://github.com/rohan-bhautoo/Python-Simulation/blob/master/Screenshots/keyboard_interrupt_exception.png">
</p>

> To verify if the user has input a numeric value, the if else has a section where it will verify on the input, if the input is not a numeric value, it will display a message and will prompt the user to input a new value.
<p align="center">
  <img height="300" src="https://github.com/rohan-bhautoo/Python-Simulation/blob/master/Screenshots/non_numeric_exception.png">
</p>

> Conditional staments was used to check if the option entered by the user, in the Menu, is a valid one. If not, then the program will return an error and the menu will be displayed again.
<p align="center">
  <img height="300" src="https://github.com/rohan-bhautoo/Python-Simulation/blob/master/Screenshots/menu_validation.png">
</p>

## Arduino Connection
<p align="center">
  <img width="600" src="https://github.com/rohan-bhautoo/Python-Simulation/blob/master/Screenshots/arduino_connection.png">
</p>

## Usage
> 1 - Open Python IDLE 
> 2 - From the File setting, open the \Python Simulation\Python code\Coursework.py file.
> 3 - Run the /Python Simulation/simulator/bin/windows64/readopcForStrands.exe.
> 4 - Run python code and view the python simulator.
> 5 - The WELCOME animation will appear.

## Author

👤 **Rohan Bhautoo**

* Github: [@rohan-bhautoo](https://github.com/rohan-bhautoo)
* LinkedIn: [@rohan-bhautoo](https://linkedin.com/in/rohan-bhautoo)

## Show your support

Give a ⭐️ if this project helped you!
