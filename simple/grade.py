
def display_grade(m1,m2,m3,m4,m5):

    avg = ( m1 + m2 + m3 + m4 + m5 ) // 5

    if (avg >= 90):
        print("Grade A")
    elif (avg >= 75 & avg < 90):
        print("Grade B")
    elif (avg >= 60 & avg < 75):
        print("Grade C")
    elif (avg >= 50 & avg < 60):
        print("Grade D")
    else:
        print("Fail")

m1 = int(input("Enter M1 : ")) 
m2 = int(input("Enter M2 : ")) 
m3 = int(input("Enter M3 : ")) 
m4 = int(input("Enter M4 : ")) 
m5 = int(input("Enter M5 : ")) 

display_grade(m1,m2,m3,m4,m5)