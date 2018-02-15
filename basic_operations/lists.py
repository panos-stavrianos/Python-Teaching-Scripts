# Simple lists operations
a = [5, 3, "banana", 300]  # declare and assign values
print a
print '---A---'
print a[2]  # access a value
print '---B---'
a[3] = 15  # change a value
print a
print '---C---'
a.append(6)  # Insert a new value at the end of the list
print a
print '---D---'
a.insert(2, 69)  # Insert a new value at the given index of the list
print a
print '---E---'
a.pop()  # Remove a value at the end of the list
print a
print '---F---'
a.pop(3)  # Remove a new value at the given index of the list
print a
print '---G---'
