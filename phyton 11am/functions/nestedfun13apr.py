def outer(idno, name, salary):
    print("Employee IdNo:", idno)
    print("Employee Name:", name)
    print("Employee Salary:",salary)
    pf = 500
    def inner(idno, name, salary):
        nonlocal pf
        pf = 300
        totalsal = salary+pf
        print("New Total Salary = ",totalsal)
    inner(101,"Aira",5000)
    print("Pfund = ",pf)
    saving = pf*2
    print("Total Savings =",saving)
outer(101,"Aira",5000)
print("Thanks")

























print("-------------------------")

def outer(idno, name, salary):
    print("Employee IdNo:", idno)
    print("Employee Name:", name)
    print("Employee Salary:",salary)
    pf = 500
    def inner(idno, name, salary):
        nonlocal pf
        pf = 300
        totalsal = salary+pf
        print("New Total Salary = ",totalsal)
    inner(101,"Aira",5000)
    inner(102,"Advik",6000)
    print("Pfund = ",pf)
    saving = pf*2
    print("Total Savings =",saving)
outer(101,"Aira",5000)
outer(102, "Advik",6000)
print("Thanks")
