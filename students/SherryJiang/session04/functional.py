def tuple_map(x,y):
    """Can you use a map function on some tuple x with some function y"""
    map(x,y)

def multiply_by_three(a):
    for i in a:
        return i*3

x = (1,2,3,4)

tuple_map(x,y)

def string_filter(a,b):
    """Can you create a function that filters based on conditions for strings? Using the lambda instead of a defined function
    This function takes a string a, and filters for only the words that have the letter 'e' in them """
    split_string = a.split()
    filter(lambda x: #i contains the letter a, split_string)

def tuple_reduce(a):
    """Can you use a reduce function on a tuple?"""
    reduce(lambda x, y: x+y, a)

tuple = (1,2,3,4,5,6)
tuple_reduce(a)
