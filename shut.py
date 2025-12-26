import os

ans=(input('Do you want to shut the system yes/no: '))

if ans=='no':
    exit()
else:
    os.system('shutdown /s /t 1')    