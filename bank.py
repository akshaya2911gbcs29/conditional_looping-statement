initial=int(input("Enter the initial amount:"))
print("---Menu---")
print("1.Deposit")
print("2.Withdraw")
choice=int(input("Enter your choice"))
if choice ==1:
    deposit=int(input("Enter the deposit amount:"))
    if deposit>=1000:
        print("Balance:",initial+deposit)
    else:
        print("Needs sufficient amount to deposit")
        print("Balance:",initial)
elif choice ==2:
    withdraw=int(input("enter the withdraw amount:"))
    d=initial-withdraw
    if d<1000:
       print("Balance:",d)
       print("Balance must be greater than 1000")
       print("Updated balance:",initial)
    else:
        print("Balance:",d)
else:
    print("Invalid choice")
