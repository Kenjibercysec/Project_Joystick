import serial
import time

def main():
    ser = serial.Serial('COM6', 9600)  
    while True:
        data = ser.readline().decode().strip()
        if data:
            x, y, button = map(int, data.split(','))
            print("Valor do eixo X:", x)
            print("Valor do eixo Y:", y)
        time.sleep(0.1)

if __name__ == "__main__":
    main()