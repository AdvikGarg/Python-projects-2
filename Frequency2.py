
Frequeny={'Codingal':3, 'is':2, 'best':2, 'for':2, 'coding':1}

ans=(input('Do you want to check the frequency: Yes/No\n'))

if ans=='No':
    print('Ok!')
if ans=='Yes':
    x=2
    res=0
    for i in Frequeny:
        if Frequeny[i]==x:
           res+=1

    print('The Frequency of the a is: ',res) 


     