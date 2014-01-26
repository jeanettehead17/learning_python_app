x = 5 
y = 10
z = 15

# List of our variables
numbers = [x, y, z]

# Checking if y is both greater than x and less than z
if x < y and y < z:
    print 'y is in the middle'
    numbers.append(20) # If this is true, append 20 to our numbers list

# Checking if z is less than y or less than x
elif z < y or z < x:
    print 'z is less'

print numbers

# Making a dictionary of the number of letters in each word
structures = {'lists': 5, 'dictionaries': 12}
print structures.keys()

structures['items'] = 5
print structures

