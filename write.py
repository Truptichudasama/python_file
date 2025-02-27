#file open with append mode and write data as per user input.
try:
    with open("output.txt", "a") as f:
        data=input("Enter text to write to the file:")
        f.write(data)
        f.write("\n")
        print("data succssfully written in to output.txt")
        new_data =input("Enter additional text to append to file:")
        f.write(new_data)
except Exception as e:
    print(e)

#file reading for output.
try:
    file_name = "output.txt"
    file = open(file_name,"r")
    count = 0
    print("Final content of output.txt")
    for line in file:
        print(line.strip())
    file.close()
except Exception as e:
    print("File {} was not found".format(file_name))