#find the minimum and maximum age
min_age=100
min_name=""
for record in details:
    age=record["age"]
    name=record["name"]
    if age<min_age:
        min_age=age
        min_name=name
print("Minimum age",min_age,min_name)

#maximum age and name
max_age=0
max_name=""
for record in details:
    ages=record["age"]
    name=record["name"]
    if age>max_age:
        max_age=age
        max_name=name
print("maximum age",max_age,max_name)

def get_age(record):
    return record["age"]