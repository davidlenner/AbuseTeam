from flask import Flask, render_template, request, redirect
import data_manager
from datetime import datetime
import pwhashing


app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def list():
    questions = data_manager.get_question_and_title()
    return render_template('list.html', questions=reversed(questions))


@app.route("/add-question", methods=["GET", "POST"])
def add_question():
    if request.method == "GET":
        return render_template('add_question.html')
    dt = datetime.now()
    data_manager.add_question(request.form['title'], request.form['message'], dt)
    return redirect("/")


@app.route("/question/<question_id>", methods=['GET'])
def question(question_id):
    answer = data_manager.get_answers(question_id)
    question = data_manager.question_by_id(question_id)
    return render_template('question_id.html', question=question, answer=answer, question_id=question_id)


@app.route("/question/<question_id>/add-answer", methods=['GET', 'POST'])
def add_answer(question_id):
    question = data_manager.question_by_id(question_id)
    if request.method == 'GET':
        return render_template('add_answer.html', question=question)
    message = request.form.get('message', '')
    dt = datetime.now()
    data_manager.add_answer(question_id, message, dt)
    return redirect('/')


@app.route("/answer/<answer_id>/edit_answer", methods=['GET', 'POST'])
def edit_answer(answer_id):
    if request.method == 'GET':
        answer = data_manager.get_answer_by_id(answer_id)
        return render_template('edit_answer.html', answer=answer)
    data_manager.update_answer(answer_id, request.form['message'])
    return redirect('/')


@app.route("/question/<question_id>/edit_question", methods=['GET', 'POST'])
def edit_question(question_id):
    if request.method == "GET":
        question = data_manager.question_by_id(question_id)
        return render_template('edit_question.html', question=question, question_id=question)
    data_manager.edit_question(request.form['title'], request.form['message'], question_id)
    return redirect('/')


@app.route("/registration", methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':
        usernames = data_manager.check_usernames()
        username = request.form.get('username', '')
        for dict in usernames:
            for names in dict:
                if names == username:
                    time = datetime.now()
                    hashedpw = pwhashing.hash_password(request.form.get('password', ''))
                    data_manager.registration(username, hashedpw, time)
                    return redirect('/')
                else:
                    used_name = 'True'
                    return render_template('registration.html', used_name=used_name)
    return render_template('registration.html')


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True,
    )
