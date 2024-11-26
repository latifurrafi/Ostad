# def firstevennumber(Numbers):
#     flag = 0
#     for number in Numbers:
#         if number % 2 != 0:
#             flag+=1        
#     return flag

# print(firstevennumber([1,2,34,56,7,4,3])) 

# lamda function
# result  = lambda: 2+3
# print(result())

# result = lambda x, y : x + y
# print(result(10,20))

# result = lambda x, y: x if x>y else y
# print(result(10,20))

# text = "Hello I Global"
# def myFun():
#     text = "Hello I Local"
#     print(text)
# myFun()
# print(text)

# x = 10
# def sum1():
#     global x
#     x = 20
#     result = x + 1
#     print(result)
# sum1()
# def sum2():
#     result = x + 2
#     print(result)
# sum2()

# with open("New_Directory/Example.text","w") as file:
#     file.write("Hello World")

# import os
# os.rename("Example.text","New_Example.text")

# import os
# os.remove("New_Example.text")

# import os
# os.mkdir("New_Directory")

# import os
# os.rmdir("New_Directory")

# import os
# os.rename("New_Directory","new_directory")

# import os
# file_list = os.listdir("Codeforces")
# for file in file_list:
#     print(file)

# import zipfile
# with zipfile.ZipFile("new.zip","w") as zip:
#     zip.write("forZip.text")
#     zip.write("forzipp.text")

# import zipfile
# with zipfile.ZipFile("new.zip","r") as zip:
#     zip.extractall()
#     extracted_file = zip.namelist()
#     print(extracted_file)

# import shutil
# shutil.make_archive("new", "zip", "zip")

# import csv
# data = [
#     ["Name", "Age", "Gender", "City", "Email"],
#     ["John Smith", 28, "Male", "New York", "john.smith@example.com"],
#     ["Emily Johnson", 35, "Female", "Los Angeles", "emily.johnson@example.com"],
#     ["Michael Brown", 40, "Male", "Chicago", "michael.brown@example.com"],
#     ["Sophia Martinez", 22, "Female", "Miami", "sophia.martinez@example.com"],
#     ["David Wilson", 50, "Male", "Houston", "david.wilson@example.com"],
# ]
# with open("new.csv", "w") as file:
#     csv_file = csv.writer(file)
#     csv_file.writerows(data)
#     print("File Created Successfully")


# data = []
# import csv
# with open("new.csv","r") as file:
#     content = csv.reader(file)
#     for row in content:
#         data.append(row)

# print(data)

# try:
#     result = 10/0
#     print(result)

# except ZeroDivisionError:
#     print("ZeroDivisionError")

# finally:
#     print("NoProblem")

