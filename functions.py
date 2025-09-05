def square(x):
    return x**2

print(square(2))

#lambda function
sq=lambda n:True #one-line function/anonymous function #whatever you write after return write that after colon here true
print(sq(2))

#squares2=[sq(i) for i in nums]
#print(squares2)

#map
#squares3=list(map(sq,nums))
#print(squares3)


#filter

'''final=[]
for i in nums:
    final.append((i,sq(i)))
print(final)

final2=[(i,sq(I)) for i in nums]
print(final2)

#zip 
final3=list(zip(nums,squares3))

#enumerate
for i in enumerate(nums,start=100):
    idx,value=i
    print(idx,value)'''

#filter
#L=[2,5,6,8,3,1]

x=[1,4,6,5]
print(x.sort())
print(x)

y=[2,4,6,3]
z=sorted(y)
print(z)


#take a tuple and sort it in descending order and return the sorted tuple

x=[True,False,True,True]
print(any(x))
print(all(x))