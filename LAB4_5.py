mounths = ['','January','February','March','April','May','June','July','August','September','October','November','December']
date = input("Input Date : ")
day,mounth,year = date.split('-')
mounth = int(mounth)
print(day+'-'+mounths[mounth]+'-'+year)

