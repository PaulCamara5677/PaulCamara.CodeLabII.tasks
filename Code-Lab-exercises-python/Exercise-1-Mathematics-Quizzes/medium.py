import _tkinter

def display_menu():
    print("DIFFICULTY LEVEL")
    print(" 1. Easy")
    print(" 2. Moderate")
    print(" 3. Advanced")
    
def random_int(difficulty):
    if difficulty == 1:
        return _tkinter.randint(0, 9)  # Easy: single digit
    elif difficulty == 2:
        return _tkinter.randint(10, 99)  # Moderate: double digits
    elif difficulty == 3:
        return _tkinter.randint(1000, 9999)  # Advanced: four digits

def decide_operation():
    return _tkinter.choice(['+', '-'])

def display_problem(difficulty):
    num1 = random_int(difficulty)
    num2 = random_int(difficulty)
    operation = decide_operation()
    
    if operation == '+':
        question = f"{num1} + {num2} = "
        correct_answer = num1 + num2
    else:
        question = f"{num1} - {num2} = "
        correct_answer = num1 - num2
        
    return question, correct_answer

def is_correct(user_answer, correct_answer):
    return user_answer == correct_answer

def display_results(score):
    print(f"\nYour final score is: {score} out of 100")
    if score >= 90:
        print("Rank: A+")
    elif score >= 80:
        print("Rank: A")
    elif score >= 70:
        print("Rank: B")
    elif score >= 60:
        print("Rank: C")
    elif score >= 50:
        print("Rank: D")
    else:
        print("Rank: F")

def quiz():
    score = 0
    for _ in range(10):
        question, correct_answer = display_problem( 'difficulty' )
        for attempt in range(2):  # Two attempts
            user_answer = int(input(question))
            if is_correct(user_answer, correct_answer):
                if attempt == 0:
                    score += 10  # First attempt score
                else:
                    score += 5   # Second attempt score
                print("Correct!")
                break
            else:
                print("Incorrect, try again." if attempt == 0 else "Still incorrect.")
    
    display_results(score)

def main():
    while True:
        display_menu()
        difficulty = int(input("Select difficulty (1-3): "))
        if difficulty not in [1, 2, 3]:
            print("Invalid selection. Please try again.")
            continue
        
        quiz()
        
        play_again = input("\nWould you like to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

if __name__ == "__main__":
    main()
