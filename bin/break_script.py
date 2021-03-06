from pathlib import Path 
from random import shuffle

## Method that takes in moves and spits out combinations of three

def getMoves(moves):
	# Neater code, list comprehension instead of several lines with the code asking for
	# 'input' each time
	
	combinations = []

	# Formulate all the different combinations...run time is exponential so will need to
	# find a different way next time
	for step in moves:
		for next_step in moves:
			for final_step in moves:
				if (step != next_step and step != final_step and next_step != final_step):
					combo = [step, next_step, final_step]
					if (combo not in combinations):
						combinations.append(combo)
	shuffle(combinations)
	return combinations

## Write the combinations to a file
def toFile(combinations, name_of_file):
	# Get the name of the file from the user
	userFileName = name_of_file + ".txt"
	# Making the right path to put where the damn text file should be -_-
	data_folder = Path('output')
	path = data_folder / userFileName
	filename = path.resolve()
	# Open and create the text file
	file = open(filename,"w+")
	file.write("Number of combinations are: " + str(len(combinations)) + '\n\n')
	for element in combinations:
		index = combinations.index(element)
		line = ' '.join(str(e) for e in element)
		file.write(str(index + 1) + ") " + line + '\n')
	file.close
