list1 = [1,2,3,4,5,6,7]

#for loop
for num in list1 :
    print(num)

for i in range(5):
    print(i)

#while loop
i = 0
while i < 5 :
    print(i)
    i+=1

while i < 10 :
    print(i)
    if i == 7 :
        i+=1
        continue
    if i == 8 :
        break
    i+=1

#nested loop
for i in range(5):
    print()
    for j in range(5) :
        print(i, end="")

# loop with else
for n in range(2, 6):
    for x in range(2, 10) :
        if n%x == 0 :
            break
        else :
            continue
