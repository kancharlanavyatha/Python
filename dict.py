d={1:2, 3:4,2:5,6:7,3:5}
print(d)

print(d[3])

#dictiionary can only have hashable values

d={
    1:2,
    True:5,
    0:4,
    (2,3):4,
    "":6,
    False:7
}
print(int(True),hash(True))
print(bool(1),hash(1))

print(d)
print(len(d))