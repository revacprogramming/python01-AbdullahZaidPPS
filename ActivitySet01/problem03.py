# Variables, Expressions & Statements
  
def res(hrs,rt):
  salary = hrs*rt
  return salary
hrs = float(input("Enter hours? "))
rt = float(input("Enter hourly rate: "))
s=res(hrs,rt)
print("The salary is ",s)
