#  Creating an empty list
my_list = []

#  Appending the elements 10, 20, 30, 40
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

#  Inserting 15 at the second position 
my_list.insert(1, 15)

#  Extending the list with [50, 60, 70]
my_list.extend([50, 60, 70])

#  Removing the last element
my_list.pop()  # Removes and returns the last item

#  Sorting the list in ascending order
my_list.sort()

#  Find and print the index of the value 30
index_30 = my_list.index(30)
print("The index of 30 is:", index_30)

# Optional: print the final list to verify each step
print("Final list:", my_list)
