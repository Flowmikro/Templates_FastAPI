# Валидация данных
import re
from datetime import datetime


async def is_date(value: str) -> bool:
    """
    Проверяем является ли значение датой.
    Дата может быть формата DD.MM.YYYY или YYYY-MM-DD.
    """
    if value.count('.') == 2:
        try:
            datetime.strptime(value, "%d.%m.%Y")
        except:
            return False
        else:
            return True
    elif value.count('-') == 2:
        try:
            datetime.strptime(value, "%Y-%m-%d")
        except:
            return False
        else:
            return True
    return False


async def is_phone(value: str) -> bool:
    """
    Проверяем является ли значение телефоном.
    Телефон формата +7 ХХХ ХХХ ХХ ХХ.
    """
    result = re.search('^\+7\s\d{3}\s\d{3}\s\d{2}\s\d{2}$', value)
    if result is None:
        return False
    return True


async def is_email(value: str) -> bool:
    """
     Проверяем является ли значение почтой.
    """
    result = re.search('^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$', value)
    if result is None:
        return False
    return True
