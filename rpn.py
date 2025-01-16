import micropython as mp
mp.kbd_intr(-1) # Disable KeyboardInterrupt
from ion import *
from kandinsky import *
from math import *
from random import *
from time import *

# GUI: refreshes whole screen
def display():
    # STACK: number of levels displayed
    if fixed:
        levels = 4
    else:
        levels = 8
    # Fixed stack: drops oldest level if not displayable
    if fixed and len(stack) > levels:
        stack.pop()
    # GUI: height (pixels) of lines displayed (stack + entry)
    h = 222 // (levels+1)
    # GUI: blank background
    fill_rect(0,0, 320,222, color(245,250,255))
    # GUI: odd/even line backgrounds
    if fixed or len(stack)>=8:
        fill_rect(0,0, 320,h, color(255,254,255))
    if fixed or len(stack)>=6:
        fill_rect(0,2*h, 320,h, color(255,254,255))
    if not fixed and len(stack) >= 4:
        fill_rect(0,4*h, 320,h, color(255,254,255))
    if not fixed and len(stack) >= 2:
        fill_rect(0,6*h, 320,h, color(255,254,255))  
    # GUI: displays stack level names
    if fixed:
        shift = 13
    else:
        shift = 3
    if fixed:
        name = ["X:", "Y:", "Z:", "T:"]
        for line in range(levels):
            draw_string(name[line], 10, h*(levels-1-line) + shift, (0,0,0), (245+10*(line%2),250+4*(line%2),255))
    else:
        for line in range(min(levels, len(stack))):
            draw_string(str(line+1)+":", 10, h*(levels-1-line) + shift, (0,0,0), (245+10*(line%2),250+4*(line%2),255))
    # GUI: displays stack levels contents
    for line in range(len(stack)):
        draw_string(str(stack[line]), 310 - 10*len(str(stack[line])), h*(levels-1-line) + shift, (0,0,0), (245+10*(line%2),250+4*(line%2),255))
    # GUI: entry field
    fill_rect(0,levels*h, 320,1, color(223,217,222))  # Separation line
    fill_rect(0,levels*h+1, 320,222-(levels-1)*h, color(255,254,255))  # Contents
    draw_string(entry, 10, levels*h + shift + shift%9, (0,0,0), (255,254,255))
    sleep(0.2)

# Highlight selected stack level if any
def selected(level):
    if fixed:
        levels = 4
        shift = 13
    else:
        levels = 8
        shift = 3
    h = 222 // (levels+1)
    draw_string(str(stack[level]), 310 - 10*len(str(stack[level])), h*(levels-1-level) + shift, (138,141,139), (214,213,231))

# Python-specific: keep integers and not floats if possible
def python_int(foo):
    foo = float(foo)
    if foo == int(foo):
        foo = int(foo)
    return foo

# Dropping something from the stack
def drop():
    stack.pop(0)
    # On fixed stack: T-level keeps its value
    if fixed:
        stack.append(stack[2])

# Pushing something to the stack
def push(foo):
    try:
        top = python_int(foo)
    except Exception as message:
        error(message)
    else:
        global lastx
        lastx = foo
        stack.insert(0, top)

# Unary operations
def evaluate1(operation):
    global entry, stack, lastx
    if not entry and stack:
        try:
            result = operation(stack[0])
        except Exception as message:
            error(message)
        else:
            lastx = stack[0]
            stack[0] = python_int(result)
    elif entry:
        try:
            result = operation(float(entry))
        except Exception as message:
            error(message)
        else:
            lastx = entry
            stack.insert(0,python_int(result))
            entry = ""
    display()

# Binary operations
def evaluate2(operation):
    global entry, stack, lastx
    if not entry and len(stack)>=2:
        try:
            result = operation(stack[1], stack[0])
        except Exception as message:
            error(message)
        else:
            lastx = stack[0]
            stack[1] = python_int(result)
            drop()
    elif entry and stack:
        try:
            result = operation(stack[0], float(entry))
        except Exception as message:
            error(message)
        else:
            lastx = entry
            stack[0] = python_int(result)
            entry = ""
    display()

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

