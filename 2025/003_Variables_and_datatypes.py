### Python Fundamentals

## Variables

var = 12
print(var)

## Data Types
# int
Film_No = 30
print(Film_No, "is ", type(Film_No))

# float
pi = 3.14
print(pi,"is ", type(pi))

# str
movie = 'Ojas Gambheera'
print(type(movie))
print(f"The movie {movie} is Pawan Kalyan's {Film_No}th film")

# bool
Sujeet_3rd = 'Ojas Gambheera'
print(Sujeet_3rd == movie, "is ", type(Sujeet_3rd == 'Ojas Gambheera')) # return True

# Lists : Ordered, mutable collections [1, 2, 2 ,5, 6]
Lists = [1, "Two", True, 4.0]
print(Lists)

print("Lists Length is ", len(Lists)) # prints the lenght of Lists
print("0th index element", Lists[0])
print("3rd index element is ", Lists[3])

print("Slicing the Lists", Lists[1:3]) # excludes right index while slicing and includes the left index.
print(Lists[2:])

print("Reverse indexing", Lists[-1]) # starts with -1
print("Reverse slicing", Lists[:-2]) # sliced the right most and excluded -2 index and then prints the remaing elements
print(Lists[:-3])
print(Lists[-3:-1]) # here in reverse slicing left most is excluded and right most is included

print(Lists.append("Five"))  # appends which adds element in last
print(Lists)
print(Lists[4])
print(Lists.pop(4))
print(Lists)
# and many more which can be checked online or documentation for requirements

# Tuples : Ordered, immutable collection eg: (1, 2, 3,4)
Tuples = (1, 4 ,3, 2, 7, 5 ,5)
print(Tuples)

# Sets : unordered collectino of unique elemnents eg: {1, 2 ,4,56, 78}
set  = {2, 56, 78, 23, 12, 23}
print(set) # prints randomly without following the given order and prints by ignoring duplicte entries

# Dictionaries : Keys and Values
AA = {"Movie":"Dangal", "year":2016, "Collections": "2000+", "Rank":1}
print(AA)
print(AA.keys())
print(AA.values())
