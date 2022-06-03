list_a = [i for i in range(10)]
print(list_a)

list_b = []
for i in range(3):
    list_b.append(list_a[i])
print(list_b)

list_c = [list_a[i] for i in range(3)]
print(list_c)

# List slicing
list_d = list_a[0:3:1]  # start, end index not inclusive, step (optional); : separated
print(list_d)
list_d[0] = -100
print(list_d)

