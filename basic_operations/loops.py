# For
for i in range(0, 5, 1):  # loop i from 0 to 3 with 1 step
    print i

print "---A----"

for i in range(5):  # exactly the same
    print i

print "---B----"

# While
i = 0
while i < 5:
    print i
    i = i + 1

print "---C----"

i = -2
while i < 5:
    print i
    if i < 0:
        break
    i = i + 1

print "---D----"


