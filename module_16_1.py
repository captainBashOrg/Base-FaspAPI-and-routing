from fastapi import FastAPI

# python -m uvicorn main:app --reload


app = FastAPI()

@app.get("/user/admin/")
async def welcome_admin(): # -> dict:
    return ( "Вы вошли как администратор" )

@app.get("/user/{user_id}")
async def read_user_id(user_id: int) :
    return ( f"Вы вошли как пользователь № {user_id}" )

@app.get("/user")
async def user_reader(username:str, age: int):
    return ( f"Информация о пользователе. Имя: <{username}>, Возраст: <{age}>" )

@app.get("/")
async def welcome() :
    return ("Главная страница")