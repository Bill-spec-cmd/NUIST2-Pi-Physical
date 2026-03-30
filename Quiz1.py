def quiz():
    # Welcome message
    print("Welcome to the Animal Quiz!")
    print("Answer the following questions (enter the full answer in lowercase):\n")
    
    # Define questions and corresponding correct answers
    questions = [
        "1. What is the largest animal on Earth?: a. Blue Whale, b. Mouse, c. Cat\nYour answer: ",
        "2. Which bird can fly backwards?: a. Cuckoo, b. Eagle, c. Hummingbird\nYour answer: ",
        "3. What is the only mammal capable of flight?: a. Bat, b. Squirrel, c. Dolphin\nYour answer: "
    ]
    answers = [
        "blue whale",
        "hummingbird",
        "bat"
    ]
    
    score = 0  # Initialize score
    
    # Iterate through all questions
    for i in range(len(questions)):
        user_answer = input(questions[i]).strip().lower()
        # Judge answer and update score
        if user_answer == answers[i]:
            print("Correct!\n")
            score += 1
        else:
            print("Incorrect!\n")
    
    # Output final score
    print("Quiz completed!")
    print(f"You got {score}/{len(questions)} questions correct.")

# Run the quiz function
if __name__ == "__main__":
    quiz()
