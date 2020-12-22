data = data2 = ""

with open('CSC_217_attendance_ week1_30.txt') as fp:
    data = fp.read()

with open('CSC_217_attendance_ week1_end.txt') as fp:
    data2 = fp.read()

# Merging 2 files
# To add the data of file2
# from next line
data += "\n"
data += data2

with open('merged file', 'w') as fp:
    fp.write(data)

content = open('merged file','r').readlines()

content_set = set(content)

cleandata = open('CSC_217_attendance_ week1_.txt','w')

for line in content_set:
    cleandata.write(line)
