---
layout: post
title:  "Scope"
date:   2019-04-04 17:21:19 -0700
categories: week2
---
# Scope: (Not like the mouthwash)
One of the more challenging concepts in programming is scope. Scope refers to the context in which a particular set of instructions are being carried out. There are many levels of scope are related largely to how the computer finds things. This gets really complicated, but it is very important. I think a good way to think of it is to begin with a metaphor:

Right now, we're in a city: Seattle (or if you're in another city, then whatever that city is). There are a lot of different spaces within that city, but everything is within the city. Some of those spaces are public and others are private. For instance, public parks are totally public. Anyone can go into these spaces, use all of the equipment, have barbecues, etc. Some of those spaces are private. For instance, Seattle also has private houses. Now while I can go into the park and use all the resources there, I couldn't go into some random person's house and use their stuff. They'd be angry. I'd probably get arrested. The person can use their own stuff, but I can't. If I want something from their house, I'd have to ask and have them give it to me.

We might say that the park, being outside of the house, is in the global environment. The house, on the other hand, is a local environment. Anyone who lives in any house can still access the park. Only people who live in their house can access the stuff in the house unless there is some way to take the stuff out of the house.

Scope is a little bit like this. In a program you will have "names" (functions, classes, variables, objects, etc.) in various spaces from the global space to various local spaces. If you've ever received a "Name Error" in Python, it probably means that you are trying to access a name that is not accessible in that particular space or context.

Now applying this metaphor to coding really specifically. Consider the following code:

```python
some_number = 27

def is_odd(num):
   if num % 2 == 0:
      return False
   else:
      return True

if __name__ == "__main__":
   if is_odd(some_number):
      print("It's odd")
   else:
      print("It's even")
   print(num) # This won't work will throw a Name Error
```

The variable "some_number" exists in the global space. That's why I can access it in the conditional at the bottom of the program. However, ```print(num)``` will not work because num only exists inside of the ```is_odd()``` function and is not accessible outside of that function unless it is returned as output. 

Variables that can be accessed from anywhere in the program are called **global variables**. Variables that can only be accessed within a class or function are called local variables and only exist within that scope. Let's look at a more complicated example:

```python
import requests
# Constants
BASE_URL = 'https://en.wikipedia.org/w/api.php?action=search&search=list'

# functions
def search(term: str) -> str:
   # this resp is a local variable
   resp = requests.get(BASE_URL + '&srsearch={}'.format(term))
   if resp.status_code == 200:
      return resp.text
   else:
      return "Error"

if __name__ == '__main__':
   print("Hello, Friend! I'm here to help you find stuff on
      Wikipedia.")
   search_for = input("Please enter a search term: ")
   # this resp is a global variable but it is not the 
   # same as the local variable of the same name within
   # the search function.
   resp = search(search_for)
   if resp != "Error":
      print("Your search was successful")
      print(resp)
   else:
      print("I'm sorry. Try again later.")
      print(resp)
```
There are a few names to cover:

* BASE_URL: This is a global variable. It is also a "constant." While Python doesn't enforce constants in the same way that C++ or Java does, it is conventional to name variables that are set once and never change will all capital letters. This tells future programmers that they shouldn't reset the value of this variable.
* search(): search is the name of our function. It is declared in the global context, so it can be accessed anywhere in our program after it is declared.
* term: This is a variable that is a parameter of search(). it is only accessible within the scope of the search function. You'll notice the funky ```: str``` and ```-> str```. These are new features of Python. Unlike C++ and Java, Python is not strongly typed. This means that you can change the type of data a variable holds. This is generally considered bad practice, so they've added a way to give developers a hint as to what type of variable these are going to be. The ```: str``` means that term ought to be a string (not enforced). The ```-> str``` tells us that the function will return a string (again, not enforced). 
* resp: This variable is local to ```search()``` and cannot be accessed outside of search. resp happens to be the object returned from the ```requests.get()``` method.
* search_for: this is a string that exists in the global context, but notice that if the condition (ie. this program is being run as the main program rather than a subprocess within another program) is not satisfied the variable will never be created.
* resp: this variable is also a string (ie. the output of ```search_for()```). It is also only created if the condition passes. However, notice that this program has two variables of the same name. This is not good practice, but it does illustrate the importance of scope. The first resp is a local varible within the function. The second resp is a global variable to the program. They do not refer to the same thing or the same space in memory even though they are of the same name. The only reason I can name two variables the same thing is because they are in a different scope. If they were in the same scope, there would only be one variable, and it would be reassigned a new value. 

The key to understanding scope is to consider if the named entity (variable or function) is inside of a function or class or is in the global space of the program. This is an important prerequisite to begin thinking about Objects in a serious way. On the next page, we'll talk about objects.