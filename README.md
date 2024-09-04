# code-challange-week-1-phase-3

This repository contains a collection of Python functions and examples to demonstrate various programming concepts. Below is an overview of the provided code and its functionalities.

## Functions

## `add_numbers(num1, num2)`

#Adds two numbers and returns the result.

print(add_numbers(1, 2))  # Output: 3

## is_even(number)

Checks if the number is even
def is_even(number):
    return number % 2 == 0
print(is_even(2))

## Function: reverse_string

Reverses the given string.
print(reverse_string("hello")) and it will give an output: "olleh"

## Decorators

A decorator that prints decorator applied before calling the wrapped function.

def apply_decorator(func):
    return decorator_func(func)
print(apply_decorator(lambda x: x + 1)(2))


## Sequences: Sort List of Tuples 
Sorts a list of tuples by the second element of each tuple.

def sort_by_age(list_of_tuples):
    return sorted(list_of_tuples, key=lambda x: x[1])
print(sort_by_age([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))

## Car Class
A simple class to represent a car with attributes for make, model, and year, and a method to display its information.

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def display_info(self):
        print(f"Car Make: {self.make}, Model: {self.model}, Year: {self.year}")
print(Car("Toyota", "Camry", 2022).display_info())

## How To Run Code
1.Execute the file using Python:

2.Run these comand in the terminal :python3 lib/python.py

3.The results will be printed to the console.