#open file with reading mode
file = open("sample", "r")
count = 0

#print line by line using for loop
for line in file:
    count += 1
    print("Line{}: {}".format(count, line.strip()))
file.close()

#use try_catch _exception block for handling file
try:
    file_name = "sample1"
    file = open(file_name,"r")
    count = 0
    for line in file:
        count += 1
        print("Line{}: {}".format(count, line.strip()))
    file.close()
except Exception as e:
    print("File {} was not found".format(file_name))