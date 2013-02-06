# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

image bg park = "images/park.jpg"
image bg apartment shitty = "images/shitty apartment.jpg"
image horse = "images/horse.png"
image horse warp1 = "images/horse warp1.png"
image horse warp1 sad = "images/horse warp1 sad.png"
image horse warp2 = "images/horse warp2.png"
image horse warp3 = "images/horse warp3.png"
image horse warp4 = "images/horse warp4.png"

# Declare characters used by this game.

define narrator = Character(None)
define neighthan = Character('Neighthan')
define lh = Character('???')

init:
  python:
    def countdown(st, at, length=0.0):
      remaining = length - st
      return Text("%.0f" % remaining, color="#fff", size=72), .1

# The game starts here.
label start:
  scene bg park

  "Boy, this sure is a beautiful day"
  "If only I had someone to share it with..."
  lh "Hello, Neighthan."

  show horse

  neighthan "Well, hello. It's great to see you."
  lh "It's been a while, hasn't it Neighthan?"
  neighthan "Yes... almost too long."

  show horse warp1
  with dissolve

  lh "Well, it's been hard to think of you since you..."
  show horse warp1 sad
  with dissolve
  lh "...broke my heart."
  neighthan "What! I've never broken anyone's heart!"

  show horse warp2
  with dissolve

  lh "Don't be ridiculous, Neighthan. You know what you did to me. You know you broke my heart."
  neighthan "What... what is wrong with your face?"

  show horse warp3
  with dissolve

  lh "Neighthan! You jerk, nothing is wrong with my face!"
  neighthan "No... your skin!"
  lh "My skin is flawless!"

  show horse warp4
  with dissolve

  neighthan "AAAHHHHH"

  hide horse warp4
  scene black
  with Pause(2)

  "So... it was just a dream."

  scene bg apartment shitty
  with dissolve

  "ugh"