# Median of a list
def med(data):
    s = sorted(data)
    n = len(s)
    if n % 2 == 1:
        return s[n//2]
    else:
        return (s[n//2 - 1] + s[n//2]) / 2

# Quartiles (1st or 3rd) of a list
def quartile(data, q):
    s = sorted(data)
    n = len(s)
    i = ceil(q/4 * n)
    return s[i - 1]

# Standard deviation of a list
def stdev(s):
    m = sum(s) / len(s)
    v = 0
    for i in s:
        v += (i - m)**2
    v = v / len(s)
    return sqrt(v)

# Error message box
def error(text):
    text = str(text)
    width = 10*len(text) + 32
    x  = (320 - width) // 2
    fill_rect(x,89, width,44, color(0,0,0))
    draw_string(text, x+16,102, (255,254,255), (0,0,0))
    sleep(0.5)
    pressed = False
    while not pressed:
        for i in range(53):
            if keydown(i):
                pressed = True
    display()

# RPN hotkeys toolbox
def toolbox():
    keys = ["xnt", " (", " )", "Ans", "[s]+Ans", " i", " ,"]
    desc = ["Fixed/dynamic stack", "ROLL (n)/all levels", "SWAP last two levels", "Copy last X value", "Copy 2nd level", "Inverse", "Change signs"]
    # Dialog title
    fill_rect(27,27, 266,21, color(65,64,65))
    fill_rect(28,28, 264,19, color(108,99,115))
    draw_string("Hotkeys", 125,28, (255,254,255), (108,99,115))
    # Dialog contents
    fill_rect(27,48, 266,174, color(238,238,238))
    fill_rect(28,49, 264,173, color(255,254,255))
    # Lists keys next to their functionality
    for i in range(len(keys)):
        y = 49 + i * 174 // len(keys)
        draw_string(keys[i], 35, y+4)
        draw_string(desc[i], 285 - 10*len(desc[i]), y+4, (164,165,164), (255,254,255))
        # Draw a separator between each line
        fill_rect(28, y-1, 264, 1, (238,238,238))
    # Closing the hotkeys toolbox
    sleep(0.5)
    while not keydown(KEY_OK) and not keydown(KEY_TOOLBOX) and not keydown(KEY_BACK):
        None
    display()

# Alpha shortcuts toolbox
def varbox():
    keys = ["D", "R", "C", "F", "H", "P", "S", "?"]
    desc = ["Convert rad to °", "Convert ° to rad", "Convert °F to °C", "Convert °C to °F", "Convert hrs to h:min", "Prime factorisation", "Statistics", "Random number in [0,1)"]
    # Dialog title
    fill_rect(27,27, 266,21, color(65,64,65))
    fill_rect(28,28, 264,19, color(108,99,115))
    draw_string("Alpha shortcuts", 85,28, (255,254,255), (108,99,115))
    # Dialog contents
    fill_rect(27,48, 266,174, color(238,238,238))
    fill_rect(28,49, 264,173, color(255,254,255))
    # Lists keys next to their functionality
    for i in range(len(keys)):
        y = 49 + i * 174 // len(keys)
        draw_string(keys[i], 35, y+2)
        draw_string(desc[i], 285 - 10*len(desc[i]), y+2, (164,165,164), (255,254,255))
        # Draw a separator between each line
        fill_rect(28, y-1, 264, 1, (238,238,238))
    # Closing the Alpha shortcuts toolbox
    sleep(0.5)
    while not keydown(KEY_OK) and not keydown(KEY_VAR) and not keydown(KEY_BACK):
        None
    display()

# Statistics toolbox
def statistics():
    # What to calculate?
    desc = ["Minimum", "1st quartile", "Median", "3rd quartile", "Maximum", "Mean", "Std deviation", "Nb of data", "Sum of values"]
    stat = ["Min", "Q1", "Med", "Q3", "Max", "x", "σ", "n", "Σx"]
    values = [min(stack), quartile(stack,1), med(stack), quartile(stack,3), max(stack), sum(stack)/len(stack), stdev(stack), len(stack), sum(stack)]
    # Dialog title
    fill_rect(27,27, 266,21, color(65,64,65))
    fill_rect(28,28, 264,19, color(108,99,115))
    draw_string("Statistics", 110,28, (255,254,255), (108,99,115))
    # Dialog contents
    fill_rect(27,48, 266,174, color(238,238,238))
    fill_rect(28,49, 264,173, color(255,254,255))
    # Line backgrounds
    for i in range(max(len(stat), len(values))):
         fill_rect(28, 49 + 19*i, 264, 19, (245+10*(i%2), 250+4*(i%2), 255))
    # Name of statistic then notation
    for i in range(len(desc)):
        draw_string(desc[i], 162-10*len(desc[i]), 50 + 19*i, (0,0,0), (245+10*(i%2), 250+4*(i%2), 255))
    for i in range(len(stat)):
        draw_string(stat[i], 185-5*len(stat[i]), 50 + 19*i, (180,180,180), (245+10*(i%2), 250+4*(i%2), 255))
    # Workaround: draw a bar over x for the missing "mean" glyph
    fill_rect(180, 148, 10, 1, color(180,180,180))
    # Display computed values
    for i in range(len(values)):
        txt = str(values[i])[0:8]
        draw_string(txt, 285-10*len(txt), 50 + 19*i, (0,0,0), (245+10*(i%2), 250+4*(i%2), 255))
    # Separators for more convenient reading
    fill_rect(28, 49 + 19*5, 264, 1, color(180,180,180))
    fill_rect(28, 49 + 19*7, 264, 1, color(180,180,180))
    # Closing the statistics toolbox
    sleep(0.5)
    while not keydown(KEY_OK) and not keydown(KEY_BACK):
        None
    display()

################################################

# Original state: dynamic stack, empty entry field

fixed = False
stack = []
entry = ""
lastx = ""

display()
while True:
    # Type in entry
    if keydown(KEY_ZERO):
        entry += "0"
        display()
    elif keydown(KEY_ONE):
        entry += "1"
        display()
    elif keydown(KEY_TWO):
        entry += "2"
        display()
    elif keydown(KEY_THREE):
        entry += "3"
        display()
    elif keydown(KEY_FOUR):
        entry += "4"
        display()
    elif keydown(KEY_FIVE):
        entry += "5"
        display()
    elif keydown(KEY_SIX):
        entry += "6"
        display()
    elif keydown(KEY_SEVEN):
        entry += "7"
        display()
    elif keydown(KEY_EIGHT):
        entry += "8"
        display()
    elif keydown(KEY_NINE):
        entry += "9"
        display()
    elif keydown(KEY_DOT):
        if not entry:
            entry = "0."
        else:
            entry += "."
        display()
    elif keydown(KEY_EE):
        entry += "e"
        display()
    elif keydown(KEY_PI) and not entry:
        push(pi)
        display()
    
    # RPN-specific

    elif keydown(KEY_XNT):  # Fixed or dynamic stack
        fixed = not fixed
        if fixed:  # Max 4 levels, equal to 0 if not used
            for level in range(4, len(stack)):
                stack.pop()
            for level in range(4 - len(stack)):
                stack.append(0)
        else:  # All levels should be empty if not used
            while stack[len(stack) - 1] == 0:
                stack.pop()
                if stack == [0]:
                    stack = []
                    break
        display()
    elif keydown(KEY_ANS):  # LastX
        if entry:
            stack.insert(0, python_int(entry))
        push(lastx)
        display()
    elif keydown(KEY_EXE) or keydown(KEY_OK):  # ENTER, DUP
        if entry:
            push(entry)
            entry = ""
        elif stack:
            dup = stack[0]
            push(dup)
        display()
    elif keydown(KEY_LEFTPARENTHESIS):  # (n) ROLL down
        if entry:
            pos = float(entry)
            entry = ""
            if pos == int(pos) and int(pos) <= len(stack):
                stack.insert(int(pos-1), stack.pop(0))
        elif len(stack) >= 2:
            stack.append(stack.pop(0))
        display()
    elif keydown(KEY_RIGHTPARENTHESIS):  # SWAP
        if entry:
            push(entry)
            entry = ""
        if len(stack) >= 2:
            swap = stack[0]
            stack[0] = stack[1]
            stack[1] = swap
        display()
    elif keydown(KEY_BACKSPACE):  # Drops stack top or deletes cipher
        if not entry and stack:
            drop()
        else:
            entry = entry[:-1]
        display()
    elif keydown(KEY_UP):  # Selection of stack levels
        if not fixed and stack:
            level = 0
            selected(level)
            sleep(0.2)
            while level >= 0:
                if keydown(KEY_UP) and level < len(stack)-1:
                    level +=1
                    display()
                    selected(level)
                if keydown(KEY_DOWN):
                    level -= 1
                    display()
                    selected(level)
                if keydown(KEY_BACKSPACE):  # DROPs first levels
                    stack = stack[level+1:]
                    level = -1
                if keydown(KEY_OK) or keydown(KEY_EXE):  # PICKs actual level and copy to stack top
                    stack[0] = stack[level]
                    level = -1
                if keydown(KEY_BACK):  # Exit selection mode
                    level = -1
            display()

    # Unary operators

    elif keydown(KEY_EXP):
        # If no value: inputs e instead
        if not entry and not stack:
            push(exp(1))
            display()
        else:
            evaluate1(lambda x: exp(x))
    elif keydown(KEY_LN):
        evaluate1(lambda x: log(x))
    elif keydown(KEY_LOG):
        evaluate1(lambda x: log10(x))
    elif keydown(KEY_SINE):
        evaluate1(lambda x: sin(x))
    elif keydown(KEY_COSINE):
        evaluate1(lambda x: cos(x))
    elif keydown(KEY_TANGENT):
        evaluate1(lambda x: tan(x))
    elif keydown(KEY_SQRT):
        evaluate1(lambda x: sqrt(x))
    elif keydown(KEY_SQUARE):
        evaluate1(lambda x: x*x)

    # SHIFT: reciprocal trig, ROLL up, CLEAR, OVER

    elif keydown(KEY_SHIFT):
        pressed = False
        draw_string("shift",270,0)
        sleep(0.2)
        while not pressed:
            if keydown(KEY_SINE):
                evaluate1(lambda x: asin(x))
                pressed = True
            if keydown(KEY_COSINE):
                evaluate1(lambda x: acos(x))
                pressed = True
            if keydown(KEY_TANGENT):
                evaluate1(lambda x: atan(x))
                pressed = True
            if keydown(KEY_LEFTPARENTHESIS): # ROLL up
                if entry:
                    pos = float(entry)
                    entry = ""
                    if pos == int(pos) and int(pos) <= len(stack):
                        stack.insert(0, stack.pop(int(pos)-1))
                elif len(stack) >= 2:
                    stack.insert(0, stack.pop())
                pressed = True
                display()
            if keydown(KEY_BACKSPACE): # CLEAR
                if fixed:
                    stack = [0, 0, 0, 0]
                else:
                    stack = []
                entry = ""
                pressed = True
                display()
            if keydown(KEY_ANS):  # OVER
                if fixed or len(stack) >= 2:
                    push(stack[1])
                pressed = True
                display()
            if keydown(KEY_SHIFT):  # Quit shift mode
                pressed = True
                display()

    # Not labeled unary operators

    elif keydown(KEY_IMAGINARY):
        evaluate1(lambda x: 1/x)
    elif keydown(KEY_COMMA):
        evaluate1(lambda x: -x)

    # Binary operators

    elif keydown(KEY_PLUS):
        evaluate2(lambda x,y: x+y)
    elif keydown(KEY_MINUS):
        if entry and entry[-1] == "e" and entry.count("-") == 0:
            entry += "-"
        else:
            evaluate2(lambda x,y: x-y)
    elif keydown(KEY_MULTIPLICATION):
        evaluate2(lambda x,y: x*y)
    elif keydown(KEY_DIVISION):
        evaluate2(lambda x,y: x/y)
    elif keydown(KEY_POWER):
        evaluate2(lambda x,y: x**y)

    # ALPHA operators

    elif keydown(KEY_ALPHA):
        pressed = False
        draw_string("alpha",270,0)
        sleep(0.2)
        while not pressed:
            if keydown(KEY_DOT):  # !: factorial
                evaluate1(lambda x: factorial(int(x)))
                pressed = True
            if keydown(KEY_BACKSPACE):  # %: proportion of
                evaluate2(lambda x,y: x*y / 100)
                pressed = True
            if keydown(KEY_COSINE):  # H: dec to HH:MM
                evaluate1(lambda x: hms(x))
                pressed = True
            if keydown(KEY_IMAGINARY):  # D: radians to degrees
                evaluate1(lambda x: degrees(x))
                pressed = True
            if keydown(KEY_FOUR):  # R: degrees to radians
                evaluate1(lambda x: radians(x))
                pressed = True
            if keydown(KEY_LOG):  # C: Fahrenheit to Celsius
                evaluate1(lambda x: (x-32) * 5/9)
                pressed = True
            if keydown(KEY_POWER):  # F: Celsius to Fahrenheit
                evaluate1(lambda x: x * 9/5 + 32)
                pressed = True
            if keydown(KEY_LEFTPARENTHESIS):  # P: Prime factorisation
                if not entry and stack:
                    push(prime_facto(int(stack[0])))
                elif entry:
                    push(int(entry))
                    push(prime_facto(int(entry)))
                    entry = ""
                pressed = True
                display()
            if keydown(KEY_FIVE):  # S: Statistics
                pressed = True
                if not fixed and len(stack) >= 2:
                    statistics()
                display()
            if keydown(KEY_ZERO):  # ?: Random number in [0;1[
                if not entry:
                    push(random())
                pressed = True
                display()
            if keydown(KEY_ALPHA):  # Quit alpha mode
                pressed = True
                display()
              
    # RPN Hotkeys
    elif keydown(KEY_TOOLBOX):
        toolbox()

    # Alpha shortcuts
    elif keydown(KEY_VAR):
        varbox()

    # Back to NumWorks menu
    elif keydown(KEY_HOME):
        quit()

    # Idle timeout before next inf. loop
    sleep(0.08)
