from models.user import User

class UserManager:
    def __init__(self):
        self.users_file = "users.txt"
    
    def add_user(self, user):
        # دالة لتحويل بيانات المستخدم لسطر وحفظه في الملف
        with open(self.users_file, "a") as file:
            line = f"{user.user_id},{user.username},{user.password},{user.name},{user.email},{user.allow_anonymous}\n"
            file.write(line)

    def login(self, username, password):
     with open(self.users_file, "r") as file:
         lines = file.readlines()
         for line in lines:
                # بنشيل المسافات ونقسم السطر عند كل (,)
                data = line.strip().split(',')
                # data[1] هو الـ username و data[2] هو الـ password
                if data[1] == username and data[2] == password:
                    return True  # لقاه وصح
     return False  # خلص الملف وملقاهوش
    