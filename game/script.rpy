# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

image bg stable = "images/horses_in_stable.jpg"
# Declare characters used by this game.

define narrator = Character(None)

init:
  python:
    def countdown(st, at, length=0.0):
      remaining = length - st
      return Text("%.0f" % remaining, color="#fff", size=72), .1

# The game starts here.
label start:
  image countdown = DynamicDisplayable(countdown, length=10)

  scene bg stable

  "HORSE QUEST: THE QUEST OF A LIFETIME"
  "IN WHICH YOU, A BRAVE HORSE HERO, MUST WIN THE AFFECTION OF THE LADYHORSE OF YOUR DREAMS"
  "WHILE NAVIGATING THIS CRUEL HORSE WORLD IN WHICH YOU LIVE"
  $ ui.timer(10.0, ui.jumps("menu1_slow"))
  show countdown at Position (xalign = 0.5, yalign = 0.1)
  menu:
    "Choice 1":
      hide countdown
      "You chose 'Choice 1'"
  return

label menu1_slow:
  hide countdown
  "YOU CHOSE WRONG"
