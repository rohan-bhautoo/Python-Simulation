#!/usr/bin/env python

import opc
import time
import random
from nanpy import ArduinoApi
from nanpy import SerialManager

#Declaration of led RGB code
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
Aqua = (0,255,255)
violet = (255,0,255)
white = (255,255,255)
black = (0,0,0)
    
red_random = random.randint(0,256)
green_random = random.randint(0,256)
blue_random = random.randint(0,256)
colour = (red_random,green_random,blue_random)

client = opc.Client('localhost:7890')

connection = SerialManager('COM6')    
a = ArduinoApi(connection=connection)

soundSensor = 8
a.pinMode(soundSensor, a.INPUT)

#Declaration of black screen
led_colour = [(black)]*360

client.put_pixels(led_colour)

#W display
led_colour[0] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[1] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[60] = colour
time.sleep(0.08)
client.put_pixels(led_colour)
led_colour[61] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[120] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[121] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[180] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[181] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[240] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[241] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[300] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[301] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[243] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[245] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[184] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[307] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[308] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[247] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[248] = colour
time.sleep(0.08)
led_colour[187] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[188] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[127] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[128] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[67] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[68] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[7] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[8] = colour
time.sleep(0.08)
client.put_pixels(led_colour)


#E display
led_colour[10] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[11] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[12] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[13] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[14] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[15] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[16] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[17] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[70] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[71] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[130] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[131] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[132] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[133] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[134] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[190] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[191] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[192] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[193] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[194] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[250] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[251] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[310] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[311] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[312] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[313] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[314] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[315] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[316] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[317] = colour
time.sleep(0.08)
client.put_pixels(led_colour)


#L display
led_colour[19] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[20] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[79] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[80] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[139] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[140] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[199] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[200] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[259] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[260] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[319] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[320] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[321] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[322] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[323] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[324] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[325] = colour
time.sleep(0.08)
client.put_pixels(led_colour)


#C display
led_colour[27] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[28] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[29] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[30] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[31] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[32] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[33] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[87] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[88] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[147] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[148] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[207] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[208] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[267] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[268] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[327] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[328] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[329] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[330] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[331] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[332] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[333] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

#O display
led_colour[35] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[36] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[37] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[38] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[39] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[40] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[41] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[95] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[96] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[100] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[101] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[155] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[156] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[160] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[161] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[215] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[216] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[220] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[221] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[275] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[276] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[280] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[281] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[335] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[336] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[337] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[338] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[339] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[340] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[341] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

#M display
led_colour[43] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[44] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[50] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[51] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[103] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[104] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[106] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[108] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[110] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[111] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[163] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[164] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[167] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[170] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[171] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[223] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[224] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[230] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[231] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[283] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[284] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[290] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[291] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[343] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[344] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[350] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[351] = colour
time.sleep(0.08)
client.put_pixels(led_colour)


#E display
led_colour[53] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[54] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[55] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[56] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[57] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[58] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[59] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[113] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[114] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[173] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[174] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[175] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[176] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[177] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[233] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[234] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[235] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[236] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[237] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[293] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[294] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[353] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[354] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[355] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[356] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[357] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[358] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

led_colour[359] = colour
time.sleep(0.08)
client.put_pixels(led_colour)

