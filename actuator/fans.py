from sys import tkinter
import time
from pyfirmata import Arduino , util
import time

bord= Arduino("COM3")
iterator = util.itrerator(bord)
iterator.start()
pin_number=1
start_fan_temp=bord.get_pin("d:pin_nymber:i")

if start_fan_temp==1:
    print("fan start")
    out=bord.get_pin("d:3:o")
    out.write(1) 
elif start_fan_temp==0:
     print("fan start")
     out=bord.get_pin("d:3:o")
     out.write(0) 
