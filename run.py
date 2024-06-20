x = [1,2,3,4,5,6,7,8,9,10]
y = [5,6,7,8,9,10,11,12,13,14,15]
difference_x = []
difference_y = []
symmetric = []

for item in x:
    if item not in y:
        difference_x.append(item)

for item in y:
    if item not in x:
        difference_y.append(item)

for item in x:
    if item in y:
        symmetric.append(item)

print(difference_x)
print(difference_y)
print(symmetric)