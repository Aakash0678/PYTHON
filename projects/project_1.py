import random

print("-----Snake🐍,Water💧,Gun🔫 Game-------")
yourScore = 0
ComputerScore = 0

# A list to help us print names instead of numbers
options = {1: "Snake 🐍", 2: "Water 💧", 3: "Gun 🔫"}

print(" 1 = Snake \n 2 = Water \n 3 = Gun \n 4 = Exit ")

while True:
    try:
        your_choice = int(input("You choose 👉🏻  "))
    except ValueError:
        print("Please enter a number!")
        continue

    # Exit condition
    if your_choice == 4:
        print("-----Final Scores are-----")
        print(f" Your Score = {yourScore} \n Computer Score = {ComputerScore}")
        if yourScore > ComputerScore:
            print("Congratulations🥳 You Win the game")
        elif yourScore < ComputerScore:
            print("Hard Luck🤖 You loose.")
        else:
            print("It's a tie 🫂")
        break
    
    # Validation
    if your_choice not in [1, 2, 3]:
        print("Enter a valid choice (1-4) 🫵")
        continue

    # Computer plays
    computer_choice = random.choice([1, 2, 3])
    
    # Reveal choices (The UX improvement)
    print(f"Computer chose: {options[computer_choice]}")

    # Game Logic (Simplified)
    if your_choice == computer_choice:
        print("It's a tie 🤝")
    
    # We only need to check the WIN conditions. Everything else is a loss.
    elif (your_choice == 1 and computer_choice == 2) or \
         (your_choice == 2 and computer_choice == 3) or \
         (your_choice == 3 and computer_choice == 1):
        print("Yay🙌 You Win this round!")
        yourScore += 1
    
    else:
        print("OOPS😬 You Loose this round!")
        ComputerScore += 1

    # Print score ONCE at the end
    print(f"Score: You {yourScore} - {ComputerScore} CPU")
    print("---Next Round---\n")