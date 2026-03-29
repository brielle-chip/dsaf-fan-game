# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define glorp = Character("Glorp", color="bbe480")
define ballsack = Character("Ballsack", color="1e00dc")

# The game starts here.

label start:

    "hello! this is a test of renpy i wrote!"
    "wow! this is so fast and simple!"
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    play music "audio/tadc theme.mp3" fadein 1.0 loop
    scene saferoom_bg
    with fade
    show Glorp default
    with fade
    # These display lines of dialogue.

    glorp "OMG HUMAN HELLO HUMAN."

    glorp "It is nice to meet you! I am also a fellow human! My name is Spork."

    glorp "What is your name?"

    show Glorp thinking
    
    glorp "mmmm that name sounds delicious..."

    show Glorp thinking at left
    show Ballsack enter:
        xalign 0.7
        yalign 0.6

    show Glorp shock
    glorp "GAAAAAASP IS THAT MY ONE AND ONLY RIVAL, BALLSACK??!?!"

    ballsack "hey everybody its me ballsack here"

    glorp "THERES ONLY ONE WAY TO SETTLE THIS..."
    glorp "GYATT OFF"

    show Glorp gyatt
    show Ballsack gyatt

    menu:
        "So... Who has the biggest gyatt? Choose wisely."
        "Glorp":
            jump glorp_wins_gyatt_off

        "Ballsack":
            jump ballsack_wins_gyatt_off

    # This ends the game.

    return

    
label glorp_wins_gyatt_off:
    show Glorp thinking
    glorp "YAAAAY I KNEW I HAD THE BIGGEST GYATT"
    ballsack "aw man"
    hide Ballsack with dissolve
    return

label ballsack_wins_gyatt_off:
    show Glorp shock
    glorp "WHAAAAAAAT??!?!! HOW COULD THIS BE"
    ballsack "hell yeah"
    hide Glorp with dissolve
    return