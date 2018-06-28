Calculator Tutorial
======

# Description

We are going to make a calculator that will perform a few basic operations. Namely, this calculator will have the following functions:

```text
add x y - gives x+y
subtract x y - gives x-y
multiply x y - gives x*y
divide x y - gives x/y
negative x - gives -x
inverse x - gives 1/x
sqrt x - gives sqrt(x)
```

A sample input would be:

```text
Hello, welcome to Cody's Calculator.

enter a calculation: add 2 3
5.0
enter a calculation: multiply 7 6
42.0
enter a calculation: inverse 3
0.33333
enter a calculation: asrarruereub
invalid input
```

# Implementation

First, print out a welcome message to make the interface user-friendly. Then, wrap everything in a ``while True`` loop to ensure it runs forever. Finally, we will use the following code to get the operations:

```python
operations = input("enter a calculation: ").split()
operation = operations[0]
if operation == "add":
  x, y = operations[1], operations[2]
  print (x + y)
elif operation == "subtract":
  x, y = operations[1], operations[2]
  print (x - y)
...
```
