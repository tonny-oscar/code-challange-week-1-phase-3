#Function: add_numbers
def add_numbers(num1, num2):
    return num1 + num2

#Function: is_even 
def is_even(number):
    return number % 2 == 0

#Function: reverse_string
def count_vowels(text):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in text if char in vowels)

def count_vowels(text):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in text if char in vowels)

#Function: calculate_factorial
def calculate_factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

#Function: decorator_func
def decorator_func(func):
    def wrapper(*args, **kwargs):
        print("Decorator Applied")
        return func(*args, **kwargs)
    return wrapper

def apply_decorator(func):
    return decorator_func(func)

#Sequences: Sort List of Tuples 
def sort_by_age(list_of_tuples):
    return sorted(list_of_tuples, key=lambda x: x[1])

def merge_dicts(dict1, dict2):
    merged_dict = dict1.copy()
    for key, value in dict2.items():
        if key in merged_dict:
            merged_dict[key] += value
        else:
            merged_dict[key] = value
    return merged_dict

#Object-Oriented Programming: Class Creation 
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car Make: {self.make}, Model: {self.model}, Year: {self.year}")
