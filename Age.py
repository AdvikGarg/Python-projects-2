try:
   age=int(input('Enter your age: '))
   if age%2==0:
    print('Age is even')
   else:
       print('Age is odd')
     
except ValueError as ex:    
    print('Input was wrong!',ex)     