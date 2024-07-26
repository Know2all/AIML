import pandas as pd
import matplotlib.pyplot as plt

df  = pd.read_csv("dataset/students.csv")


def get_stds_grade():
    x = df['Grade'].unique()
    y = df['Grade'].value_counts()

    print(y)

    plt.figure(figsize=(8, 8))
    plt.pie(y, labels=x, 
            autopct='%1.1f%%', shadow=True, startangle=140)
    plt.title('Grade Wise Student Count')
    plt.show()

def students_mark():

    y = df['Total'].value_counts().sort_index()
    x = y.index

    plt.figure(figsize=(10, 6))
    plt.bar(x, y)
    plt.title('Student Mark Count')
    plt.xlabel('Marks')
    plt.ylabel('Count of Students')
    plt.xticks(rotation=90)
    plt.show()

while True:
    print("Excersice 7 :\nChoices are:\n1.Students Grade Count - Pie Chart \n2.Marks Student Count - Bar Plot")
    choice = int(input("Enter Choice :"))
    
    if choice == 1:
        get_stds_grade()
    elif choice == 2:
        students_mark()
    else:
        print("System Exitting...")
        exit()