#slicing
s="parampreet"
n=len(s)

#+ve: 0 to 9(n-1)
#-ve:-1 to -n

ape=s[3:8:2] 
print(ape)

#start:end:step
rev=s[-6:-11:-1]
print(rev)

x=s[::-1] #start=0, stop=n-1 , step=-1 (this will give reverse of string)
print(x)
y=s[::-6]
print(y)


#LISTS
nums=[2,4,6,8,10]

nums.append(12) #adds element at the end of the list
nums.insert(2,14) #can add wherever you want
print(nums)
nums.insert(-1,8) #list.insert(index, value) inserts value before the given index.
print(nums)

#LIST COMPREHENSION
evens=[]
for i in range(2,11,2):
    evens.append(i)
print(evens)

myevens=[i for i in range(2,11,2)] #puts the elements in a listsquare brackets without having to append each element
print(myevens)

#next 
myevens = [i for i in range(2, 11, 2)]
it = iter(myevens)

print(next(it))   # 2
print(next(it))   # 4

#iter 
'''What iter() does

iter(obj) returns an iterator object from obj.

An iterator is something you can call next() on to get elements one by one.'''
nums = [10, 20, 30]
it = iter(nums)   # turn list into iterator

print(next(it))   # 10
print(next(it))   # 20
print(next(it))   # 30
#print(next(it))   # ERROR (StopIteration)


#TUPLES
#tuples are immutable.
#CRUD- CREATE->READ->UPDATE ->DELETE    we cannot perform create and update in tuple

nums=[]
nums2=()

#SETS
#are unordered
#no duplicates

x=[1,1,2,2,3,3] #length is 6 list
y=(1,1,2,2,3,3) #length is 6 tuple
z={1,1,2,2,3,3} #length is 3 set
print(len(x))
print(len(y))
print(len(z))

x=[1,[2,3],(4,5),{6,7}]
print(x)

y={1,[2,3],(4,5),{6,7}} #unhashable
print(y)

z=(1,[2,3],(4,5),{6,7})
print(z)

#cannot be changed-immutable-hashable:int,float,string,bool,tuple
#can be changed-mutable-unhashable:list,set,dict

#sets are unordered hence have no index

#SET COMPREHENSION

x=set()
for i in range(1,8):
    x.add(i)
print(x)

y={(i,i**2) for i in range(1,8) if i%2==0} #created a tuple to understand original number and then its square
print(y)