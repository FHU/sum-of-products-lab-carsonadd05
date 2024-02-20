def sum_of_products(list1, list2):
    if len(list1) != len(list2):
        return "Error: Lists must be the same length."

    result = sum(x * y for x, y in zip(list1, list2))
    return result

def get_integer_list(prompt):
    while True:
        try:
            integer_list = [int(x) for x in input(prompt)]
            return integer_list
        except ValueError:
            print("Error: Please enter integers only.")

# Test the function
list1 = get_integer_list("Enter the first series of integers: ")
list2 = get_integer_list("Enter the second series of integers: ")

output = sum_of_products(list1, list2)
print("Output =", output)

