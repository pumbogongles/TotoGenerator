import random

nums = []; #Declare nums list

numSize = 6; #Declare List size numSize

# Start x For loop
for x in range(numSize): #Loop x the amount of numSize
 newNumberIsSame = True; # Set newNumberIsSame as true by default 
 # Start newNumberIsSame While loop
 while newNumberIsSame: # If newNumberIsSame is true, continue looping
  randomNumber = random.randint(1,42); #random Number
  numberIsNotRepeated = True; # Set numberIsNotRepeated as true by default
  # Start oldNumber For loop
  for oldNumber in nums: # Check if number exists in nums
   if randomNumber == oldNumber: # If new number is same as any number found in nums, set numberIsNotRepeated to false
    numberIsNotRepeated = False;
  # End oldNumber For loop
  print("randomNumber: ",randomNumber); # check number repeat to proof it replaces - can be deleted after proofing
  print("numberIsNotRepeated: ",numberIsNotRepeated); # check numberIsNotRepeated to proof it replaces - can be deleted after proofing
  if numberIsNotRepeated: # If new number is not found in nums, add to list and newNumberIsSame to false to end While loop
   nums.append(randomNumber)
   newNumberIsSame = False;
 # End newNumberIsSame While loop
# End x For loop 
nums.sort(); # Sort nums in ascending order
print("Your RNG numbers are: ",nums); # Print out results