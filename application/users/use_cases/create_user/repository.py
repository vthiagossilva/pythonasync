from application.users.entities.user_entity import UserEntity
from infrastructure.persistence.base_repository import BaseRepository


class CreateUserRepository(BaseRepository):
    async def check_available_email(self, email: str) -> bool:
        return await self.my_svely.is_empty("users", "id", f"email = '{email}'")

    async def persist_user(self, user: UserEntity):
        await self.my_svely.insert("users", user)
