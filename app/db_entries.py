# Заполняет БД записями
from database import collection

db_templates = [
    {
        "name": "User registration by phone number and email",
        "user_phone": "phone",
        "user_email": "email",
    },
    {
        "name": "Employee's date of birth",
        "employee_name": "text",
        "date_of_birth": "date",
    },
    {
        "name": "Employee_phone_number",
        "employee_name": "text",
        "employee_phone_number": "phone",
    },
    {
        "name": "User_blog",
        "first_name": "text",
        "user_post": "text",
    },
]

collection.insert_many(db_templates)
