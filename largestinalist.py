lst = list(map(int,input("Enter the number :").split()))
largest = lst[0]

for i in lst :
    if i > largest :
        largest = i 
print("Largest element of the list is = " , largest )