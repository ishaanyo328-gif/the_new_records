while True:
    print("_MARKSHEET MENU_")
    print("1. Add Student")
    print("2. View All Students")
    print("3. End Program")

    choice = input("Choose 1, 2, or 3: ")

    if choice == "1":
        roll = input("Enter Roll No: ").   #here you can enter data
    
        name = input("Enter Name: ")
        math = input("Enter Math Marks: ")


        file = open("marksheet.txt", "a")
      
        file.write(roll + "," + name + "," + math + "\n")
        file.close()
        print("Your data is saved.")

    elif choice == "2":
        print("\nSaved Marksheets:")      #this is to read the data 

        file = open("marksheet.txt", "r")

    
        print(file.read())

        file.close()

    elif choice == "3":
        print("exit the program").     
        break  

    else:
        print("Read instructions again.").      #when the user enters wrong input