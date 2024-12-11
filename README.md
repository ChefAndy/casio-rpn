# Reverse Polish Notation on NumWorks

Python script for the scientific Numworks calculator, enabling to type in RPN in a graphical user interface.

### A few keys
The basic operations are mapped to the usual buttons.

The [Toolbox] button allows the user to display some other hotkeys, including RPN-specific functions as ROLL, SWAP or DUPlicate, or prime factorisation or converting degrees from/to radians, or Fahrenheit/Celsius.

![canvas](https://github.com/user-attachments/assets/a70bac27-a74f-4a62-a662-8d5162ed5462)

### Two RPN stack variants
On [x,n,t] key, the user may choose between two RPN variants:
- either dynamic levels 1,2,3,… with infinite amount of inputs (default)
- either X,Y,Z,T,L levels with dropping of oldest inputs, and L keeping the last value

### Test it & get it now
On NumWorks website https://my.numworks.com/python/xanderleadaren/rpn


### Roadmap
Here are a few ideas for improvements:

**Features**
- % of a quantity
- (n) ROLL up/down
- [Ans] maps for a LastX function
- [S] for stats (mean, median, quartiles, standard deviation, …)
- store to memories

**Bugs**
- shift & alpha should be deactivable
- handle operation errors (div by 0 and such)
