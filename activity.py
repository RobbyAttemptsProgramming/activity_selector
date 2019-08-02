# Activity selector that uses a weighted system to constantly reduce
# an activity from getting selected the more that it's selected in
# a row. Designed to help you do more things during the day than play
# video games, waste time, etc.

# Used strictly for randint()
from random import randint

# Used to clear the terminal
import os


##Functions##

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

"""
Creates a schedule with argument number of hours, and activities.
Returns a list for a schedule to be printed.

Arguments: int for hours, and a list of activities

Returns: a list containing activities
"""
def make_schedule(hours, activities):
	schedule = []
	l = activities

	for activities in range(0, hours):
		activity = roll(l)
		schedule.append(activity)

	return schedule

"""
Gets input from the user for number of hours to roll
for in make_schedule()

Arguments: None

Returns: int for number of hours
"""
def get_hours():
	os.system('clear')
	hours = input("Hours to roll for: ")

	return int(hours)


##Main Loop##

# Main program loop
# os.system is set to clear despite being on windows, due to using bash.
# CLS would be used from Windows command line

# list of activities to choose from
activities = [ 
	"Webdev",
	"A+ Cert",
	"Math",
	"Python", 
	"Free Time"]
activity = ""
schedule = []

while True:
	# Quit loop option
	inp = input(
		"\n\n\nPress Enter to roll a single activity\n" +
		"Type M to make list\n" +
		"Type Q to quit\n")

	if inp.upper() == "Q":
		break;
	elif inp.upper() == "M":
		schedule = make_schedule(get_hours(), activities)
		os.system('clear')
		for activ in schedule:
			print("- " + activ)
		print('\n')
	else:
		activity = roll(activities)
		os.system('clear')
		beautify(activity)
