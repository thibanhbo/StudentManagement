class Admin:
    def __init__(self, username, role):
        self.username = username
        self.role = role

    def show_info(self):
        print(f"Admin: {self.username} - Role: {self.role}")
