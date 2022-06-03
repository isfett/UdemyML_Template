my_value1 = 27
my_value2 = "Jan"

print("Age: ", my_value1, " Name: ", my_value2)
print(f"Age: {my_value1} Name: {my_value2}")  # should get preferred

print("Age: {} Name: {}".format(my_value1, my_value2))

print("Age: %d Name: %s" % (my_value1, my_value2))
