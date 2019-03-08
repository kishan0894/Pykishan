"""* Check the pattern:
    1
    1 1
    2 1
    1 2 1 1
    1 1 1 2 2 1
    * Its number of occurrence of each digit in one level above:
        * no. of occurrence (contiguous) of i in level above <space> i
* Calculate for level 30
"""

r = [[1]]

for i in range(1, 31):
    temp = []
    prev = None
    count = 0
    iter_count = 0
    for elem in r[i-1]:
        if elem == prev or prev is None:
            count += 1
            prev = elem
        elif elem != prev:
            temp.append(count)
            temp.append(prev)
            count = 1
            prev = elem
    if elem == prev:
        temp.append(count)
        temp.append(prev)
    r.append(temp)

print(len(r[30]))