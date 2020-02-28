import time
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names/names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names/names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()


duplicates = []
nameTree = BinarySearchTree(names_1[0])
# Needed to isolate the first index!!
print(nameTree)

for name in names_1:
    # insert each name into
    nameTree.insert(name)
for name in names_2:
    # compare compare names_2 to BST to see if there ar duplicate
    # if returns true append to duplicate
    if nameTree.contains(name):
        duplicates.append(name)


# for name_1 in names_1:                #0(n)
#     for name_2 in names_2:            #0(n)
#         if name_1 == name_2:          #
#             duplicates.append(name_1)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")


# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
