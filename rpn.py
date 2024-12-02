from ion import *
from kandinsky import *
from math import *
from random import *
from time import *

# GUI: refreshes whole screen
def display():
    mem = 8
    # STACK: limits to mem-1 items + input
    n = len(results)
    if n > mem-1:
        remove()
        n -= 1
    h = 222//mem
    # GUI: line backgrounds
    fill_rect(0,0, 320,222, color(255,254,255))
    if n >= 2:
        fill_rect(0,1*h, 320,h, color(245,250,255))
    if n >= 4:
        fill_rect(0,3*h, 320,h, color(245,250,255))
    if n >= 6:
        fill_rect(0,5*h, 320,h, color(245,250,255))
    #  GUI: displays stack items
    for line in range(n):
        draw_string(str(results[n-1-line]), 10, h*line+5)
    # GUI: input field separation line
    fill_rect(0,(mem-1)*h, 320,1, color(223,217,222))
    # GUI: input field contents
    draw_string(numbers, 6,197)
    sleep(0.2)

# Removing something from the stack
def remove():
    results.reverse()
    results.pop()
    results.reverse()

#  Adding something to the stack
def add(foo):
    results.reverse()
    results.append(foo)
    results.reverse()

# Converting decimal to sexagesimal
def hms(dec):
    hours = int(dec)
    minutes = (dec-hours) * 60
    return hours + minutes/100

# Finding the lowest prime divisor
def prime_facto(n):
    div = 2
    while div**2 <= n:
       if n % div == 0:
           return div
       div += 1
    return 1

# Hotkeys recap
def toolbox():
    # Title
    fill_rect(27,26, 266,22, color(65,64,65))
    fill_rect(28,27, 264,20, color(106,101,115))
    draw_string(" HOTKEYS ", 115,28)
    # Contents
    fill_rect(27,48, 266,174, color(238,238,238))
    fill_rect(28,49, 264,173, color(255,254,255))
    draw_string("H: dec → h:min", 35,52)
    fill_rect(28,74, 264,1, color(238,238,238))
    draw_string("D: rad → deg     i : 1/x", 35,80)
    draw_string("R: deg → rad     , :  ±", 35,100)
    fill_rect(28,124, 264,1, color(238,238,238))
    draw_string("C: °F → °C       ( : ROT", 35,130)
    draw_string("F: °C → °F       ) : SWAP", 35,150)
    fill_rect(28,174, 264,1, color(238,238,238))
    draw_string("P: prime fact.", 35,180)
    draw_string("?: random       EXE: DUP", 35,200)
    sleep(0.5)
    while not keydown(KEY_OK) and not keydown(KEY_TOOLBOX):
        None
    display()

##########################################

results = []
numbers = ""

