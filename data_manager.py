import util
import connection
import time

DATA_HEADER = ["id", "submission_time", "view_number", "vote_number", "question_id", "title", "message", "image"]


def id_generator():
    user_stories = connection.get_all_user_story('question.csv')
    id = 0
    for item in user_stories:
        if item['id'] is not None:
            id += 1
    return id


def header():
    return DATA_HEADER


def create_question(title, message):
    question_id = id_generator()
    submission_time = time.strftime("%Y/%m/%d %H:%M:%S")
    new_question = {
        "id": question_id,
        "title": title,
        "message": message,
        "submission_time": submission_time,
        "view_number": 1
    }
    connection.dict_append(new_question, 'question.csv')


def get_id():
    user_stories = connection.get_all_user_story('question.csv')
    for item in user_stories:
        return item['id']


def save_answer(message, question_id):
    submission_time = time.strftime("%Y/%m/%d %H:%M:%S")
    id = id_generator()
    new_answer = {
        'id': id,
        'submission_time': submission_time,
        'message': message,
        'question_id': question_id

    }
    connection.dict_append(new_answer, 'answer.csv')

