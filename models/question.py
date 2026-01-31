class Question:
    def __init__(self, q_id, parent_id, from_user_id, to_user_id, q_text, answer=""):
        self.q_id = q_id    # رقم السؤال
        self.parent_id = parent_id # رقم السؤال الأصلي (لو هو رد) أو -1 (لو هو سؤال رئيسي)
        self.from_user_id = from_user_id  #who asked
        self.to_user_id = to_user_id #who recieved     
        self.q_text = q_text
        self.answer = answer