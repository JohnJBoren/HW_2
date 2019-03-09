from months import create_month, month
from years import create_year, years
import os

#Counter for the number of year folders created
counter = 0
#Counter for the number of month subfolders created
subcounter = 0

#This line clears the screen
os.system("cls")

for year in years:
    file_created = create_year(year)
    if(file_created):
        counter += 1
    for moons in month:
        #I add the year folder to the path name
        moons = "\\%s\\%s" % (year, moons)
        file_created = create_month(moons)
        if (file_created):
            subcounter += 1
print "%s\tyear folders were created." % counter
print "%s\tmonth subfolders were created." % subcounter




