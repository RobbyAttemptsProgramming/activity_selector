# Activity selector that uses a weighted system to constantly reduce
# an activity from getting selected the more that it's selected in
# a row. Designed to help you do more things during the day than play
# video games, waste time, etc.

# Used strictly for randint()
from random import randint

# Used to clear the terminal
import os

# list of activities to choose from
activities = [ 
	"Webdev",
	"Math",
	"Python", 
	"Clean", 
	"Free Time", 
	"Read"]

"""
Uses random.randint to generate a number between 0 and the
length of the activity list minus one. This number is used
as the indext to the activity list to essentially pick an 
element at random.

Arguments: Activity list

Returns: string activity
"""
def roll(activities):
	index = randint(0, (len(activities) - 1))
	return activities[index]

"""
Formats the output of a string to include asteriks surrounding the
string.

Arguments: string activity

Returns: Nothing, prints to terminal
"""
def beautify(activity):
	length = len(activity)
	top = "*" * (length + 4)
	mid = "* " + activity + " *"
	bottom = "*" * (length + 4)

	print(
		top + "\n" +
		mid + "\n" + 
		bottom + "\n")

"""
Cycles through the history list and adds 10 to weight
for each string that is the same as the activity argument.
This generates a "percentage" to be used later.

Arguments: history list
		   string activity

Returns: int for percentage
"""
def get_weight(history, activity):
	weight = 0

	for act in history:
		if act == activity:
			weight += 10

	return weight

"""
Rolls a number between 1 and 100 and checks if that number is
less than 100 minus the argument weight. Acts as a chance to determine
whether the activity is to be rerolled or passed.

Argument: int weight

Returns: bool answer
"""
def weighted_roll(weight):
	max_chance = 100

	roll = randint(1, 100)

	if roll <= max_chance - weight:
		return True
	else:
		return False

# Main program loop
# os.system is set to clear despite being on windows, due to using bash.
# CLS would be used from Windows command line
cont = True
last_activity = ""
history = []
activity = ""

while cont:
	# Adds activity to history list
	history.append(last_activity)
	# stores current activity to display on next roll
	last_activity = activity

	activity = roll(activities)
	os.system('clear')
	beautify(activity)

	# Prints last selection after activity if there was one
	if last_activity: 
		print("Last activity: " + last_activity + "\n\n\n")

	# Quit loop option
	inp = input(
		"Press Enter to roll again\n"
		"Type Q to quit\n")

	if inp.upper() == "Q":
		cont = False
	



# What's left to add/figure out? I need to create a system to 
# reduce the chance of an activity being selected more than once.
# Specifically this would be an issue if "play games" appeared 
# five times in a row. This would be an inefficient use of time and
# completely contradicts the point of this program.
