import os

## Change the directory to where the files are located 
os.chdir("/Users/nahian/Desktop/Programming")

## Method that takes in moves and spits out combinations of three
footwork = ["6step","12step","3step","7step","kickout","CCs","kneeover","pretzel"]
combinations = []
for step in footwork:
    for next_step in footwork:
        if (step != next_step):
            combo = (step, next_step, step)
            if (combo not in combinations):
                combinations.append((step,next_step,step))

## Write iterations to a text file
file = open("breaking_notes.txt","w+")
for element in combinations:
	line = ' '.join(str(e) for e in element)
	file.write(line + '\n')
file.close
        