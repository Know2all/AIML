import pandas as pd
import numpy as np

while True:
      print("\n1. HANDLING MISSING VALUES IN THE OWN DATA FRAME \n2. HANDLING MISSING VALUES IN THE CSV FILE\n3. EXIT")
      print("------------------------------------------------------")
      choice = int(input("Enter your choice : "))
      print("------------------------------------------------------")
      
      if choice == 1:
            r, c = map(int, input("Enter row and column of dataset: ").split())
            print("------------------------------------------------------")

            cols = [input(f"Enter Column{i+1} Name :") for i in range(0,c)]

            print("Entering values ...")
            dataset = np.empty((r,c))
            for i in range(0,r):
                  for j in range(0,c):
                        val = input()
                        if val.lower() == 'nan':
                              dataset[i,j] = np.nan
                        else:
                              dataset[i,j] = float(val)
      
            df = pd.DataFrame(dataset,columns=cols)          

            print("------------------------------------------------------")
            column = input("Enter the column to handle missing values : ")
            print("------------------------------------------------------")
            if(True in list(df[column].isnull())):
                  print("It has null values")
                  method = input("Enter are you fill value or drop the null value :")
                  if(method.lower() =="fill"):
                        df[column].fillna(value=df[column].mean(), inplace=True)
                  else:
                        df.dropna(inplace=True)
                  print("After handling missing missing values :\n",df)
            else:
                  print("It has no null values")
            print("------------------------------------------------------")
            
      elif choice == 2:
            data = pd.read_csv('dataset/students.csv')
            print("Columns in the Datasets are : ",data.columns)
            print("------------------------------------------------------")
            print("Data in the dataset : \n",data.head(10))
            print("------------------------------------------------------")
            column = input("Enter the column to handle missing values : ")
            print("------------------------------------------------------")
            if(True in list(data[column].isnull())):
                     print("It has null values")
                     method = input("Enter are you fill value or drop the null value :")
                     if(method.lower() == "fill"):
                           data[column].fillna(value=data[column].mean(), inplace=True)
                     else:
                           data.dropna(inplace=True)
                     print("After handling missing missing values :\n",data[column].head(10))
            else:
                     print("It has no null values")
            print("------------------------------------------------------")
      
      else:
            print("System is exiting.....")
            print("------------------------------------------------------")
            exit()