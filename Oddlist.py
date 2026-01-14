list=[6,3,8,4,1,5,9,2,7]

list.sort()

odd=[]
even=[]

for i in list:
    if i%2==0:
       even.append(i)
    else:
       odd.append(i)


print(f"Odd numbers are: {odd}")
print(f"even numbers: {even}")
    


