import csv
import datetime
filename = "C:\python\sample3.csv"
# Write
with open(filename, "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f, delimiter=",")
    test = datetime.datetime.now()
    writer.writerow(["日付",test])
    writer.writerow(["日付",test.strftime('%Y/%m/%d'),test.strftime('%H:%M:%S')])