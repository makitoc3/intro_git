import csv
filename = "C:\python\csv_sample.csv"
# Write
with open(filename, "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f, delimiter=",")
    writer.writerow([1, 2, 3])
