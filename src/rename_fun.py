
import os
def rename(location,name,count):
    l =location
    n = name
    c = count
    # print("c",c)
    # print("Location of the folder : {} \n New name : {} \n Starting number : {}".format(l,n,c))

    for root, directories, files in os.walk(l, topdown=False):
        for name in files:
            # print("old file names")
            path = os.path.join(root, name)
            file_type = path.split(".")[1]
            # print("file name",name)
            print("Old file name : ",path)
            newname = '{}{}.{}'.format(n,c,file_type)
            # os.rename(filename, '{}_{}.{}'.format(n,c,file_type))
            os.rename(os.path.join(root, name), os.path.join(root, newname))
            print("New file name : ",root,newname)
            c  += 1
