import easy_gui

nz_word = easy_gui.enterbox("Please enter the NZ word", "Word to check")
letters = list(nz_word)
letters.remove("u")
letters.remove("u")
letters.remove("u")

easy_gui.msgbox(f"The American spelling of {nz_word} is {''.join(letters)}",
                "Result")
