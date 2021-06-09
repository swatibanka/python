usernames = ["a","b","c","d","e"]
passwords = ["1","2","3","4","5"]

uname = input("Enter usernames:")
upass = input("Enter passwords:")

if uname in usernames:
    pos = usernamesi.index(uname)
    if upass ==passwords[pos]:
        print("Welcome")
    else:
        print("invalid password")

else:
    print("invalid username")