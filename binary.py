dec=int(input('Enter a number to convert to binary: '))
bin=''

if dec==0:
    bin='0'
else:
    while dec>0:
        r=dec%2
        bin=str(r)+bin
        dec=dec//2
        
print('The binary conversion of the number is: ',bin)        
        
