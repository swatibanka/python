s1 = {10,20,30,40}
s2 = {30,40,50,60,70}

s3=s2.difference(s1)
print(s3)

s2.difference_update(s1)
print(s1)
print(s2)

print("---------------------")

s1 = {30,40}
s2 = {30,40,50,60,70}
s3 = s1.issubset(s2)
print(s3)

print("---------------------")

s1 = {10,20,30,40,50,60,70}
s2 = {30,40,50,60,70}
s3 = s1.issuperset(s2)
print(s3)

print("---------------------")
#union
s1 = {10,20,30,40,50,60,70}
s2 = {30,40,50,60,70}
print(s1|s2)

print("---------------------")
#update
s1 = {10,20,30,40,}
s2 = {30,40,50,60,70}
print(s1.update(s2))

print("---------------------")
#intersection
s1 = {10,20,30,40,}
s2 = {30,40,50,60,70}
print(s1 & s2)

print("---------------------")
#intersection.update
s1 = {10,20,30,40,}
s2 = {30,40,50,60,70}
print(s1.intersection_update(s2))

print("---------------------")
#difference
s1 = {10,20,30,40,}
s2 = {30,40,50,60,70}
print(s1 - s2)

print("---------------------")
#update
s1 = {10,20,30,40,}
s2 = {30,40,50,60,70}
print(s1.difference_update(s2))





