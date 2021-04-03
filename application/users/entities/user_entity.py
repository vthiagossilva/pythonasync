from datetime import datetime
from hashlib import  sha512


class UserEntity:
    def __init__(self,
                 email: str,
                 name: str,
                 password: str,
                 created_at: datetime,
                 updated_at: datetime,
                 id: int= None,
                 last_login: datetime = None,
                 ):
        self.id: int = id
        self.email: str = email
        self.name: str = name
        self.password: str = password
        self.created_at: datetime = created_at
        self.updated_at: datetime = updated_at
        self.last_login: datetime = last_login

    def crypt_password(self):
        self.password = sha512(self.password.encode('utf-8')).hexdigest()
