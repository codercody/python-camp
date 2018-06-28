Mad Libs Tutorial
======

# Description

Mad Libs is a game where you customize your own story with your own inputs. Here is a sample Mad Libs story:

```text
There are many [adjective] ways to choose a/an [noun] to read. First, you could ask for recommendations from your friends and [plural noun]. Just don't ask Aunt [person in room (female)] - she only reads [adjective] books with [article of clothing]-ripping goddesses on the cover. If your friends and family are no help, try checking out the [noun] Review in The [a city] Times. If the [plural noun] featured there are too [adjective] for your taste, try something a little more low-[part of the body], like [letter of the alphabet]: The [celebrity] Magazine, or [plural noun] Magazine. You could also choose a book the [adjective]-fashioned way. Head to your local library or [a place] and browse the shelves until something catches your [part of the body]. Or, you could save yourself a whole lot of [adjective] trouble and log on to www.bookish.com, the [adjective] new website to [verb] for books! With all the time you'll save not having to search for [plural noun], you can read [number] more books!::
```

The way our program will run is, it will first print the annotated story, then it will ask for several inputs, and then it will print the final story. It should look something like this:

```text
There are many [adjective] ways to choose a/an [noun] to read. First, you could ...

[adjective] = amazing
[noun] = wall
...

There are many amazing ways to choose a/an wall to read. First, you could ...
```

# Implementation

There are two things we must keep track of: the ``story`` and the ``user_words``. Although it may sound a bit un-intuitive right now, we're going to start with the ``user_words`` and THEN write the story. So start with ``user_words`` being a list of all the empty words with their parts of speech for the user to fill in:

```python
user_words = ["[adjective]", "[noun]", "[plural noun]", ...]
```

Then, we're going to write the story with the user words entered in:

```python
story = "There are many " + user_words[0] + " ways to choose a/an " + user_words[1] + " to read. First..."
```

Then print out the ``story``. It should print the entire Mad Libs story with none of the blanks filled in.

Next, we need to get the user to input all of these words. The way we can do this is using the ``input`` function. Since we need to do this for each of the words, we can accomplish this by looping through all the ``user_words`` and receiving the proper inputs:

```python
for i in range(len(user_words)):
  user_words[i] = input(user_words[i] + " = ")
```

Finally, we need to print out the story with the ``user_words`` added to the story. We can do this by copying the line we already wrote above and printing:

```python
story = "There are many " + user_words[0] + " ways to choose a/an " + user_words[1] + " to read. First..."
print (story)
```
