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

image bg apartment living room = Animation("images/animation/living room00.jpg", 0.1,
                                        "images/animation/living room01.jpg", 0.1,
                                        "images/animation/living room02.jpg", 0.1,
                                        "images/animation/living room03.jpg", 0.1,
                                        "images/animation/living room04.jpg", 0.1,
                                        "images/animation/living room05.jpg", 0.1,
                                        "images/animation/living room06.jpg", 0.1,
                                        "images/animation/living room07.jpg", 0.1,
                                        "images/animation/living room08.jpg", 0.1,
                                        "images/animation/living room09.jpg", 0.1,
                                        "images/animation/living room10.jpg", 0.1,
                                        "images/animation/living room11.jpg", 0.1)

# Declare characters used by this game.

define narrator = Character(None)
define neighthan = Character('Neighthan')
define lh = Character('???')
define tony = Character('Tony')
define hyperion = Character('Hyperion')

init:
  python:
    def countdown(st, at, length=0.0):
      remaining = length - st
      return Text("%.0f" % remaining, color="#fff", size=72), .1

# The game starts here.
label start:
    jump park_dream1

