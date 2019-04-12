import colorsys
import opc
import time

client = opc.Client('192.168.2.1:7890')
s = 1
v = 1



for hue in range(360):
    rgb = colorsys.hsv_to_rgb(hue/360.0, s, v)
    leds=[rgb]*360
    client.putPixels(leds)
    print hue, 
    print rgb
    time.sleep(1)
    
    

