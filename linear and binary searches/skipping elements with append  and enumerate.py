def skip_elements(elements):

	result=[] # creates the empty place to store new list
	for index, e in enumerate (elements):
		if index % 2 == 0: #if index remainder 2 equal to 0
			result.append(e) #add e
	return result # returns a list skipping the second element 
	
	

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry