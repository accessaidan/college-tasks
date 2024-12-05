import pandas as pd
import matplotlib.pyplot as plt

student_df = pd.DataFrame(columns = ["ID","Name","Grade"])

#Save dataset to CSV
def save_to_csv(df, filename="students.csv"):
    df.to_csv(filename, index = False)
    print(f"Dara saved to {filename}.")

def load_from_csv(filename="students.csv"):
    try:
        return pd.read_csv(filename)
    except FileNotFoundError:
        print("File not found, startinh with an empty dataset.")
        return pd.DataFrame(columns=["ID","Name","Grade"])

def add_student(df):
    point("\n#Add Student")
    try:
        student_id = int(input("Enter student ID: "))
        if student_id in df["ID"].values:
            print("Error: Student ID already in database.")
            return
    
        name = input("Enter name: ")
        if name in df["Name"].values:
            print("Error: Duplicate name detected. Continuing...")
        
        grade = float(input("Enter grade 90-100: "))
        if grade >= 0 and grade <= 100:
            df.loc[len(df)] = {"ID": student_id, "Name":name, "Grade": grade}
            print("Student added successcully")
        else:
            print("grade must be between 0 and 100")
    except ValueError:
        print("Please enter numeric values for ID and Grade.")

def analyse_grades(df):
    print("\n#Analyse Data")
    if df.empty:
        print("No data available. Add a student or load from CSV.")
        return
    print(f"Highest Grade: {df['Grade'].max()}")
    print(f"Highest Grade: {df['Grade'].mean():.2f}")
    print(f"Highest Grade: {df['Grade'].min()}")




while True:
    print("\n MENU:")
    print("1. Save/load CSV")
    print("2. Add Student")
    print("3. Analyse Data")
    print("4. Sort students")
    print("5. Plot Grades")
    print("6. Plot grade distrobution")
    print("7. Plot grade histogram")
    print("8. Exit")

    choice = input("\nChoose an option:")
    if choice == "1":
        print("\n#Save or Load Data")
        action = input("Enter 'save' to save or 'load' to load data: ").strip().lower()
        if action == "save":
            save_to_csv(students_df)
        elif action == "load":
            students_df = load_from_csv()
        else:
            print("Invalid input, enter either 'save' or 'load'.")

    elif choice == "2":
        add_student(students_df)
    elif choice == "3":
        analyse_grades(students_df)
    elif choice == "4":
        print("\nSort Students")
        column = input("Enter collum to sort by (ID/Name/Grade)")
        students_df = sort_students(students_df)
    elif choice == "5":
        plot_grades(students_df)
    elif choice == "6":
        plot_grade_distrobution(students_df)
    elif choice == "7":
        plot_grade_histogram(students_df)
    elif choice == "8":
        print("\nExiting program. Goodbye!\n")
        break
    else:
        print("Invalid option, please enter an option between 1-8.")




