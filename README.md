# Templates_FastAPI
Web-приложение для определения заполненных форм.
___
## Стек
Python, FastAPI, Mongodb
___
## Установка
Установить репозиторий
```
git clone https://github.com/Flowmikro/Templates_FastAPI.git
```
Перейти в директорию
```
cd Templates_FastAPI
```
Виртуальная среда
```
python -m venv venv
source venv/bin/activate
```
Установить пакеты
```
pip install -r requirements.txt
```
Запуск сервера
```
uvicorn main:app --reload
```
# Templates_FastAPI
Web-приложение для определения заполненных форм.
## Установка
Установить репозиторий
```
git clone https://github.com/Flowmikro/Templates_FastAPI.git
```
Перейти в директорию
```
cd Templates_FastAPI
```
Виртуальная среда
```
python -m venv venv
source venv/bin/activate
```
Установить пакеты
```
pip install -r requirements.txt
```
Запуск сервера
```
uvicorn main:app --reload
```
Заполнить БД записями
```
cd app 
```
```
python db_entries.py
```
