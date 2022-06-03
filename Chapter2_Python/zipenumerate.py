list_a = [100.0, 200.0, -10.0]  # bank_account
list_b = [False, False, True]  # is_broke

# Index
for i in range(len(list_a)):
    print(list_a[i], list_b[i])

print("")

# Values for multiple iterables
for val_a, val_b in zip(list_a, list_b):
    print(val_a, val_b)

print("")

# Index and value
for i, val in enumerate(list_a):
    print(i, val)

print("")

# index and values for multiple iterables
for i, (val_a, val_b) in enumerate(zip(list_a, list_b)):
    print(i, val_a, val_b)
