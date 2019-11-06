initiallist = ["The Room", "Troll2", "Samurai Cop", "Battlefield Earth"]
print("Here is my list of bad movies: \n{}".format(initiallist))

secondlist = ["Tommy Wiseau", "Darren Ewing", "Matt Hannon", "John Travolta"]
print("Here is my list of bad actors: \n{}".format(secondlist))

a = True
while a:
  entry = input("Enter a bad movie to append (start with + to add or - to subtract). To add by index add a comma and then the index: ")
  if entry == "quit":
    break
  entry2 = input("Enter a bad actor to append (start with + to add or - to subtract). To add by index add a comma between name and index: ")
  if entry2 == "quit":
    break
  print("Here is the entered value: " + entry)
  if entry.startswith("+"):
    initiallist.append(entry[1:])
    print(initiallist)
    continue
  if entry.startswith("-"):
    initiallist.remove(entry[1:])
    print(initiallist)
    continue
  if entry.startswith("*"):
    initiallist.reverse()
  
