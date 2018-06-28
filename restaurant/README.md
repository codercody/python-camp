Restaurant Tutorial
======

# Description

We will be making a restaurant interface where people can order the items on a menu, and it will calculate the cost. One sample input would be:

```text
Hello, welcome to the Cody Restaurant!

Menu:
Hamburger   $10
Pasta       $8
Soup        $4
Fries       $5

What would you like to order?

hamburger, pasta, soup

Your total is $22.
```

# Implementation

There are two main pieces of data to keep track of: your ``menu`` and the user's ``order``. ``menu`` should be kept as a dictionary:

```python
menu = {"hamburger": 10, "pasta": 8, "soup": 4, "fries": 5}
```
