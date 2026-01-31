from managers.user_manager import UserManager
from managers.question_manager import QuestionManager
from models.user import User
from models.question import Question
import random

def main():
    manager = UserManager()
    q_manager = QuestionManager()
    
    while True:
        print("\n--- AskMe Menu ---")
        print("1: Login")
        print("2: Sign Up")
        print("3: Exit")
        
        choice = input("Enter choice: ")

        if choice == '1':
            username = input("Enter username: ")
            pwd = input("Enter password: ")
            
            if manager.login(username, pwd):
                print(f"\nWelcome back, {username}!")
                while True:
                    print("\n--- User Menu ---")
                    print("1: Ask Question")
                    print("2: List Questions To Me")                  
                    print("3: Answer Question")
                    print("4: Logout")
                    
                    user_choice = input("Enter choice: ")
                    
                    if user_choice == '1':
                        to_id = input("Enter User ID to ask: ")
                        q_text = input("Enter your question: ")
                        from models.question import Question
                        
                        
                        new_q = Question(
                            q_id=random.randint(100, 999),
                            parent_id=-1,
                            from_user_id=username,
                            to_user_id=to_id,
                            q_text=q_text

                        )
                        q_manager.add_question(new_q)
                        print("Question sent successfully!")

                    elif user_choice == '2':
                        questions = q_manager.get_questions_to_user(username)
                        print(f"\n--- Questions to {username} ---")
                        if not questions:
                            print("No questions found.")
                        for q in questions:
                            print(q)    
                    elif user_choice == '3': # نفترض 3 هي Answer Question
                        q_id = input("Enter Question ID to answer: ")
                        ans = input("Enter your answer: ")
                        q_manager.answer_question(q_id, ans)
                        print("Answered successfully!")
                        
                    elif user_choice == '4':
                        print("Logging out...")
                        break
            else:
                print("Invalid username or password!")

        elif choice == '2':
            print("\n--- Welcome to Sign Up ---")
            u_id = random.randint(1, 100)
            u_name = input("Enter username: ")
            u_pwd = input("Enter password: ")
            u_real_name = input("Enter name: ")
            u_email = input("Enter email: ")
            u_anon = input("Allow anonymous? (0 or 1): ")
            
            new_user = User(u_id, u_name, u_pwd, u_real_name, u_email, u_anon)
            manager.add_user(new_user)
            print("User saved successfully! You can now login.")

        elif choice == '3':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()