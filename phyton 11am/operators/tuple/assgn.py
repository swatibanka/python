a,b,c = "nos"
print(a)
print(b)
print(c)

nos = (10,)
no = (nos*3)
print(no)

#4
t1 = (1,20,39,48,67)
#t1[1] = 23
#print(t1)

#6
t1 =5,
print(type(t1))

#11
a,b,c = (10,20,30)
print(a,"\t",b,"\t",c,"\t")

#12
#a,b = 5,7,3,1
#print(a,b)

#13,14
x = 12,34,56
p,q,r = x
print(p)

x = 12,34,56
#p,q,r,s = x
#print(r)
#print(s)

#16
t1 = (i*i for i in range(1,5))
for  i in t1:
    print(i, end = "\t")