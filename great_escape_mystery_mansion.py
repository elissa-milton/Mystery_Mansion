import random

# -------------------- GAME INFORMATION --------------------

player = ""
score = 0
lives = 5
inventory = []
rooms_escaped = 0
hints_used = 0


def line():
    print("\n" + "=" * 58)


def pause():
    input("\nPress ENTER to continue...")


def ask_choice(question, options):
    """Keep asking until the player enters a valid option."""
    while True:
        answer = input(question).strip().lower()
        if answer in options:
            return answer
        print("Please choose " + " or ".join(options) + ".")


def status():
    line()
    print("PLAYER:", player)
    print("SCORE:", score)
    print("LIVES:", "♥ " * lives)
    print("ITEMS:", ", ".join(inventory) if inventory else "None yet")
    line()


def hint(text):
    global hints_used
    choice = ask_choice("Would you like a hint? (yes/no): ", ["yes", "no"])
    if choice == "yes":
        hints_used += 1
        print("\nHINT:", text)
        return True
    return False


def answer_puzzle(question, answers, clue, points=10, attempts=2):
    """A reusable puzzle: the player gets a limited number of tries."""
    global score, lives
    print("\n" + question)
    hint(clue)

    for attempt in range(attempts):
        guess = input("\nYour answer: ").strip().lower()
        if guess in answers:
            print("\nCorrect! You solved it!")
            score += points
            return True
        remaining = attempts - attempt - 1
        if remaining:
            print("Not quite. Have another think!")
        else:
            print("That's not quite right. The answer was:", answers[0])
            print("You lose one life.")
            lives -= 1
    return False


# -------------------- ROOM 1: THE LIBRARY --------------------

def library():
    global score, lives, rooms_escaped

    line()
    print("ROOM 1: THE MYSTERIOUS LIBRARY")
    print("Dusty books reach up to the ceiling.")
    print("A Talking door gives you a riddle. If you answer correctly a drawer will open")
    print("\nA The door Says:")
    print("'I am not alive but bring to life")
    print("Love, Laughter, beauty, and strife")
    print("Though I don't speak I never fail")
    print("To captivate you wih a tale'")

    if answer_puzzle("Solve the riddle to open the secret drawer.",
                     ["book", "a book"], "You can read me and turn my pages.", 15):
        inventory.append("Brass key")
        print("\nA drawer clicks open. You found a BRASS KEY!")
        print("You feed the key to the door")
        print("The door opens")
        rooms_escaped += 1
        return True
    return False


# -------------------- ROOM 2: THE CLOCK ROOM --------------------

def clock_room():
    global score, lives, rooms_escaped

    line()
    print("ROOM 2: THE CLOCK ROOM")
    print("Three enormous clocks cover the walls.")
    print("A keypad asks for a three-digit code.")
    print("\nA message says:")
    print("'Look carefully at the pattern:'")
    print("2, 4, 8, 16, ?")

    if answer_puzzle("What number comes next?", ["32", "thirty two"],
                     "Each number is double the one before it.", 15):
        print("\nThe keypad flashes green!")
        print("A hidden compartment opens. Inside is a SILVER TOKEN.")
        inventory.append("Silver token")
        rooms_escaped += 1
        return True
    return False


# -------------------- ROOM 3: THE LABORATORY --------------------

def laboratory():
    global score, lives, rooms_escaped

    line()
    print("ROOM 3: THE SECRET LABORATORY")
    print("Bubbling potions glow on a workbench.")
    print("A robot guards the next door.")
    print("\nThe robot says:")
    print("'I am thinking of a number.")
    print("If you multiply me by 3 and add 6, the answer is 21.")
    print("What number am I?'")

    if answer_puzzle("Work out the mystery number.", ["5", "five"],
                     "Work backwards: 21 minus 6, then divide by 3.", 20):
        print("\nThe robot beeps happily and steps aside.")
        print("You found a BLUE CRYSTAL on the workbench!")
        inventory.append("Blue crystal")
        rooms_escaped += 1
        return True
    return False


