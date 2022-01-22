import csv

radiusMultiplier = 0.102763
massMultiplier = 0.000954588
data = []

with open("dwarf_stars.csv") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        data.append(row)
dwarf_headers = data[0]
dwarf_data = data[1:]
print("Working")
counter=0

for data_point in dwarf_data:
    if(len(data_point) > 0):
        if(len(data_point[3]) > 0):
            newRadius = float(data_point[3])*radiusMultiplier
            data_point[3] = newRadius
        if(len(data_point[2]) > 0):
            newMass = float(data_point[2])*massMultiplier
            data_point[2] = newMass
    else:
         dwarf_data.pop(counter)
    counter=counter+1

with open("MergeData.csv", "a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(dwarf_headers)
    csvwriter.writerows(dwarf_data)

data = []
with open("DataPrepping.csv") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        data.append(row)
star_data = data[1:]

counter = 0
merge_data = []
for data_point in star_data:
    if(len(data_point)>0):
        name = data_point[0]
        distance = data_point[1]
        mass = data_point[2]
        radius = data_point[7]
        merge_data.append([name,distance,mass,radius])
        counter = counter+1

with open("MergeData.csv", "a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerows(merge_data)