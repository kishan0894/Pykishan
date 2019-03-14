import os;import re;import commands
_, string =commands.getstatusoutput("docker images")
string = re.sub(r'([^ ]) ([^ ])',r'\1_\2', string)
lines = string.splitlines()    #Splitting Lines
string.replace(' ','_', 0)
new_command='docker rmi'
for line in range (1,len(lines)): #appending respective row's data to keys in dictionary
    row = re.sub(' +', ' ', lines[line]).split()
    new_command+= ' ' + row[2]
new_command+= ' -f'
print(new_command)