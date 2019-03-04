string = "ass.ysdv hsdif kashgf    vacshvfne cfjctydhf ashfacd cfvcds"
dictionary = {}
length = len(string)

for i in range(0, length):
    keys = dictionary.keys()
    if string[i] not in keys:
        dictionary[string[i]] = 1
    else:
        dictionary[string[i]] += 1
print(dictionary)