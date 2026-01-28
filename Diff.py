set1={"green","blue"}
set2={"blue","yellow"}

set3={1,2,3,4,5}
set4={1,5,6,7,8,9}

print('The original sets are:\n',set1,'\n',set2)
print('The original sets are:\n',set3,'\n',set4)

#Symetrical differenc
setx=set1.symmetric_difference(set2)
sety=set3.symmetric_difference(set4)
print('The values after intersection are:\n',setx)
print('The values after intersection are:\n',sety)