import csv
import datetime

now = datetime.datetime.now()
recordtime = 'rec_{0:%Y%m%d}'.format(now)
print("recordtime = %s" % recordtime)

data = "foo,bar,baz"
data = recordtime + "," + data
data = data.split(',')
print("data= %s" % data)

with open('log.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(data)
f.close()
print("loggging done. see log.csv")
