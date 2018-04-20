from flask import Flask, render_template, request, redirect
import connection
import data_manager
import time

app = Flask(__name__)


@app.route("/")
@app.route("/list")
def list():
    header = data_manager.header()
    questions = connection.get_all_user_story('question.csv')
    return render_template('list.html', headers=header, questions=reversed(questions))


@app.route("/add-question", methods=["GET", "POST"])
def add_question():

    if request.method == "GET":
        return render_template('add_question.html')

    title = request.form.get("title", "")
    message = request.form.get("message", "")
    data_manager.create_question(title, message)

    return redirect("/")


@app.route("/question/<question_id>", methods=['GET'])
def question(question_id):
    question_data = connection.get_question_by_id(question_id)
    user_stories = connection.get_all_user_story("question.csv")
    answers = connection.get_answer_by_id(question_id)
    for item in user_stories:
        if item["id"] == question_id and request.method == "GET":
            item["view_number"] = int(item["view_number"])
            item["view_number"] += 1
            '''mi a faasz ez???'''
            item["view_number"] = str(item["view_number"])
            break
    connection.dict_writer(user_stories, "question.csv")

    return render_template('question_id.html', question_data=question_data, answers=answers)


@app.route("/question/<question_id>/add-answer", methods=['GET','POST'])
def new_answer(question_id):
    question_data = connection.get_question_by_id(question_id)
    if request.method == 'GET':
        return render_template('add_answer.html', question_data=question_data)
    else:
        question_id = question_data['id']
        message = request.form.get('message', '')
        data_manager.save_answer(message, question_id)

        return redirect('/')


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True,
    )
