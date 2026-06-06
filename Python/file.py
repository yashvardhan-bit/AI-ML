# f=open("sample.txt","w")
# f.write("all the data is overwritten")
# f.close()
# with open("sample.txt","r") as f:
#     print(f.read())
# import os
# os.remove("sample2.txt")
data=True
line=1
with open("sample.txt","r") as f:
    while data:
        data=f.readline()
        if "python" in data:
            print("present in line ", line)
            break
        line+=1