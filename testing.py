# Assignment 2 Files DAY 3

# Create a text file
with open("notes.txt", "w") as file:
    file.write("Hello Shourya")

# Read the file
with open("notes.txt", "r") as file:
    content = file.read()
print(content)

# Read line by line
with open("notes.txt", "r") as file:
    for line in file:
        print(line.strip())

# Append new data
with open("notes.txt", "a") as file:
    file.write("Graduated in 2026\n")
print("Student Added")

# Create a CSV file
import csv

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["ID", "Name", "Marks"])
    writer.writerow([101, "Shourya", 95])

# CSV read
with open("students.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# Append new record
with open("students.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([104, "Kiran", 87])
print("Record Added")

# DictWriter
with open("students.csv", "w", newline="") as file:
    fieldnames = ["ID", "Name", "Marks"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({"ID": 101, "Name": "Reddy", "Marks": 95})
    writer.writerow({"ID": 102, "Name": "Hari", "Marks": 88})
    writer.writerow({"ID": 103, "Name": "Ruhan", "Marks": 91})
print("Data written successfully.")

# DictReader
with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)



import numpy as np
a = np.array([1, 2, 3, 4, 5])
print(a)