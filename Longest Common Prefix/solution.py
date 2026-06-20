strs = ["flower", "flow", "flight"]
letters = []
amount = len(strs) 

for l in strs:
    letters.append(l[0])

all_initial_same = len(set(letters[-amount:])) == 1


for l in strs:
    letters.append(l[1])


all_new_same = len(set(letters[-amount:])) == 1

for l in strs:
    letters.append(l[2])


all_new_same = len(set(letters[-amount:])) == 1
print(all_new_same)