while True :
    #Menu option
    print("Select one option:\n1. Turn On Leds.\n2. Random Colours.\n3. Light Change.\n4. Random Row.\n5. Animation with sensor\n6. Exit.")
    Option = input("Option: ")
    
    if Option == '1':

        #RGB code
        red = (255,0,0)
        green = (0,255,0)
        blue = (0,0,255)
        Aqua = (0,255,255)
        violet = (255,0,255)
        white = (255,255,255)
        black = (0,0,0)
        
        print("Turning On LEDs...\nPress CTRL + C to exit.")
        try:
            while True:
                led_colour = [(red)]*360
                client.put_pixels(led_colour)

                time.sleep(1)

                led_colour = [(green)]*360
                client.put_pixels(led_colour)

                time.sleep(1)

                led_colour = [(blue)]*360
                client.put_pixels(led_colour)

                time.sleep(1)

                led_colour = [(violet)]*360
                client.put_pixels(led_colour)

                time.sleep(1)

                led_colour = [(Aqua)]*360
                client.put_pixels(led_colour)

                time.sleep(1)
                
        except KeyboardInterrupt:
            print("\nCancelling animation...\n")
            led_colour = [(black)]*360
            client.put_pixels(led_colour)
            continue
    
    elif Option == '2':
        
        print("Starting Animation...\nPress CTRL + C to exit.")
        
        try:
            while True :
                for x in range (0,60):
                    red = random.randint(0,256)
                    green = random.randint(0,256)
                    blue = random.randint(0,256)
                    led_colour[x]=(red,green,blue)
                    time.sleep(0.02)
                    client.put_pixels(led_colour)
   
                for x in reversed(range(60,120)):
                    red = random.randint(0,256)
                    green = random.randint(0,256)
                    blue = random.randint(0,256)
                    led_colour[x]=(red,green,blue)
                    time.sleep(0.02)
                    client.put_pixels(led_colour)

                for x in range (120,180):
                    red = random.randint(0,256)
                    green = random.randint(0,256)
                    blue = random.randint(0,256)
                    led_colour[x]=(red,green,blue)
                    time.sleep(0.02)
                    client.put_pixels(led_colour)
   
                for x in reversed(range(180,240)):
                    red = random.randint(0,256)
                    green = random.randint(0,256)
                    blue = random.randint(0,256)
                    led_colour[x]=(red,green,blue)
                    time.sleep(0.02)
                    client.put_pixels(led_colour)
    
                for x in range (240,300):
                    red = random.randint(0,256)
                    green = random.randint(0,256)
                    blue = random.randint(0,256)
                    led_colour[x]=(red,green,blue)
                    time.sleep(0.02)
                    client.put_pixels(led_colour)
   
                for x in reversed(range(300,360)):
                    red = random.randint(0,256)
                    green = random.randint(0,256)
                    blue = random.randint(0,256)
                    led_colour[x]=(red,green,blue)
                    time.sleep(0.02)
                    client.put_pixels(led_colour)

                for x in reversed(range(300,360)):
                    led_colour[x]=(0,0,0)
                    time.sleep(0.02)
                    client.put_pixels(led_colour)

                for x in range(240,300):
                    led_colour[x]=(0,0,0)
                    time.sleep(0.02)
                    client.put_pixels(led_colour)

                for x in reversed(range(180,240)):
                    led_colour[x]=(0,0,0)
                    time.sleep(0.02)
                    client.put_pixels(led_colour)

                for x in range(120,180):
                    led_colour[x]=(0,0,0)
                    time.sleep(0.02)
                    client.put_pixels(led_colour)

                for x in reversed(range(60,120)):
                    led_colour[x]=(0,0,0)
                    time.sleep(0.02)
                    client.put_pixels(led_colour)
                
                for x in range(0,60):
                    led_colour[x]=(0,0,0)
                    time.sleep(0.02)
                    client.put_pixels(led_colour)

        except KeyboardInterrupt:
            print("\nCancelling animation...\n")
            led_colour = [(black)]*360
            client.put_pixels(led_colour)
            time.sleep(1)
            continue

    elif Option == '3':

        print("Starting Animation...\nPress CTRL + C to exit.")
        
        try:
            while True :
                red = random.randint(0,256)
                green = random.randint(0,256)
                blue = random.randint(0,256)
                
                for i in range (0,60):
                    led_colour[i] = (red,green,blue)
                    led_colour[i+60] = (red,green,blue)
                    led_colour[i+120] = (red,green,blue)
                    led_colour[i+180] = (red,green,blue)
                    led_colour[i+240] = (red,green,blue)
                    led_colour[i+300] = (red,green,blue)
                    client.put_pixels(led_colour)
                    time.sleep(0.01)
		
                red = random.randint(0,256)
                green = random.randint(0,256)
                blue = random.randint(0,256)
                
                for i in reversed(range(0,60)):
                    led_colour[i] = (red,green,blue)
                    led_colour[i+60] = (red,green,blue)
                    led_colour[i+120] = (red,green,blue)
                    led_colour[i+180] = (red,green,blue)
                    led_colour[i+240] = (red,green,blue)
                    led_colour[i+300] = (red,green,blue)
                    client.put_pixels(led_colour)
                    time.sleep(0.01)
                    
        except KeyboardInterrupt:
            print("\nCancelling animation...\n")
            led_colour = [(black)]*360
            client.put_pixels(led_colour)
            time.sleep(1)
            continue

    elif Option == '4':

        print("Starting Animation...\nPress CTRL + C to exit.")
        
        try:

            while True :
                led_colour = [(black)]*360
                client.put_pixels(led_colour)
                for x in range (0,25):
                    rowOne = random.randint(0,60)
                    rowTwo = random.randint(60,120)
                    rowThree = random.randint(120,180)
                    rowFour = random.randint(180,240)
                    rowFive = random.randint(240,300)
                    rowSix = random.randint(300,359)

                    red = random.randint(0,256)
                    green = random.randint(0,256)
                    blue = random.randint(0,256)
                    colour = (red,green,blue)
                
                    led_colour[rowOne]= colour
                    led_colour[rowTwo]= colour
                    led_colour[rowThree]= colour
                    led_colour[rowFour]= colour
                    led_colour[rowFive]= colour
                    led_colour[rowSix]= colour
                    client.put_pixels(led_colour)
                    time.sleep(0.1)
		
                time.sleep(0.2)

        except KeyboardInterrupt:
            print("\nCancelling animation...\n")
            led_colour = [(black)]*360
            client.put_pixels(led_colour)
            time.sleep(1)
            continue

    elif Option == '5':

        print("Turn on sound near sensor.\nPress CTRL + C to exit.")

        try:

            while True:

               #reading values from sound sensor
               SensorData = a.digitalRead(soundSensor)
               print(SensorData)

               led_colour1=[(255,0,0)]*360
               led_colour2=[(0,0,0)]*360
               
               #condition for intensity of soundData
               if(SensorData == 0):

                client.put_pixels(led_colour1)

               elif(SensorData == 1):

                client.put_pixels(led_colour2)


        except KeyboardInterrupt:
            print("\nCancelling animation...\n")
            led_colour = [(black)]*360
            client.put_pixels(led_colour)
            time.sleep(1)
            continue
        
    elif Option == '6':

        print("\nExiting...")
        led_colour = [(black)]*360
        client.put_pixels(led_colour)
        break;
    
    else:
        
        print("\nInvalid Input. Please try again\n")
        time.sleep(1)
