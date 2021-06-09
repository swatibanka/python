d1 = {}
print(type(d1))

d1 = dict()
print(type(d1))

d1 = {101: "abc", 102:"def"}
d1[103] = "ghi"
print(d1)

d1 = {101: "abc", 102:"def"}
#del d1["ghi"]
print(d1)

d1 = {101: "abc", 102:"def"}
del d1[102]
print(d1)

d1={
101:"RaviKumar",
102:"Vishnu"}
for i in d1.keys( ):
    print( i )

d1={
101:"RaviKumar",
102:"Vishnu"}
for i in d1.items():
    print(i)

d1={
101:"RaviKumar",
102:"Vishnu"}
for i in d1.values():
    print(i)

d1={
101:["Ravi",2000.0]}
for i in d1:
    print( i )

d1={
101:["Ravi",2000.0]}
for i, j in d1.items():
    print(i, "\t",j)

d1={
101:["Ravi",2000.0]}
#for i, j in d1.items():
    #print(i, end="\t")
    #for k in j():
        #print(k, end='\t')

d1 = {
    "HR":{
        101:"Ravi",
        102:"Lakshmi"
    }
}

for x in d1:
    print(x,d1[x])

d1 = {101:["Ravi",1000],102:["Lakshmi",2000]}
print(d1[102])

#que no 19:doubt
d1 = {
    "HR":{
        101:"Ravi",
        102:"Lakshmi"
    },
    "Production":{
        201:"Vishnu",
        202:"Avinash"}
    
}
#print(d1[0]["HR"])

departement = {468:"csc", 274:"IT", 456:"ETC"}
departement[304] = "Civil"
print(departement)

print("Code    ","Dept")
for x in departement:
    print(x,"\t",departement[x])

for x in departement:
    y = 468
    if x==y:
        print(departement[x])

for x,y in departement.items():
    z = "IT"
    if z==y:
        print(x)
