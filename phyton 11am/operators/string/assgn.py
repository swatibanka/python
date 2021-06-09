print("______________")
s1 = "sathya technology"

odd_str = ""
even_str = ""

for i in range(len(s1)):
    if i % 2 == 0:
        even_str = even_str + s1[i]
    else:
        odd_str = odd_str + s1[i]
    
print (even_str)
print (odd_str)


