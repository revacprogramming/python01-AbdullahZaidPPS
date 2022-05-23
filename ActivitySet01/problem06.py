# Loops & Iterators

largest = 0
smallest = 0
while True:
    try:
        num = input("Enter a number: ")
        if num == "done":
            break
        n=int(num)
        if largest==0 or n>largest:
            largest=n
        elif smallest==0 or n<smallest:
            smallest=n
    except:
        print("Invalid input")
print("Maximum is", largest)
print("Minimum is", smallest)