#pg 109, 5
st1_sub1 =int(input("enter student mark :"))
st1_sub2 =int(input("enter student mark :"))
st1_sub3 =int(input("enter student mark :"))
st2_sub1 =int(input("enter student mark :"))
st2_sub2 =int(input("enter student mark :"))
st2_sub3 =int(input("enter student mark :"))

print("           ","s1   ","s2   ","s3   ","Total    ","Avg")
print("           ","--   ","--   ","--   ","-----    ","---")
st1_marks = [st1_sub1,st1_sub2,st1_sub3]
st2_marks = [st2_sub1,st2_sub2,st2_sub3]
total_s1 = (st1_sub1+st1_sub2+st1_sub3)
total_s2 = (st2_sub1+st2_sub2+st2_sub3)
Avg1 = total_s1/len(st1_marks)
Avg2 = total_s2/len(st2_marks)

print(*("student1",st1_sub1,st1_sub2,st1_sub3,total_s1,Avg1), sep="    ")
print(*("student2",st2_sub1,st2_sub2,st2_sub3,total_s2,Avg2), sep="    ")

#WAP for book shop

Total_number_of_books = 5
book_name = ["the secret", "rich dad poor dad","how to win friends","think and grow rich","you can win"]

search_book = input("Enter the book name")

#using in operator
if search_book.lower() in book_name:
    print("Found")

else:
    print("not found")

#pg 109, 3
student_mark1 =int(input("enter student mark 1:"))
student_mark2 =int(input("enter student mark 2:"))
student_mark3 =int(input("enter student mark 3:"))

print("s1   ","s2   ","s3")
print("--   ","--   ","--")
# * is used to remove ", "
print(*(student_mark1,student_mark2,student_mark3), sep="    ")



