import csv
import os

DATA_HEADER = ["id", "submission_time", "view_number", "vote_number", "title", "message", "image", "question_id"]


def get_all_user_story(file_name):
    with open(file_name) as csvfile:
        user_story = []
        spamreader = csv.DictReader(csvfile)
        for row in spamreader:
            user_story.append(row)
        return user_story


def dict_append(values, file_name):
    with open(file_name, 'a') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=DATA_HEADER)
        writer.writerow(values)


def get_question_by_id(user_id):
    all_user_stories = get_all_user_story('question.csv')
    question = None
    for story in all_user_stories:
        if story['id'] == user_id:
            question = story
    return question


def dict_writer(values, file_name):
    with open(file_name, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=DATA_HEADER)
        writer.writeheader()
        writer.writerows(values)


def get_answer_by_id(user_id):
    all_answers = get_all_user_story('answer.csv')
    list_of_answers = []
    for any_answer in all_answers:
        if int(any_answer['question_id']) == int(user_id):
            list_of_answers.append(any_answer['message'])
    return list_of_answers