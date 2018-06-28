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

hamburger, pasta, and soup

Your total is $22.
```

# Implementation

There are three main pieces of data to keep track of: your ``menu``, the user's ``order``, and the total price (which will keep on increasing every time something is added to the order). ``menu`` should be kept as a dictionary:

```python
menu = {"hamburger": 10, "pasta": 8, "soup": 4, "fries": 5}
```

``order`` should be kept as a string. You can check if the ``order`` contains any of the menu items using ``in``:

```python
if "hamburger" in order:
    total_cost += menu["hamburger"]
```
