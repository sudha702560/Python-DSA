# OS 

import os
# Create , Read , Write / Append , Delete  

# Rename , Move , Copy 


# 

# file = open("hello.py","r")
# print(file)
# print(file.read())


# with open("hello.py","a") as f :
#     f.write("#This is a newly added line -- Using the Append Mode")


with open("hello.py","w") as f :
    f.write("#Previous Data will be removed -- Using the Write Mode")

with open("hello.py","r") as f:
    print(f.read())
# file.close()


# x -- 

# os.remove("hello.py")

# os.rmdir
# os.removedirs