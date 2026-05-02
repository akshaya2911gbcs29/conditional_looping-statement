sub1=int(input("Enter the mark of subject1:"))
sub2=int(input ("Enter the mark of subject 2:"))
sub3=int(input("Enter the mark of subject 3:"))
sub4=int(input("Enter the mark of subject 4:"))
sub5=int(input("Enter the mark of subject 5:"))
tot=sub1+sub2+sub3+sub4+sub5
percent=(tot*100)/500
print("Total:",tot)
print("Percentage:",percent)
if percent>=90:
    print("Grade:o")
elif percent>=80 and percent<=89:
    print("Grade:A+")
elif percent>=70 and percent<=79:
    print("Grade:A")
elif percent>=60 and percent<=69:
    print("Grade:B+")
elif percent>=55 and percent<=59:
    print("Grade:B")
elif percent>=50 and percent<=54:
    print("Grade:C")
elif percent>=0 and percent<=50:
    print("FAIL")
else:
    print("Invalid mark")


