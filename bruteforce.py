import string
from time import time
import itertools
from tqdm import tqdm
import pandas as pd

dataset = pd.read_csv("dataset/common_passwords.csv")

def general_attack(target):
    total = dataset.count()
    total_combination = int(total.password)
    print("General Scanning Started ....")
    for row in tqdm(dataset.iterrows(),total=total_combination,desc=f"Scanning ...."):
        guess = row[1]['password']
        if target == guess:
            print(f"Password : {target} is Cracked !")
            return True
    return False

def check_password(password, target):
    if password == target:
        print(f"Password: {password} is Cracked!")
        return True
    return False

def crack(target):
    found = general_attack(target)
    if not found:
        print("Brute Force is starting......")
        chars = string.ascii_lowercase + string.digits
        start_time = time()
        total_combinations = len(chars) ** len(target)
        for combine in tqdm(itertools.product(chars, repeat=len(target)),total=total_combinations, desc=f"Trying length {len(target)}"):
            password_attempt = ''.join(combine)
            if check_password(password_attempt, target):
                end_time = time()
                print(f"Time taken: {end_time - start_time:.2f} seconds")
                return

        print("Failed to crack the password.")
    

password = input("Enter Your Valid Password :")
if password:
    crack(password)
