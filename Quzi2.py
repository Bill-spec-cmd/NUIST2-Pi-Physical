import RPi.GPIO as GPIO
import time

# GPIO Pin Configuration
GREEN_LED = 17  # Correct answer LED pin
RED_LED = 18    # Incorrect answer LED pin
LED_DELAY = 1   # LED light duration (seconds)

def setup_gpio():
    """Initialize GPIO pins for LED control"""
    GPIO.setmode(GPIO.BCM)  # Use BCM GPIO numbering (consistent with Raspberry Pi standard)
    GPIO.setup(GREEN_LED, GPIO.OUT)  # Set as output pin
    GPIO.setup(RED_LED, GPIO.OUT)
    # Turn off LEDs initially
    GPIO.output(GREEN_LED, GPIO.LOW)
    GPIO.output(RED_LED, GPIO.LOW)

def led_feedback(is_correct):
    """Control LED light based on answer result"""
    if is_correct:
        GPIO.output(GREEN_LED, GPIO.HIGH)  # Green LED on for correct
    else:
        GPIO.output(RED_LED, GPIO.HIGH)    # Red LED on for incorrect
    time.sleep(LED_DELAY)  # Keep LED on for set duration
    # Turn off both LEDs
    GPIO.output(GREEN_LED, GPIO.LOW)
    GPIO.output(RED_LED, GPIO.LOW)

def python_quiz():
    """Python knowledge quiz with LED interactive feedback"""
    setup_gpio()  # Initialize GPIO
    score = 0     # Initialize score
    
    # Define Python quiz questions and correct answers (a/b/c)
    quiz_data = [
        {
            "question": "1. Which of the following is NOT a python data type?\na) int\nb) float\nc) rational\nd) string\ne) bool\nYour answer: ",
            "answer": "c"
        },
        {
            "question": "2. Which of the following is NOT a built-in operation in Python?\na) +\nb) %\nc) abs()\nd) sqrt()\nYour answer: ",
            "answer": "d"
        },
        {
            "question": "3. In a mixed-type expression involving ints and floats, Python will convert:\na) floats to ints\nb) ints to strings\nc) floats and ints to strings\nd) ints to floats\nYour answer: ",
            "answer": "d"
        },
        {
            "question": "4. The best structure for implementing a multi-way decision in Python is:\na) if\nb) if-else\nc) if-elif-else\nd) try\nYour answer: ",
            "answer": "c"
        },
        {
            "question": "5. What statement can be executed in the body of a loop to cause it to terminate?\na) if\nb) exit\nc) continue\nd) break\nYour answer: ",
            "answer": "d"
        }
    ]
    
    # Welcome message
    print("Welcome to the Python Basic Quiz (LED Interactive Version)!")
    print("Answer with a/b/c, correct = green light, incorrect = red light.\n")
    
    # Iterate through quiz questions
    for item in quiz_data:
        user_ans = input(item["question"]).strip().lower()
        # Judge answer
        if user_ans == item["answer"]:
            print("Correct!\n")
            score += 1
            led_feedback(is_correct=True)
        else:
            print("Incorrect!\n")
            led_feedback(is_correct=False)
    
    # Output final score
    total_questions = len(quiz_data)
    print("="*30)
    print(f"Quiz Completed! Final Score: {score}/{total_questions}")
    print("="*30)
    
    # Clean up GPIO (critical to avoid pin occupation)
    GPIO.cleanup()
    print("GPIO cleaned up successfully.")

# Run the quiz with LED control
if __name__ == "__main__":
    try:
        python_quiz()
    except KeyboardInterrupt:
        # Handle manual program stop (Ctrl+C)
        GPIO.cleanup()
        print("\nProgram interrupted, GPIO cleaned up.")
