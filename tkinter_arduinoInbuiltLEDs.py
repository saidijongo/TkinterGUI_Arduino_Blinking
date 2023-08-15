import serial
import tkinter as tk 

baudRate = 9600
port = '/dev/ttyACM0'

ser = serial.Serial(port, baudRate, timeout = 1)

def turnOnLED():
    ser.write(b'on')
    print("Sent: ON")

def turnOffLED(): 
    ser.write(b'off')
    print("Sent: OFF")
    

#tkinter window 
root = Tk() 
root.title('Arduino LEDs')

btn_On= tk.Button(root, text="Turn ON", command=turnOnLED)
btn_On.grid(row=0, column=0)

btn_Off = tk.Button(root, text="Turn OFF", command=turnOffLED)
btn_Off.grid(row=0, column=1)

root.geometry("200x100")
root.mainloop()