# -------------------- ROOM 4: THE MIRROR MAZE --------------------

def mirror_maze():
    global score, lives, rooms_escaped

    line()
    print("ROOM 4: THE MIRROR MAZE")
    print("Mirrors stretch in every direction.")
    print("A sign reads:")
    print("'Choose the path that is NOT a dead end.'")
    print("\nYou see three doors:")
    print("A: A door marked EXIT")
    print("B: A door marked EXIT EXIT")
    print("C: A door marked EXIT EXIT EXIT")
    print("\nA clue is scratched into the mirror:")
    print("'Sometimes the answer is hiding in plain sight.'")

    if answer_puzzle("Which door should you choose: A, B or C?",
                     ["a"], "Look for the simplest, real exit sign.", 15):
        print("\nYou chose wisely! The mirror wall slides open.")
        print("Behind it is a GOLDEN GEAR.")
        inventory.append("Golden gear")
        rooms_escaped += 1
        return True
    return False


# -------------------- FINAL ROOM: THE EXIT VAULT --------------------

def final_vault():
    global score, lives

    line()
    print("FINAL ROOM: THE EXIT VAULT")
    print("A giant vault door stands before you.")
    print("There are four spaces for four digits.")
    print("You must use the clues you have collected.")
    print("\nThe vault displays this challenge:")
    print("1) How many sides does a triangle have?")
    print("2) How many legs does a spider have?")
    print("3) How many letters are in the word CAT?")
    print("4) How many wheels does a bicycle have?")

    print("\nPut the four answers together to make the code.")
    hint("Answer each question in order, then join the digits together.")

    correct = False
    for attempt in range(3):
        code = input("\nEnter the four-digit vault code: ").strip()
        if code == "3832":
            correct = True
            break
        print("The vault flashes red. Try again!")
    if correct:
        score += 40
        line()
        print("THE VAULT OPENS!")
        print("Golden light fills the room.")
        print("You have escaped the Mystery Mansion!")
        return True
    else:
        print("\nThe vault locks. You have run out of attempts.")
        return False


# -------------------- MAIN GAME --------------------

def play_game():
    global player, score, lives, hints_used, rooms_escaped

    line()
    print("       THE GREAT ESCAPE: MYSTERY MANSION")
    print("              A PUZZLE ADVENTURE")
    line()
    player = input("\nWelcome, adventurer! What is your name? ").strip()
    if not player:
        player = "Adventurer"

    print("\nHello, " + player + "!")
    print("You have been locked inside a mysterious mansion.")
    print("Solve the puzzles, collect four special objects and escape.")
    print("\nRULES:")
    print("- You have 5 lives.")
    print("- You can ask for a hint in each puzzle.")
    print("- Correct answers earn points.")
    print("- If you lose all your lives, the game ends.")
    print("- Type your answers or choose from the options shown.")
    pause()

    rooms = [
        ("The Library", library),
        ("The Clock Room", clock_room),
        ("The Laboratory", laboratory),
        ("The Mirror Maze", mirror_maze)
    ]

    for room_name, room_function in rooms:
        if lives <= 0:
            break
        print("\nNext destination:", room_name)
        pause()
        room_function()
        status()
        if lives <= 0:
            break

    if lives > 0 and rooms_escaped == 4:
        print("\nYou have collected all four special objects!")
        pause()
        escaped = final_vault()
        if escaped:
            line()
            print("CONGRATULATIONS, " + player.upper() + "!")
            print("YOU ARE THE MYSTERY MANSION CHAMPION!")
            print("Final score:", score)
            print("Hints used:", hints_used)
            print("Rooms escaped: 4 out of 4")
            print("\nThanks for playing!")
            return

    line()
    print("GAME OVER")
    print("Good effort, " + player + "!")
    print("Final score:", score)
    print("Rooms escaped:", rooms_escaped, "out of 4")
    print("You can play again and try a different strategy!")
    print("Thanks for playing!")


if __name__ == "__main__":
    play_game()
