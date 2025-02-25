# Reverse Polish Notation on NumWorks

Python script for the scientific Numworks calculator, enabling to type in RPN in a graphical user interface.

### Test it & get it now
On NumWorks website https://my.numworks.com/python/xanderleadaren/rpn

### Keystrokes
- Basic operations are mapped to the usual keys.
- [Toolbox] key allows the user to display some other hotkeys, including RPN-specific functions as LastX, OVER, ROLL, SWAP, DUPlicate, …
- [var] key shows functionalities mapped to [alpha]+{key}: prime factorisation, random, converting (degrees/radians, Fahrenheit/Celsius), random, …

![téléchargement](https://github.com/user-attachments/assets/c633782f-a30b-4241-a8d5-fd019da3d049)


A remark for the [(] key, which emulates [R↓] of HP calculators:

- used as-is, rotates the stack downwards
- with [shift], rotates the stack upwards
- if an natural number `n` is on the command line, rotates only the first `n` stack levels

### Two RPN stack variants
On [x,n,t] key, the user may choose between two RPN variants:
- either dynamic levels 1,2,3,… with infinite amount of inputs (default)
- either X,Y,Z,T levels with dropping of oldest inputs, and T keeping its value

In dynamic mode, use the [↑] and [↓] arrows to select stack levels. When a level is selected, press [⌫] to DROP all levels from top down to the selected one, or press [OK] or [EXE] to PICK the value in the selected level and copy it on stack top instead of the actual value.
