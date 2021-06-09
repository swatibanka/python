def show():
    print("i am show")

def display():
    print("i am display")
    show()

display()
show()

print("-----------------------")

def one():
    print("One")

print("Hi")
def two():
    print("Two")
    one()

def three():
    print("Three")
    one()

one()
two()
three()
print("Bye")


print("-----------------------------")

def one():
    print("One")
    two()


print("Hi")
def two():
    print("Two")


def three():
    print("Three")
    one()

one()
two()
three()
print("Bye")

print("-----------------")

def one():
    print("One")
    two()
def two():
    print("Two")
    one()

def three():
    print("Three")
    one()

one()
two()
three()
print("Bye")

