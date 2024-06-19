import csv

def read_csv(file_path):
    with open(file_path, mode='r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            print(', '.join(row))


file_path = input("Enter the path to your CSV file: ")
read_csv(file_path)