from datetime import datetime

from application.users.entities.user_entity import UserEntity
from .repository import CreateUserRepository


async def create_user_uc(data: dict) -> (str, int):
    if data.get("email") and data.get("password") and data.get("name"):
        repo = CreateUserRepository()

        email_available = await repo.check_available_email(data["email"])
        if email_available:

            user = UserEntity(
                email=data["email"],
                password=data["password"],
                name=data["name"],
                created_at=(datetime.now()),
                updated_at=(datetime.now()),
            )
            user.crypt_password()

            await repo.persist_user(user)
            await repo.end()
            return "Ok", 201
        return "E-mail indisponível", 409
    return "Informações insuficientes", 400
