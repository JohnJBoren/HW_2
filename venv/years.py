import os

path = os.getcwd()
path += "\\"

BEGIN_YEAR = 2005
END_YEAR = 2011

def create_year(yr):

    if(os.path.exists(path + str(yr))):
        print "%s already exists." % yr
        return False
    else:
        os.makedirs(path + str(yr))
        print "%s folder has been successfully created" % yr
        return True
years = range(BEGIN_YEAR, END_YEAR)

#Uncomment to use this file individually
#for year in years:
#   create_year(year)