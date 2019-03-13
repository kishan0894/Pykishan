import os
import re
import commands
_, string =commands.getstatusoutput("docker images")
string = re.sub(r'([^ ]) ([^ ])',r'\1_\2', string)
lines = string.splitlines()    #Splitting Lines
string.replace(' ','_', 0)
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
new_command='docker rmi '

Image_id=dict_of_list['IMAGE_ID']
for id in Image_id:
    new_command += ' '
    new_command += str(id)

new_command += ' -f'

os.system(new_command)
