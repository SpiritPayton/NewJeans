"""Version 2 of the spelling checker program
program to change words from the Aotearoa spelling to
the United States of America spelling
"""

import easy_gui

while True:
    # check the word and convert to list
    aotearoa_word = easy_gui.enterbox("enter thee aotearoan word",
                                      "word to check")
    america_word = aotearoa_word

    # check for aotearoan words and ELIMINATE the letters
    # our
    if "our" in aotearoa_word:
        america_word = aotearoa_word.replace("our", "or")

    # ise
    elif "ise" in aotearoa_word:
        america_word = aotearoa_word.replace("ise", "ize")

    # yse
    elif "yse" in aotearoa_word:
        america_word = aotearoa_word.replace("yse", "yze")

    # show results and ask if the user want to check another word
    new_word = easy_gui.buttonbox(f"america spell '{aotearoa_word}' is "
                                  f"'{america_word}'\n\nany more words"
                                  f" to americanise???", "check another",
                                  choices=["Yes", "No"])
    # kill program if mr baker has had enough testing
    if new_word == "No":
        break

    easy_gui.msgbox("ka kite ano whanau", "baby we ain't got tyme!")
