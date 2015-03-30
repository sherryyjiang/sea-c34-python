#item 1
chris_dict = {"name": "Chris", "city": "Seattle", "cake": "chocolate"}

print chris_dict

del chris_dict["cake"]

chris_dict["fruit"] = "Mango"

for k in chris_dict.items():
    print k

for v in chris_dict.values():
    print v


"cake" in chris_dict.items()

"Mango" in chris_dict.values()


#item 2
dictionary = {}

i = range(16)
j = []

for x in range(16):
    h = hex(x)
    j.append(h)

for i,j in zip(a,b):
    dictionary[i] = j


#item 3

for k, v in chris_dict.items():
    chris_dict[k] = v.count('a')

#item 4
    """Create sets s2, s3 and s4 that contain numbers from zero through twenty, divisible 2, 3 and 4.
    Display the sets.
    Display if s3 is a subset of s2 (False)
    and if s4 is a subset of s2 (True). """

list1 = []
for i in range(21):
    if i % 2== 0:
        list1.append(i)

list2 = []
for i in range(21):
    if i % 3== 0:
        list2.append(i)

list3 = []
for i in range(21):
    if i % 3== 0:
        list3.append(i)

s2 = set(list1)
s3 = set(list2)
s4 = set(list3)

print s2
print s3
print s4

s3.issubset(s2)

s4.issubset(s2)

#item 5 

python = []

for i in "Python":
    python.append(i)
    
s5 = set(python)

s5.update('i')

"""Create a frozenset with the letters in ‘marathon’
display the union and intersection of the two sets."""

marathon = []

for i in "marathon":
    marathon.append(i)
    
fs = frozenset(marathon)

s5.union(fs)

s5.intersection(fs)
