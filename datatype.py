# Datatype

number = 78  # int
num = 45.09  # float
greeting = "How are you doing?" # str
Is_Programming_Interesting = True # bool
devices = ["laptop","comuter","tablet","phone"] # list
browsers = ("Firefox","Chrome","Safari","Opera") #Tuple
countries = {"Kenya","Uganda","India"} #set
employ = {
    "firstname" : "Jane",
    "age": 29,
    "nationality": "Kenyan",
    "email": "jane@gmail.com",
}  # dictionary

print(Is_Programming_Interesting)
print(num)
print(countries)
print(employ)
print(employ["firstname"])
print(employ["age"])

#determining tatatype

print(type(countries))
print(type(employ))

# Typecasting it's the process of converting one datatype to another
print(int(num))
print(float(number))
