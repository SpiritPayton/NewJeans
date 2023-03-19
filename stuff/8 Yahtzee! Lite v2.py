"""program to do a yahtzee! game thingy"""
import random
import easy_gui


def roll_dice():
    return [random.randint(1, 6) for _ in range(5)]


def get_counts(dice):
    counts = [0] * 7
    for d in dice:
        counts[d] += 1
    return counts


def get_score(dice):
    counts = get_counts(dice)
    if 5 in counts:
        return 50
    elif 4 in counts:
        return 30
    elif 3 in counts:
        return 10
    else:
        return 0


def play_game():
    player_scores = {"player 1": 0, "player 2": 0}
    player_names = []
    for i in range(2):
        player_name = easy_gui.enterbox(f"GIMME the name of player {i+1}!!!!!!!!!!!!!!!!!!")
        player_names.append(player_name)

    for i in range(3):
        for player_name in player_names:
            dice = roll_dice()
            roll_num = i + 1
            message = f"{player_name} Roll {roll_num}: {dice}\ni will let you roll again" \
                      f" even though you should just leave..."
            if not easy_gui.boolbox(message, "Yahtzee!", ["roll again", "stick"]):
                score = get_score(dice)
                dice.sort()
                easy_gui.msgbox(f"{player_name} score: {score}\ndice: {dice}")
                player_scores[player_name] = score
                break

    max_score = max(player_scores.values())
    winners = [k for k, v in player_scores.items() if v == max_score]
    if len(winners) == 1:
        winner_msg = f"{winners[0]} wins with a score of {max_score}!"
    else:
        winner_msg = f"wooooooo hoooooooo it's a tie between {', '.join(winners)} with a" \
                     f" score of {max_score}!! you both suck"

    play_again = easy_gui.boolbox(f"{winner_msg}\nwanna play again? (please don't ;-;)", "Yahtzee!", ["yeah", "nah"])
    if play_again:
        play_game()


play_game()
