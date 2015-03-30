def list_exponent(x,y):
    """Can you take a list x and apply an exponent of y to each of the items in the list using list comprehension?"""
    exponent_list = [i**y for i in x]
    print exponent_list


def list_conditions(a,b,c):
    """Can you take a list of numbers from a certain range and find only ones that are divisible by two chosen numbers"""
    divisible_list = [x for x in range(a) if x % b == 0 and x % c == 0]
    print divisible_list

list_conditions(16,2,3)

def set(x):
    """Can you create a set out of a range of numbers 0 to x-1"""
    new_set = {x for x in range(x)}
    print new_set
