dict1 = {1:2}
print(dict1)
print(1 in dict1)

dict2 = {"Apple":1, "Banana":2, "Dog":3, "Cow":4, "Eagle":4}

max_value=0
list1=[]

for key,value in dict2.items():
    if value>max_value:
        max_value=value
        
        
for key,value in dict2.items():
    if value==max_value:
        list1.append(key)
        
list2= sorted(list1)

print(list2[0])
