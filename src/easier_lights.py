import time
import pigpio
pi = pigpio.pi()

RED_PIN = 17
GREEN_PIN = 22
BLUE_PIN = 24

red = 255
green = 0
blue = 0
def easier_color(r,g,b):
    pi.set_PWM_dutycycle(RED_PIN, r)
    pi.set_PWM_dutycycle(BLUE_PIN, g)
    pi.set_PWM_dutycycle(GREEN_PIN, b)

def update():
    pi.set_PWM_dutycycle(RED_PIN, red)
    pi.set_PWM_dutycycle(BLUE_PIN, green)
    pi.set_PWM_dutycycle(GREEN_PIN, blue)

def white(level):
    easier_color(level,level,level)

def off():
    global red
    global green
    global blue
    red = 0
    green = 0
    blue = 0
    update()

def rainbow(do):
    global red
    global green
    global blue
    while(do):
        if (red == 255) and green < 255 and blue == 0:
            green = green+1

        if red > 0 and green == 255 and blue == 0:
            red = red-1

        if red == 0 and green == 255 and blue < 255:
            blue = blue+1

        if red == 0 and green > 0 and blue == 255:
            green = green -1

        if red < 255 and green ==0 and blue == 255:
            red = red+1

        if red == 255 and green == 0 and blue > 0:
            blue = blue-1
        update()
        time.sleep(0.005)
def main():
    off()







if __name__ == '__main__':
    main()
