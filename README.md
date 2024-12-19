# Reverse Polish Notation on NumWorks

Python script for the scientific Numworks calculator, enabling to type in RPN in a graphical user interface.

### Keystrokes
- Basic operations are mapped to the usual buttons.
- [Toolbox] button allows the user to display some other hotkeys, including RPN-specific functions as ROLL, SWAP or DUPlicate, or prime factorisation or converting degrees from/to radians, or Fahrenheit/Celsius.

![canvas](https://github.com/user-attachments/assets/8fee3a04-c9ed-4026-9050-e00fa4f0d427)

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
- [Ans] maps for a LastX function
- add a narrow no-break space every 3 digits from right
- display large numbers as approximations instead of overflowing to the left
- [S] for stats (mean, median, quartiles, standard deviation, …)
- [var] for a dedicated Conversions menu
- store to memories
- interactive “clickable” menus

**Bugs**
- fix text background on odd/even lines
- shift & alpha should be deactivable
- handle operation errors (div by 0 and such)
