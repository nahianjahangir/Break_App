from appJar import gui
import break_script as bboy

def initialize():
	# Number of moves used in the script
	num_moves = 9

	# Sets the size of the gui
	app = gui("Combo Formula", "600x400")

	# Title on the gui 
	app.addLabel("title", "Dance Combo Maker")
	app.setLabelBg("title", "red")

	# Interface formatting
	app.setBg("orange")
	app.setFont(18)

	# Add file input widget
	app.addValidationEntry("f1")
	app.setEntryDefault("f1", "Filename")

	# Adding input widgets for Move 1, 2, and 3
	entries = []
	for i in range(num_moves):
		iternum = str(i+1)
		entries.append("m" + iternum)
		app.addValidationEntry("m" + iternum)
		app.setEntryDefault("m" + iternum, "Move " + iternum)

	# Encapsulated function for button presses
	def press(button):
		# Exit out
		if button == "Cancel":
			app.stop()
		# If the button "Mix" is pressed
		else:
			# The three input widgets
			inputs = [[len(app.getEntry(e)), e] for e in entries]
			inputs.append([len(app.getEntry("f1")), "f1"])

			# If all three are valid, we run the code. Check the length of input
			# to have at least one character in the input
			validations = 0
			# Number of moves + filename 
			valid_nums = num_moves + 1

			for e in inputs:
				if (e[0] <= 0):
					app.setEntryInvalid(e[1])
				else:
					app.setEntryValid(e[1])
					validations += 1

			if (validations == valid_nums):
				routines = bboy.getMoves([app.getEntry(m) for m in entries])
#				routines = bboy.getMoves(app.getAllEntries().values())
				bboy.toFile(routines, app.getEntry("f1"))

				# Create message widget
				## Output to another window
				popout = False
				if popout == True:
					message = ""
					for combo in routines:
						for move in combo:
							if (move != combo[-1]):
								message += move + " -> "
							else:
								message += move + "\n"
					app.startSubWindow("Break Output",modal=True)
					app.setFont(size=20, family="Verdana")
					app.addLabel("output", "Combos")
					app.setLabelBg("output", "orange")
					app.setBg("orange")
					app.setSize(400,200)
					app.addMessage("routines", message)
					app.showSubWindow("Break Output")


	# Creating buttons
	app.addButtons(["Mix", "Cancel"],press)

	app.go()

initialize()





