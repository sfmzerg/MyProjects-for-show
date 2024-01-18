from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from database_api.database_api import *
import uvicorn
from models import *
from scripts.core import *
import json
import time
app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=origins,
    allow_headers=origins,
)

session_pattern = {
    "weights": {
        "math":1,
        "discrete_math":1,
        "informatics":1,
        "microprocessors":1,
        "sport_programming":1,
        "assembly_programming":1,
        "high_level_programming":1,
        "mobile_development":1,
        "web_development":1,
        "data_science":1,
        "data_security":1,
        "supercomputers":1,
        "neural_networks":1,
        "machine_learning":1,
        "automation":1,
        "architecture":1,
        "design":1,
        "project_management":1,
        "english":1
    },
    "answered": []
}

# Роут для авторизации пользователя, на вход - почта и пароль


@app.post('/login', status_code=200)
async def login(body: LoginModel):
    if authorize_user(body.email, body.password) == [(1,)]:
        result = select_user_data(body.email)
        result_dictionary = {}
        if result != -1:
            result_dictionary.update(
                statusCode='200',
                data=result
            )
            return result_dictionary
        else:
            print('Ошибка входа')
            raise HTTPException(status_code=400, detail="Ошибка на сервере")
    else:
        print('Ошибка входа')
        raise HTTPException(status_code=400, detail="Неверный логин или пароль")


# Роут для регистрации, на вход почта, пароль, имя, фамилия, отчество, университет
@app.post('/registration', status_code=200)
async def registration(body: RegistrModel):
    if authorize_user(body.email, body.password) != [(1,)]:
        add_new_user(body.email, body.password, body.firstName, body.secondName, body.thirdName, body.university)
        result = select_user_data(body.email)
        result_dictionary = {}
        if result != -1:
            result_dictionary.update(
                statusCode='200',
                data=result
            )
            return result_dictionary
        else:
            print('Ошибка регистрации')
            raise HTTPException(status_code=400, detail="Ошибка на сервере")
    else:
        print('Ошибка регистрации')
        raise HTTPException(status_code=400, detail="Такой пользователь уже существует")


# Роут кафедр
@app.post('/departments', status_code=200)
async def departments(body: CafedraModel):
    if body.id != -1:
        if select_cafedra_by_id(body.id):
            result = select_cafedra_by_id(body.id)
            result_dictionary = {}
            result_dictionary.update(
                statusCode='200',
                data=result
            )
            return result_dictionary
        else:
            raise HTTPException(status_code=400, detail="Такой кафедры не существует")
    else:
        return select_cafedras()


# Роут для получения нужного вопроса
@app.post('/relevant-question', status_code=200)
async def get_relevant_question(body: UserSessionDataModel):
    try:
        dictionary = {'weights': body.weights, 'answered': body.answered}
        result_question = choose_relevant_question(dictionary)
        result_dictionary = {}
        if result_question is not None:
            result_dictionary.update(
                statusCode='200',
                data=result_question
            )
            return result_dictionary
        else:
            result_question = choose_relevant_question(dictionary)
            if result_question is not None:
                result_dictionary.update(
                    statusCode='200',
                    data=result_question
                )
                return result_dictionary
            else:
                result_question = choose_relevant_question(dictionary)
                if result_question is not None:
                    result_dictionary.update(
                        statusCode='200',
                        data=result_question
                    )
                    return result_dictionary
    except:
        print('Ошибка запроса вопроса')
        raise HTTPException(status_code=204, detail='Нет данных')


# Роут для отправки дефолтной сессии
@app.get('/default-session', status_code=200)
async def session_default():
    dictionary = {}
    with open('session_pattern.json', 'r', encoding='UTF-8') as session_pattern:
        dictionary.update(
            statusCode='200',
            data=session_pattern.read(),
            totalCount=return_how_many_questions()
        )
        return dictionary


# Обновление сессии
@app.post('/answer-question', status_code=200)
async def answer_question(body: AnswerQuestion):
    dictionary = {}
    new_session = update_weights(body.session, body.id, body.answer)
    dictionary.update(
        statusCode='200',
        data=new_session
    )
    return dictionary


# Обновляет данные пользователя
@app.post('/change-user-information', status_code=200)
async def change_user_data(body: UpdateUserData):
    if update_user_data(body.email, body.new_email, body.new_password, body.new_name, body.new_surname,
                        body.new_patronymic, body.new_university) == [0]:
        dictionary = {}
        dictionary.update(
            statusCode='200',
            data=select_user_data(body.email)
        )
        return dictionary
    else:
        print('Ошибка обновления пользователя')
        raise HTTPException(status_code=400, detail='Такого пользователя не существует')


# Восстановление пароля


@app.post('/restore-password', status_code=200)
async def restore_password(body: RestorePassword):
    restore_user_password(body.email, body.password)
    dictionary = {}
    dictionary.update(
        statusCode='200',
        data=select_user_data(body.email)
    )
    return dictionary


# Возврат данных юзера по его почте
@app.post('/take-user-data', status_code=200)
async def take_user_data(body: ResultModel):
    result = select_user_data(body.email)
    dictionary = {}
    dictionary.update(
        statusCode='200',
        data=result
    )
    return dictionary


# Фиксирование результата пользователя
@app.post('/last-user-answer', status_code=200)
async def last_user_answer(body: LastAnswer):
    scores = calculate_cafedras_score(body.session)
    result = insert_table_results(body.email, body.session, scores, body.time)
    dictionary = {}

    if (result == 200):
        dictionary.update(
            statusCode='200'
        )
    else:
        dictionary.update(
            statusCode='400'
        )
    
    return dictionary


# Получение последнего результата пользователя
@app.post('/last-user-result', status_code=200)
async def last_user_result(body: LastResult):
    result = select_last_result(body.email)
    dictionary = {}
    dictionary.update(
        statusCode='200',
        data=result
    )
    return dictionary

@app.get('/', status_code=200)
async def first_data():
    return 'hello world'


if __name__ == "__main__":
    uvicorn.run('main:app', port=5000, reload=True)
