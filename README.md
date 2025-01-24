# Reverse Polish Notation on NumWorks

Python script for the scientific Numworks calculator, enabling to type in RPN in a graphical user interface.

### Keystrokes
- Basic operations are mapped to the usual keys.
- [Toolbox] key allows the user to display some other hotkeys, including RPN-specific functions as LastX, OVER, ROLL, SWAP, DUPlicate, …
- [var] key shows functionalities mapped to [alpha]+{key}: prime factorisation, statistics, random, converting (degrees/radians, Fahrenheit/Celsius), random, …

![nw-rpn_hotkeys](https://github.com/user-attachments/assets/844d718f-ada6-4167-80ac-2a7fe744cdc9)


A remark for the [(] key, which emulates [R↓] of HP calculators:

- used as-is, rotates the stack downwards
- with [shift], rotates the stack upwards
- if an natural number `n` is on the command line, rotates only the first `n` stack levels

### Two RPN stack variants
On [x,n,t] key, the user may choose between two RPN variants:
- either dynamic levels 1,2,3,… with infinite amount of inputs (default)
- either X,Y,Z,T levels with dropping of oldest inputs, and T keeping its value

In dynamic mode, use the [↑] and [↓] arrows to select stack levels. When a level is selected, press [⌫] to DROP all levels from top down to the selected one, or press [OK] or [EXE] to PICK the value in the selected level and copy it on stack top instead of the actual value.

### Test it & get it now
On NumWorks website https://my.numworks.com/python/xanderleadaren/rpn


### Roadmap
Here are a few ideas for future improvements:

**Bugfix**
- [(] may not ROLL, raising a ValueError if incorrect syntax on the command line
- with huge numbers, python_int() raises an OverflowError, cannot converting inf to int

**GUI Updates**
- error dialogs instead of nothing happening for e.g. factorial of non natural number
- statistics displayed “fullscreen” instead of inside a dialogbox.
- when selecting a level in dynamic mode: `…` submenu for PICK, DROP, (and n ROLL?)
- display large numbers as approximations instead of overflowing to the left (max: 27 digits)
- add a narrow no-break space every 3 digits from right

**Features**
- study the possibility of *setting* angles to degrees/radians instead of *converting*
- Level selection in dynamic mode: n ROLL
- interactive “clickable” menus
- (then) [%] menu with proportion, evolution, and so on (cf. HP 12C)
- Settings: switch between fixed number of d.p., scientific notation, and so on
- conversion tool on [STO→]
- vectors? (with `[` and `]`): add, substract, scalar multiplication, norm (with `[N]`), dot product, cross product, determinant?…
- complex numbers? (with `(` and `)`) (cf. HP 28S)

**Discarded ideas**
- store to memories: non-pertinence of data when exiting the Python script
