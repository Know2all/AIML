import pandas as pd

dataset = None

def handle_choice(choice):
    if dataset is not None:
        col = input("Enter Col Name :")
        if col in dataset.columns :
            if choice == 4:
                print(dataset[col])
            elif choice == 5:
                dataset.rename(columns={col: input("Enter New Col Name :")}, inplace=True)
                print("Renamed Successfully !")
            elif choice == 6:
                print(dataset[col].nunique(axis=1))
            elif choice == 7:
                print(dataset.size)
        else:
            print("Invalid Column")
    else:
        print("Please Create DataFrame !")

def create_df():
    global dataset
    cols = [input(f"Column Name  {i+1} :") for i in range(int(input("Enter No. Of Columns:")))]
    dataset = pd.DataFrame(columns=cols,data=[])

def add_row():
    global dataset
    new_row = []
    for col in dataset.columns:
        data = input(f"Enter {col} :")
        new_row.append(data)
    dataset.loc[len(dataset)] = new_row
    
while True:
    print("Exercise 4 : Working With DataFrame \nChoices are:")
    print("1.Create data frame  \n2.Add New Row \n3.Print DF \n4.Retreive Specific Column \n5.Rename Column \n6.Unique Values \n7.Size of an dataset")
    choice:int = int(input("Enter Choice : "))
    if choice == 1:
        create_df()
    elif choice == 2:
        add_row()
    elif choice == 3:
        print(dataset)
    elif choice in [4,5,6,7]:
        handle_choice(choice)
    else:
        print("Exiting..")
        exit()