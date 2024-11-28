from ion import *
from kandinsky import *
from math import *
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
    
    # RPN-specific: ENTER, DUP, ROT, SWAP
    elif keydown(KEY_EXE):
        if numbers:
            add(float(numbers))
            numbers = ""
        elif results:
            dup = results[0]
            add(dup)
        display()
    elif keydown(KEY_LEFTPARENTHESIS):
        if numbers:
            add(float(numbers))
            numbers = ""
        if len(results) >= 2:
            results.reverse()
            rot = results[0]
            remove()
            results.reverse()
            add(rot)
        else:
            add(0)
        display()
    elif keydown(KEY_RIGHTPARENTHESIS):
        if numbers:
            add(float(numbers))
            numbers = ""
        if len(results) >= 2:
            swap = results[0]
            results[0] = results[1]
            results[1] = swap
        else:
            add(0)
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

    # SHIFT: reciprocal trig operators
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
                sleep(0.1)
            if keydown(KEY_IMAGINARY): # D: radians to degrees
                pressed = True
                if not numbers and results:
                    results[0] = degrees(results[0])
                elif numbers:
                    add(degrees(float(numbers)))
                    numbers = ""
                display()
                sleep(0.1)
            if keydown(KEY_FOUR): # R: degrees to radians
                pressed = True
                if not numbers and results:
                    results[0] = radians(results[0])
                elif numbers:
                    add(radians(float(numbers)))
                    numbers = ""
                display()
                sleep(0.1)
            if keydown(KEY_COSINE): # H: dec to HH:MM
                pressed = True
                if not numbers and results:
                    results[0] = hms(results[0])
                elif numbers:
                    add(hms(float(numbers)))
                    numbers = ""
                display()
                sleep(0.1)

    # Idle timeout before next inf. loop
    sleep(0.173)
