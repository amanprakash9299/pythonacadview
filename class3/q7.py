list1=[25,14,65,22,489,285]
l1=[]
l2=[]

for x in list1:
    if x%2==0:
        l1.append(x)
    else:
        l2.append(x)

print("even list",l1)
print("odd list",l2)
