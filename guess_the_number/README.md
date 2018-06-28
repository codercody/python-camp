Guess the Number Tutorial
======

# Description

We will be making a guess the number game, where a random number is generated and the user has to guess it. Each time, the program must output whether the guess was too high, too low, or correct. A sample input would be:

```text
Welcome to Cody's guess the number game. I'm thinking of a number between 1 and 100, try guessing it: 40
That's too low! 80
That's too high! 55
That's too low! 57
That's correct! Good job!
```

# Implementation

First, you must generate a random mystery number for the user to guess. You can do this using the ``randint`` function from the ``random`` library:

```python
import random

mystery_number = random.randint(1, 100)
```
