class Authentication:
    USERS = [{
        "username": "user1",
        "password": "pwd1"
    }]

    def login(self, username, password):
        u = self.fetch_user(username)
        if not u or u["password"] != password:
            return None
        return dict(u)

    def fetch_user(self, username):
        for u in self.USERS:
            if u['username'] == username:
                return dict(u)
            else:
                return None
