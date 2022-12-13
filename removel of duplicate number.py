#removel of duplicate number
n=int(input('enter no of list elements'))
list=[]
for i in range(n):
    x=input("enter the elemengt:")
    list.append(x)
list1=[]
for j in list:
    if j  not in  list1:
        list1.append(j)
print(list1)        
        
