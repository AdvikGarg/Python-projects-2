num=int(input('Enter a number: '))

n=0

if num>=0:
    while num>=1:
        num=num//10
        n=n+1

else:
    num=num*-1  
    num>=0
    while num>=1:
        num=num/10
        n=n+1 
        
        
print('The number of digits in the number is: ',n)    
         
     
        
        