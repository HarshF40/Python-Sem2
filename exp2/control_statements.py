age = 20

#simple
if age >=18 :
    print("Im above 18")

#if-else
if age >= 18 :
    print("Im above 18")
else :
    print("Im below 18")

#if-elif-else
if age > 18 :
    print("Im above 18")
elif age == 18 :
    print("Im 18")
else :
    print("Im Below 18")

#nested if
if age >= 18 :
    if age >- 60 :
        print("Im Old")
    else :
        print("Im young")
else :
    print("Im a kid")

print("Above 18" if age > 18 else "Not above 18")

if age > 18 and age < 30 :
    print("Im Fit")
