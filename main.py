def sum_of_products(list1,list2):
    if len(usr1_list) != len(usr2_list):
        return "Are these the same length?"
    
    listsum = 0 

for i in range(len(usr2_list)): 
    listsum += usr1_list[i] * usr2_list[i]
    return listsum 

if __name__ == '__main__':
    usr1_list = input().split()
    usr2_list = input().split()

    usr1_list = [int(num) for num in usr1_list]
    usr2_list = [int(num) for num in usr2_list]

    SumofLists = sum_of_products(usr1_list, usr2_list)
    print(SumofLists)
