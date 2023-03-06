"""program to PUNISH those who are absent"""

peoples = {

}


def input_joonda():
    name = None
    while True:
        name = str(input("NAME?"))
        if name == "":
            print("WTF ARE YOU ACTUALLY STUPID DOES "
                  "THIS PERSON NOT HAVE A NAME?")
        else:
            break
    while True:
        absenses = input("ABSENSES?!?!?!")
        try:
            peoples[name] = int(absenses)
            return
        except:
            print("ENTER A NUMBER OR I WILL STAB YOU")


def initial_loop():
    while True:
        should_continue = input("INPUT '$' TO NOT INPUT DATA OR PRESS "
                                "LITERALLY ANYTHING ELSE TO INPUT DATA::: ")
        if should_continue == "$":
            print("GO AWAY\n\n")
            avg = 0
            most_absenses = None
            zero_absenses = []
            for name in peoples:
                absenses = peoples[name]
                if most_absenses == None or absenses > peoples[most_absenses]:
                    most_absenses = name
                avg += absenses
                if absenses == 0:
                    zero_absenses.append(name)
            zero_absenses = "\n".join(sorted(zero_absenses))
            avg /= len(peoples.keys())
            above_average = []
            for name in peoples:
                absenses = peoples[name]
                if absenses > avg:
                    above_average.append(name)
            above_average = "\n".join(above_average)
            print(f"'*•.¸♡ Average absenSeS per year "
                  f"(A.S.S for short) ♡¸.•*'\n{avg}")
            print(f"\n'*•.¸♡ Laziest of the year award "
                  f"(R.O.F.L for short) ♡¸.•*'\n{most_absenses} ({peoples[most_absenses]} absenses)")
            print(f"\n≡;- ꒰ ° Tryhards with no kabsenses! "
                  f"(T.W.I.N.K for short) ꒱\n{zero_absenses}")
            print(f"\n⇢ ˗ˏˋ Staycies who were above the average absenses "
                  f"(L.O.O.N.A for short) ࿐ྂ\n{above_average}")
            print("\n( :̲̅:̲̅:[̲̅: Thank you for your time! Came again! :]̲̅:̲̅:̲̅:̲̅)")
            return
        else:
            input_joonda()

# Run the thing
initial_loop()
