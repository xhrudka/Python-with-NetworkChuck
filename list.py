# List usage

camping_list = ["test", "sleeping_bags", "water", "rasberry pi", "coffee", "knife", "ethernet cable", "flash drive", "beard oil", "marshmallows"]
print(camping_list)

# Append can add just one item 
camping_list.append("Jeff")
print(camping_list)  

# Insert can add just an item, but on the certain position 
camping_list.insert(0,"Joe")
print(camping_list)  

# Extend can add just one item 
camping_list.extend(["Chuck", "Mike"])
print(camping_list)  
 
# It is also possitble to do it with extension
camping_list = camping_list + ["Hallo"]
print(camping_list)  

# Removing the items from the list
camping_list.remove("knife")
print(camping_list)  

# Removing the items from the list by method pop, works indexing not values
camping_list.pop(3)
print(camping_list) 

# Clear the whole list
camping_list.clear()
print(camping_list) 

camp_site = ["Crystal lake", 404, 89.3, True] 

# Show value of the list on the position 1 
me = camping_list[1]
print(me)
# Show value of the list on the position -1 
you = camping_list[-1]
print(you)

