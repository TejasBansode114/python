import csv

# Write CSV file
with open("data.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["Alice", 28, "Los Angeles"])
    writer.writerow(["Bob", 34, "Chicago"])

# Read CSV file
with open("data.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)