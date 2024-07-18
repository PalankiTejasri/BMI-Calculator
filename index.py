Height=float (input ("Enter your height in centimeters: "))
Weight=float (input ("Enter your Weight in Kg: "))
Height=Height/100
BMI=Weight/(Height*Height)
print ("your Body Mass Index is: ", BMI)
if (BMI>0):
    if (BMI<=16):
        print ("you are severely underweight")
        for row in range (7):
            for col in range (5):
                if row not in {0,6} and col in {0,4}:
                    print ("*", end=" ")
                elif row in {0,6} and col not in {0,4}:
                    print ("*", end=" ")
                else:
                    print (" ", end=" ") 
            print ()
    elif(BMI>=16 and BMI<=18.5):
        print ("you are underweight")
        for row in range (7):
            for col in range (6):
                if row in {5} and col in {2}:
                    print ("*", end=" ")
                if row in {4} and col in {1,3}:
                    print ("*", end=" ")
                elif row in {2} and col in {5}:
                    print ("*", end=" ")
                elif row in {3} and col in {4}:
                    print ("*", end=" ")
                else:
                    print (" ", end=" ")
            print ()
    elif(BMI>=18.5 and BMI<=25):
        print ("you are Healthy")
        for row in range (8):
            for col in range (8):
                if row not in {0,7} and col in {0,7}:
                    print ("*", end=" ")
                elif row in {0,7} and col not in {0,7}:
                    print ("*", end=" ")
                elif row in {4} and col in {2}:
                    print ("*", end=" ")
                elif row in {2,5} and col in {3}:
                    print ("*", end=" ")
                elif row in {2,5} and col in {4}:
                    print ("*", end=" ")
                elif row in {4} and col in {5}:
                    print ("*", end=" ")
                else:
                    print (" ", end=" ")
            print ()
    elif(BMI>=25 and BMI<=29.9):
        print ("you are overweight")
        for row in range (7):
            for col in range (8):
                if row not in {0,6} and col in {0,7}:
                    print ("*", end=" ")
                elif row in {0,6} and col not in {0,7}:
                    print ("*", end=" ")
                elif row in {2,4} and col in {3}:
                    print ("*", end=" ")
                elif row in {2,4} and col in {4}:
                    print ("*", end=" ")
                elif row in {4} and col in {2}:
                    print ("*", end=" ")
                elif row in {4} and col in {5}:
                    print ("*", end=" ")
                else:
                    print (" ", end=" ")
        
            print ()
    else: 
        print ("you are under obesity condition")
        for row in range (7):
            for col in range (5):
                if row in {1,5} and col in {0,4}:
                    print ("*", end=" ")
                elif row in {2,4} and col in {1,3}:
                    print ("*", end=" ")
                elif row in {3} and col in {2}:
                    print ("*", end=" ")
                else:
                    print (" ", end=" ")
        
            print ()
else:
    print ("enter valid details")
