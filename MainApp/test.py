from models.Users import Users

obj=Users()
#print(obj.insert({"name":"ankit"}))
x=obj.find({"name":"praveen"})
print(x.count())
for i in x:
    print(i)
