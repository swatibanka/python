#1
l1 = list(range(5))
print (l1)

#4
l2 = [10,20,30,40,50]
print(len(l2))

#5
l2 = [10,20,30,40,50]
l2[3] = 45
print(l2)

#9
l4 = [41,12,85,96,78,69]
l5 = l4[1:]
print(l5)

#10
l6 = [41,12,85,96,78,69]
l7 = l6[:1]
print(l6)

#11
l8 = [41,12,85,96,78,69]
l9 = l4[:]
print(l9)

#12
l10 = [41,12,85,96,78,69]
l11 = l4[-2:]
print(l11)

#13
#names = []
#names[0] = "stahya tech"
#print(names)

#14
names = []
names.append("ravi")
print(names)

#15
l1 = []
l1.append("A")
l1.append("B")
l1.append("C")

print(l1)

#17
l1 = [89,45,2,7,9]
l1.sort()
print(l1)

#18
#l1 = [23,'A',45,67,'e',4]
#l1.sort()
#print(l1)

#19
l1 = [5, 34,67,89]
l2 = l1
l1[2] = 12
print(l2)
print(l1)

#21-25
l1 = [[5,10],[20,10]]
print(l1[0],[-1])
print(l1[1], [0])

#28
names = ['We','are','a','family']
l1 = [n[0] for n in names]
print(l1)