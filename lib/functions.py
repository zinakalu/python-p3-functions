#!/usr/bin/env python3

def greet_programmer():
    pass
    print("Hello, programmer!")
greet_programmer()

def greet(name):
    pass
    print(f"Hello, {name}!")
greet("Naureen")

def greet_with_default(name="programmer"):
    pass
    print(f"Hello, {name}!")
greet_with_default("Sunny")

def add(num1, num2):
    pass
    return num1 + num2
add(45, 55)

def halve(number):
    pass
    if type(number) != int and type(number) != float:
            return None
    return number/2