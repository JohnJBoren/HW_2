import os

path = os.getcwd()
path += "\\"

def create_month(mon):

    if(os.path.exists(path + mon)):
        print "%s already exists." % mon
        return False
    else:
        os.makedirs(path + mon)
        print "%s\t subfolder has been successfully created." % mon
        return True
month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

#Uncomment to use this file individually
# for each in month:
#     create_month(each)