display()
while True:
    # Type in numbers
    if keydown(KEY_ZERO):
        numbers += "0"
        display()
    elif keydown(KEY_ONE):
        numbers += "1"
        display()
    elif keydown(KEY_TWO):
        numbers += "2"
        display()
    elif keydown(KEY_THREE):
        numbers += "3"
        display()
    elif keydown(KEY_FOUR):
        numbers += "4"
        display()
    elif keydown(KEY_FIVE):
        numbers += "5"
        display()
    elif keydown(KEY_SIX):
        numbers += "6"
        display()
    elif keydown(KEY_SEVEN):
        numbers += "7"
        display()
    elif keydown(KEY_EIGHT):
        numbers += "8"
        display()
    elif keydown(KEY_NINE):
        numbers += "9"
        display()
    elif keydown(KEY_DOT):
        numbers += "."
        display()
    elif keydown(KEY_PI) and not numbers:
        add(pi)
        display()
    
    # RPN-specific
    elif keydown(KEY_EXE): # ENTER, DUP
        if numbers:
            add(float(numbers))
            numbers = ""
        elif results:
            dup = results[0]
            add(dup)
        display()
    elif keydown(KEY_LEFTPARENTHESIS): # ROT
        if numbers:
            add(float(numbers))
            numbers = ""
        if len(results) >= 2:
            results.reverse()
            rot = results[0]
            remove()
            results.reverse()
            add(rot)
        display()
    elif keydown(KEY_RIGHTPARENTHESIS): # SWAP
        if numbers:
            add(float(numbers))
            numbers = ""
        if len(results) >= 2:
            swap = results[0]
            results[0] = results[1]
            results[1] = swap
        display()

    # Drops stack item or deletes cipher
    elif keydown(KEY_BACKSPACE):
        if not numbers and results:
            remove()
        else:
            numbers = numbers[:-1]
        display()

    # Unary operators
    elif keydown(KEY_EXP):
        # Inputs e
        if not numbers and not results:
            add(exp(1))
        elif not numbers and results:
            results[0] = exp(results[0])
        elif numbers:
            add(exp(float(numbers)))
            numbers = ""
        display()
    elif keydown(KEY_LN):
        if not numbers and results:
            results[0] = log(results[0])
        elif numbers:
            add(log(float(numbers)))
            numbers = ""
        display()
    elif keydown(KEY_LOG):
        if not numbers and results:
            results[0] = log10(results[0])
        elif numbers:
            add(log10(float(numbers)))
            numbers = ""
        display()
    elif keydown(KEY_SINE):
        if not numbers and results:
            results[0] = sin(results[0])
        elif numbers:
            add(sin(float(numbers)))
            numbers = ""
        display()
    elif keydown(KEY_COSINE):
        if not numbers and results:
            results[0] = cos(results[0])
        elif numbers:
            add(cos(float(numbers)))
            numbers = ""
        display()
    elif keydown(KEY_TANGENT):
        if not numbers and results:
            results[0] = tan(results[0])
        elif numbers:
            add(tan(float(numbers)))
            numbers = ""
        display()

    # SHIFT: reciprocal trig, CLEAR
    elif keydown(KEY_SHIFT):
        pressed = False
        draw_string("shift",270,0)
        while not pressed:
            if keydown(KEY_SINE):
                pressed = True
                if not numbers and results:
                    results[0] = asin(results[0])
                elif numbers:
                    add(asin(float(numbers)))
                    numbers = ""
                display()
            if keydown(KEY_COSINE):
                pressed = True
                if not numbers and results:
                    results[0] = acos(results[0])
                elif numbers:
                    add(acos(float(numbers)))
                    numbers = ""
                display()
            if keydown(KEY_TANGENT):
                pressed = True
                if not numbers and results:
                    results[0] = atan(results[0])
                elif numbers:
                    add(atan(float(numbers)))
                    numbers = ""
                display()
            if keydown(KEY_BACKSPACE):
                pressed = True
                results = []
                numbers = ""
                display()

    elif keydown(KEY_SQRT):
        if not numbers and results:
            results[0] = sqrt(results[0])
        elif numbers:
            add(sqrt(float(numbers)))
            numbers = ""
        display()
    elif keydown(KEY_SQUARE):
        if not numbers and results:
            results[0] = results[0]**2
        elif numbers:
            add(float(numbers)**2)
            numbers = ""
        display()

    # Not labeled unary operators
    elif keydown(KEY_IMAGINARY):
        if not numbers and results:
            results[0] = 1/results[0]
        elif numbers:
            add(1/float(numbers))
            numbers = ""
        display()
    elif keydown(KEY_COMMA):
        if not numbers and results:
            results[0] = -results[0]
        elif numbers:
            add(-float(numbers))
            numbers = ""
        display()

    # Binary operators
    elif keydown(KEY_PLUS):
        if not numbers and len(results)>=2:
            results[1] += results[0]
            remove()
        elif numbers and results:
            results[0] += float(numbers)
            numbers = ""
        display()
    elif keydown(KEY_MINUS):
        if not numbers and len(results)>=2:
            results[1] -= results[0]
            remove()
        elif numbers and results:
            results[0] -= float(numbers)
            numbers = ""
        display()
    elif keydown(KEY_MULTIPLICATION):
        if not numbers and len(results)>=2:
            results[1] = results[1]*results[0]
            remove()
        elif numbers and results:
            results[0] = results[0]*float(numbers)
            numbers = ""
        display()
    elif keydown(KEY_DIVISION):
        if not numbers and len(results)>=2:
            results[1] = results[1]/results[0]
            remove()
        elif numbers and results:
            results[0] = results[0]/float(numbers)
            numbers = ""
        display()
    elif keydown(KEY_POWER):
        if not numbers and len(results)>=2:
            results[1] = results[1] ** results[0]
            remove()
        elif numbers and results:
            results[0] = results[0] ** float(numbers)
            numbers = ""
        display()
    elif keydown(KEY_EE):
        if not numbers and len(results)>=2:
            results[1] = results[1] * 10**results[0]
            remove()
        elif numbers and results:
            results[0] = results[0] * 10**float(numbers)
            numbers = ""
        display()

    # ALPHA operators
    elif keydown(KEY_ALPHA):
        pressed = False
        draw_string("alpha",270,0)
        while not pressed:
            if keydown(KEY_DOT): # !: factorial
                pressed = True
                if not numbers and results:
                    results[0] = factorial(int(results[0]))
                elif numbers:
                    add(factorial(int(numbers)))
                    numbers = ""
                display()
            if keydown(KEY_COSINE): # H: dec to HH:MM
                pressed = True
                if not numbers and results:
                    results[0] = hms(results[0])
                elif numbers:
                    add(hms(float(numbers)))
                    numbers = ""
                display()
            if keydown(KEY_IMAGINARY): # D: radians to degrees
                pressed = True
                if not numbers and results:
                    results[0] = degrees(results[0])
                elif numbers:
                    add(degrees(float(numbers)))
                    numbers = ""
                display()
            if keydown(KEY_FOUR): # R: degrees to radians
                pressed = True
                if not numbers and results:
                    results[0] = radians(results[0])
                elif numbers:
                    add(radians(float(numbers)))
                    numbers = ""
                display()
            if keydown(KEY_LOG): # C: Fahrenheit to Celsius
                pressed = True
                if not numbers and results:
                    results[0] = (results[0] - 32) * 5/9
                elif numbers:
                    add((float(numbers) - 32) * 5/9)
                    numbers = ""
                display()
            if keydown(KEY_POWER): # F: Celsius to Fahrenheit
                pressed = True
                if not numbers and results:
                    results[0] = results[0] * 9/5 + 32
                elif numbers:
                    add(float(numbers) * 9/5 + 32)
                    numbers = ""
                display()
            if keydown(KEY_LEFTPARENTHESIS): # P: Prime factorisation
                pressed = True
                if not numbers and results:
                    add(prime_facto(results[0]))
                elif numbers:
                    add(float(numbers))
                    add(prime_facto(float(numbers)))
                    numbers = ""
                display()
            if keydown(KEY_ZERO): # ?: Random number in [0;1[
                pressed = True
                if not numbers:
                    add(random())
                display()
              
    # Hotkeys / Help
    elif keydown(KEY_TOOLBOX):
        toolbox()

    # Idle timeout before next inf. loop
    sleep(0.1)
