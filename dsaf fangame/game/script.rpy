# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define glorp = Character("Glorp", color="bbe480")


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

    # This ends the game.

    return

    
