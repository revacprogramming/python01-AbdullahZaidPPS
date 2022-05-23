# Conditional Execution

hrs = input("Enter hours? ")
rate = input("Enter rate ")
hours = float(hrs)
rt = float(rate)
if hours>40:
    sly = 1.5*(hours-40)*rt+(40*rt)
    print(sly)
else:
    sly = hours*rt
    print(sly)

