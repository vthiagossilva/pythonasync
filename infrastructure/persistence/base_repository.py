from .connection import get_svely


class BaseRepository:
    def __init__(self):
        self.my_svely = get_svely()

    async def end(self):
        await self.my_svely.close()
