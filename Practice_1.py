import re
str = 'Volume Name  Host           Share               Accessible  Mounted  Read-Only   isPE  Hardware Acceleration\n\
-----------  -------------  ------------------  ----------  -------  ---------  -----  --------------------\n\
nfsds1       151.10.10.101  /mnt/vol1/nfs1/ds1        true     true      false  false  Not Supported\n\
nfsds2       151.10.10.102  /mnt/vol1/nfs1/ds2        true     true      false  false  Not Supported'
lines = str.splitlines()    #Splitting Lines
columns = re.sub(' +', ' ', lines[0]).split() # removing all the spaces from first row creating a list named columns
dict_of_list={} # created empty dictionary with elements of first row as keys
for column in columns:
    dict_of_list[column]=[]
for line in range (2,len(lines)): #appending respective row's data to keys in dictionary
    element =0
    row = re.sub(' +', ' ', lines[line])
    row = row.split()
    for element in range (0, len(row)):
        dict_of_list[columns[element]].append(row[element])
        element+=1
keys = dict_of_list.keys()
for key in keys:
    globals()['{}'.format(key)] = dict_of_list[key] #creating lists in run time and adding key value to it from dict_of_lists


print("Enter Filed name")

xx= input()
if(xx in keys ):

    print()
else:
    print("Wrong Filed name")
#you can dynamically use any column name as per your requirement