#REMOVE PASS AND FIX THE FUNCTION
#change to test push and forks
def sum_of_products(list1, list2):
    if len(list1) != len(list2):
        return "Error: Lists must be the same length."

    result = sum(x * y for x, y in zip(list1, list2))
    return result

# Test the function
list1 = [int(x) for x in input("Enter the first series of integers: ")]
list2 = [int(x) for x in input("Enter the second series of integers: ")]

output = sum_of_products(list1, list2)
print("Output =", output)