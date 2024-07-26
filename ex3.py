import statistics as st

def getData():
    print("Enter Values For Dataset :")
    data = [ int(input()) for i in range(5)]
    return data

while True:
    print("Exercise 3 : Statistical Functions ")
    print("Choice are : \n1.Mean \n2.Median \n3.Mode \n4.Variance \n0.Exit")
    choice = int(input("Enter Choice :"))
    if choice == 1:
        data = getData()
        print(f"Mean Value for {data} is {st.mean(data)}")
    elif choice == 2:
        data = getData()
        print(f"Median Value for {data} is {st.median(data)}")
    
    elif choice == 3:
        data = getData()
        print(f"Mode Value for {data} is {st.mode(data)}")
    elif choice == 4:
        data = getData()
        print(f"SD Value for {data} is {st.stdev(data)}")
    elif choice == 5:
        data = getData()
        print(f"Variance Value for {data} is {st.variance(data)}")
    else:
        print("Exitted at 0 .")
        exit()
    