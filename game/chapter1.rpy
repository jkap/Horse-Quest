label park_dream1:
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

  jump apartment1


label apartment1:
  "So... it was just a dream."

  scene bg apartment shitty
  with dissolve

  "Fuucccckkkk.... I need a pick me up."

  show horse at truecenter
  with dissolve

  "Shit, almost out of pills. I need to get some more. Need to call Hyperion."

  hide horse
  with dissolve

  "WHERE THE FUCK IS MY PHONE"

  scene bg apartment living room
  with dissolve

  neighthan "Hey Tony, have you seen my phone?"
  tony "Nah, man. You need to borrow mine?"
  neighthan "Yeah, thanks."

  scene bg apartment shitty
  with dissolve

  "C'mon, pick up."
  hyperion "Speak"
  neighthan "Hyperion, it's Neighthan"
  hyperion "Hey, my man. What can Hyperion do for you?"
  neighthan "I need some more pills."
  hyperion "Hyperion's running a little short right now, but Hyperion will see what he can do. When do you need them?"
  
  menu:
    "Today":
        jump hypToday
    "Tomorrow":
        jump hypTomorrow

label hypToday:
    neighthan "Today. I need them today. I'm almost out."
    hyperion "That's gonna cost you. Hyperion has to go through a lot of trouble to get more today, ya dig?"
    neighthan "How much extra?"
    hyperion "$6 per"
    
    show horse at truecenter
    
    "Shit, only enough for half"
    
    hide horse
    
    neighthan "I've only got enough for half a bottle."
    hyperion "Well, Hyperion can get you half today and the rest later."
    neighthan "I..."
    neighthan "I guess that works."
    hyperion "Aight, meet Hyperion at the park in two hours. Don't be late."
    
    jump hypHangsUp
    
label hypTomorrow:
    neighthan "I can wait until tomorrow, I've got a bit left."
    hyperion "Aight, Hyperion will get you some for tomorrow. Regular price, you got enough?"
    
    show horse at truecenter
    
    "Just barely enough."
    
    hide horse
    
    neighthan "Yeah, get me a full bottle. I'll see you tomorrow."
    hyperion "Noon at the park. Don't be late."
    
    jump hypHangsUp
    
label hypHangsUp:
    "...doesn't even say goodbye. What a dick."
    "Now... where is my phone?"
    
    scene black with fade

