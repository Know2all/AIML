import pandas as pd

dataset = pd.read_csv("dataset/students.csv")

def menu():
    print("- - - - - - Challenge 1 - - - - - -")
    print("\nChoices are :\n")
    print("1.Get 20 Records")

def handle(choice):
    if choice == 2:
        print(dataset.dtypes)
    elif choice == 3:
        print(f"Columns : {dataset.columns} , Count : {len(dataset.columns)}")
    elif choice == 4:
        print(f"Dimension of dataset is {dataset.ndim}")
    elif choice == 5:
        print(f"1. Using Group BY Method")
        col = input("Enter Col Name to Group")
        if col in dataset.columns:
            print(dataset.groupby(col).value_counts())
        else:
            print("Invalid Column")
        
        print(f"2. Using N Largest Method")
        col = input("Enter Col Name :")
        if col in dataset.columns:
            print(dataset.nlargest(10,columns=[col]))
        else:
            print("Invalid Column")
    
    elif choice == 6:
        col = input("Enter Col Name :")
        print(f"Basic Statistics : {dataset[col].describe()}")

    elif choice == 7:
        startRow,endRow = map(int,input("Enter Filtering by Index :").split(" "))
        print(f"Filtering Records :\n{dataset.loc[startRow:endRow,[input(i) for i in dataset.columns]]}")

    elif choice == 8:
        row = int(input("Enter Row :"))
        print(f"Dataset of given row is :{dataset.loc[row]} ")
    
    

while True:
    menu()
    choice:int = int(input("Enter Choice : "))
    if choice == 1:
        print(dataset.head(20))
    elif choice in [2,3,4,5,6,7,8]:
        handle(choice)
    else:
        print("System Exitting ...")
        exit()
