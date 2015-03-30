def optional(a, b=0, c=0):
    """Can you have optional variables?"""
    print(a,b,c)

optional(1)

y = [1,2,3,4]
def default(x=y):
    """Can you set anything as a default variable? """
    print x

default()
default(5)


d = {"name": "Sherry", "hometown": "San Francisco", "food": "sushi"}

def format_string():
    """Can you apply any elements into a string from a dictionary using the .format() command?"""
    "My name is {name} and I am from {hometown}. My favorite food is {food}".format(**d)    



