"""program to PUNISH naughty people who are TOO ADDICTED to technology
"""
import easy_gui

used_tech = easy_gui.msgbox("Enter the days on which you used tech\nseparate each day with a space",
                            "Days tech was used")
days = len(used_tech.split())
if days <= 3:
    easy_gui.msgbox(f"Congratulations. You used tech {days} tech free days with "
                    f"{7-days} tech-free days.", "Goal achieved!!!!!!!!!!!!!")
else:
    easy_gui.msgbox(f"You SUCK!!!! I can't believe how trash you are to have used tech {7 - days} \n"
                    f"That is like {days - 4} less than your goal,", "Goal FAILED")
    o
