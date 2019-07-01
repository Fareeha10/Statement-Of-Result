print("****************STATEMENT OF RESULT****************")
name = input("Name of Canditate:")
roll= int(input("Enter roll number:")) 
s1=input("Enter name of subject:")
n1=int(input("Enter marks aquired:"))
s2=input("Enter name of subject:")
n2=int(input("Enter marks aquired:"))
s3=input("Enter name of subject:")
n3=int(input("Enter marks aquired:"))
s4=input("Enter name of subject:")
n4=int(input("Enter marks aquired:"))
s5=input("Enter name of subject:")
n5=int(input("Enter marks aquired:"))
tot= n1+n2+n3+n4+n5
print("Total marks acquire:",tot)
if(tot<=500 & tot==485):
    print("Grade is A")
elif (tot<=484 & tot==450):
    print("Grade is B")
elif (tot<=449 & tot==430):
    print("Grade is C")
elif (tot<=390 & tot==370):
    print("Grade is D")
else:
    print("Grade is fail")
