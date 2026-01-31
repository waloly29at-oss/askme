class QuestionManager:
    def __init__(self):
        self.file_path = "questions.txt"

    def add_question(self, question):
        # بنجهز السطر: ID السؤال، اللي سأل، اللي اتسأل، النص، والرد (فاضي حالياً)
        line = f"{question.q_id},{question.parent_id},{question.from_user_id},{question.to_user_id},{question.q_text},no answer\n"
        with open(self.file_path, "a") as file:
            file.write(line)
    def get_questions_to_user(self, user_id):
        user_questions = []
        try:
            with open(self.file_path, "r") as file:
                for line in file:
                    data = line.strip().split(',')
                    if len(data) >= 4 and data[3] == user_id: # لو الـ to_user_id هو اليوزر الحالي
                        user_questions.append(line.strip())
            return user_questions
        except FileNotFoundError:
            return []
    def answer_question(self, question_id, new_answer):
        all_questions = []
        try:
            # 1. بنقرأ كل الأسئلة اللي في الملف
            with open(self.file_path, "r") as file:
                for line in file:
                    data = line.strip().split(',')
                    # لو لقينا الـ ID اللي اليوزر دخله، بنعدل الإجابة
                    if len(data) >= 6 and data[0] == question_id:
                        data[5] = new_answer
                        all_questions.append(",".join(data) + "\n")
                    else:
                        all_questions.append(line)
            
            # 2. بنمسح الملف ونكتبه من جديد بالبيانات المعدلة
            with open(self.file_path, "w") as file:
                file.writelines(all_questions)
        except FileNotFoundError:
            print("No questions file found.")        