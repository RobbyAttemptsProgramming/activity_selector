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
	"Play Games", 
	"Webdev",
	"Math",
	"Python", 
	"Clean", 
	"Free Time", 
	"Read"]

def roll(activities):
	index = randint(0, (len(activities) - 1))

	return activities[index]

def beautify(activity):
	length = len(activity)
	top = "*" * (length + 4)
	mid = "* " + activity + " *"
	bottom = "*" * (length + 4)

	print(
		top + "\n" +
		mid + "\n" + 
		bottom + "\n")


# Main program loop
# os.system is set to clear despite being on windows, due to using bash.
# CLS would be used from Windows command line
cont = True

while cont:
	os.system('clear')
	beautify(roll(activities))

	inp = input("Type Q to quit\n")

	if inp.upper() == "Q":
		cont = False



# What's left to add/figure out? I need to create a system to 
# reduce the chance of an activity being selected more than once.
# Specifically this would be an issue if "play games" appeared 
# five times in a row. This would be an inefficient use of time and
# completely contradicts the point of this program.
