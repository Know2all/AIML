import pandas as pd

df = pd.read_csv("dataset/students.csv")

def handle(choice):
    choices = [1,2,3,4,5,6]
    if choice == 1:
        print(f"Describe about dataset : \n{df.describe()}")
    elif choice in choices:    
        col = input("Enter Column Name :")
        if col in df.columns:
            if choice == 2:
                print(f"Unique Values : \n{df[col].unique()}")
            elif choice == 3:
                print(f"value counts : \n{df[col].value_counts()}")
            elif choice == 4:
                print(f"Group By : \n{df.groupby(col).value_counts()}")
            elif choice == 5:
                n = int(input("How Many You Want ? \nPlease Enter :"))
                print(f"N-highest : \n{df.nlargest(n,col)}")
            elif choice == 6:
                n = int(input("How Many You Want ? \nPlease Enter :"))
                print(f"N-Lowest : \n{df.nsmallest(n,col)}")                
        else:
            print("Invalid Column")
    elif choice in [7,8]:
        if choice == 7:
            print(f"Total Rows : {df.size}")
    else:
        print("System exiting ..")
        exit()

while True:
    print("Choices Are: \n1.Describe \n2.Unique Marks \n3.Value Count \n4.Group By \n5.N-Highest \n6.N-Smallest \n7. Total Rows")
    choice = int(input("Enter Choice :"))
    handle(choice)