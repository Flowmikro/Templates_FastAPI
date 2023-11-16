# Сервисы
from .utils import is_phone, is_email, is_date
from .database import collection


async def define_a_template(data: dict[str, str]) -> dict[str, str]:
    """
    Определяет шаблон, и возвращает название шаблона.
    Если шаблон не найден вернет типы полей.
    """
    types_found: dict[str, str] = {}
    for key, value in data.items():
        if await is_date(value):
            types_found[key] = 'date'
        elif await is_phone(value):
            types_found[key] = 'phone'
        elif await is_email(value):
            types_found[key] = 'email'
        else:
            types_found[key] = 'text'

    cursor = collection.find({}, {'_id': 0})
    list_template: list[dict[str, str]] = [template for template in await cursor.to_list(length=100)]
    for form in list_template:
        template_name = form.pop('name')
        for values in form.values():
            if values not in types_found.values():
                break
        else:
            return {'form_name': template_name}

    else:
        return types_found

