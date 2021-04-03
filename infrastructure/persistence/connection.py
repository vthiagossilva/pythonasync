from .svely import Svely
from settings import DB_CREDENTIALS


def get_svely(): return Svely(**DB_CREDENTIALS)
