from appJar import gui
import break_script as bboy

def initialize():

	# Sets the size of the gui
	app = gui("Combo Formula", "600x400")

	# Title on the gui 
	app.addLabel("title", "Dance Combo Maker")
	app.setLabelBg("title", "red")

	# Interface formatting
	app.setBg("orange")
	app.setFont(18)

	# Adding input widgets for Move 1, 2, and 3
	entries = []
	for i in range(3):
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
			inputs = [[len(app.getEntry("m1")), "m1"],
			[len(app.getEntry("m2")), "m2"],
			[len(app.getEntry("m3")), "m3"]
			]

			# If all three are valid, we run the code
			validations = 0
			for e in inputs:
				if (e[0] <= 0):
					app.setEntryInvalid(e[1])
				else:
					app.setEntryValid(e[1])
					validations += 1

			if (validations == 3):
				# Create message widget
				routines = bboy.getMoves(app.getAllEntries().values())

				## Output to another window
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





