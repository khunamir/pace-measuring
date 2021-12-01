import datetime

pace = float(input("Enter pace: "))
distance = int(input("Enter distance: "))

def conv_to_total_seconds(pace, distance):
    pace = pace * 60
    total = pace * distance
    return total

total = conv_to_total_seconds(pace, distance)

def define_quarters(total, distance):
    quarters = []
    quarterly = 0
    for i in range(distance):
        for j in range(3,-1,-1):
            quarterly = quarterly + (total / distance * 1 / 4)
            quarters.append(quarterly)
    return quarters

f = open('pace.txt', 'w')

quarters = define_quarters(total, distance)
full_quarter = 1
quarter_distance = 250

for i in quarters:
    print(str(datetime.timedelta(seconds = i)), quarter_distance, 'm')
    print(str(datetime.timedelta(seconds = i)), quarter_distance, 'm', file=f)
    if full_quarter % 4 == 0:
        print((full_quarter / 4),' km')
        print((full_quarter / 4),' km', file=f)
    full_quarter = full_quarter + 1
    quarter_distance = quarter_distance + 250

print("Printed to file with name pace.txt")

f.close()