# Reverse Polish Notation on NumWorks

Python script for the scientific Numworks calculator, enabling to type in RPN in a graphical user interface.

### Keystrokes
- Basic operations are mapped to the usual buttons.
- [Toolbox] button allows the user to display some other hotkeys, including RPN-specific functions as LastX, ROLL, SWAP or DUPlicate, or prime factorisation or converting degrees from/to radians, or Fahrenheit/Celsius.

![canvas](https://github.com/user-attachments/assets/373930fb-d84a-4949-81f1-c39001a9ecab)

A remark for the [(] key, which emulates [R↓] of HP calculators:

- used as-is, rotates the stack downwards
- with shift, rotates the stack upwards
- if an natural number `n` is on the command line, rotates only the first `n` stack levels

### Two RPN stack variants
On [x,n,t] key, the user may choose between two RPN variants:
- either dynamic levels 1,2,3,… with infinite amount of inputs (default)
- either X,Y,Z,T levels with dropping of oldest inputs, and T keeping its value

### Test it & get it now
On NumWorks website https://my.numworks.com/python/xanderleadaren/rpn


### Roadmap
Here are a few ideas for improvements:

**Features**
- add a narrow no-break space every 3 digits from right
- [var] for a dedicated Conversions menu
- OVER function (mapped to shift+[exe]?)
- Study the possibility of *setting* angles to degrees/radians instead of *converting*
- [S] for stats (mean, median, quartiles, standard deviation, …)
- display large numbers as approximations instead of overflowing to the left
- switch between fixed number of d.p., scientific notation, and so on
- store to memories
- interactive “clickable” menus
- [up]/[down] arrows and PICK or DROP

**Bugs**
- shift & alpha should be deactivable
- handle operation errors (div by 0 and such)
