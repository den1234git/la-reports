import random

def generate_question(operation):
    if operation == 'add':
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        question = f"{a} + {b} = "
    elif operation == 'subtract':
        a = random.randint(1, 100)
        b = random.randint(1, a)
        question = f"{a} - {b} = "
    return question

def main():
    print("Welcome to the Calculation Drill!")
    print("Type 'add' for addition or 'subtract' for subtraction.")
    operation = input("Choose an operation: ").strip().lower()
    
    if operation not in ['add', 'subtract']:
        print("Invalid operation. Please choose 'add' or 'subtract'.")
        return
    
    score = 0
    num_questions = 5  # 5 questions per session
    
    for _ in range(num_questions):
        question = generate_question(operation)
        print(question)
        user_answer = input("Your answer: ").strip()
        
        try:
            user_answer = int(user_answer)
            if operation == 'add':
                correct_answer = random.randint(1, 100) + random.randint(1, 100)
            elif operation == 'subtract':
                correct_answer = random.randint(1, 100) - random.randint(1, 100)
            
            if user_answer == correct_answer:
                print("Correct!")
                score += 1
            else:
                print(f"Incorrect. The correct answer is {correct_answer}.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    print(f"Session complete. Your final score is {score}/{num_questions}.")

if __name__ == "__main__":
    main()