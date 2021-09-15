a = int(input("geef een gehele gatal in"))
b = int(input("geef een gehele getal in"))

if a > b:
    max = a
    min = b
    print("het grotste getal is",max)
elif a < b :
    max = b
    min = a  
    print("het kleinste getal",min)
else: 
    min = b
    max = a
    print("getalen zijn gelijk")     

print("het miniummum is",min)
print("het maximum is ",max)