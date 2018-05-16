from flask import Flask, render_template, request, redirect, session
import data_manager
from datetime import datetime
import pwhashing

app = Flask(__name__)
app.secret_key = 'AskMateSecretKey'


@app.route("/")
@app.route("/list", methods=['GET', 'POST'])
def route_list():
    questions = data_manager.get_questions()
    if request.method == 'GET':
        return render_template('list.html', questions=reversed(questions))

    elif request.method == 'POST':
        user_input_username = request.form['user_input_username']
        user_input_password = request.form['user_input_password']
        user_database_password = data_manager.get_password(user_input_username)
        for dict in user_database_password:
            for key, value in dict.items():
                if pwhashing.verify_password(user_input_password, value):
                    session['user_id'] = data_manager.get_user_id(user_input_username)
                    is_logged_in = "true"
                    message = "Hi " + user_input_username + "!"
                    return render_template('list.html', questions=reversed(questions), is_logged_in=is_logged_in, message=message)

                else:
                    message = "Invalid username or password!"
                    is_logged_in = "false"
                    return render_template('list.html', questions=reversed(questions), is_logged_in=is_logged_in, message=message)


@app.route('/add-question', methods=['GET', 'POST'])
def add_question():
    if request.method == 'GET':
        return render_template('add_question.html')
    dt = datetime.now()
    for dict in session['user_id']:
        for key, value in dict.items():
            data_manager.add_question(request.form['title'], request.form['message'], dt, value)
            return redirect('/')


@app.route('/question/<question_id>', methods=['GET'])
def question_by_id(question_id):
    answer = data_manager.get_answers(question_id)
    question = data_manager.get_question_by_id(question_id)
    return render_template('question_id.html', question=question, answer=answer, question_id=question_id)


@app.route('/question/<question_id>/edit-question', methods=['GET', 'POST'])
def edit_question(question_id):
    if request.method == 'GET':
        question = data_manager.get_question_by_id(question_id)
        return render_template('edit_question.html', question=question, question_id=question_id)
    data_manager.edit_question(request.form['title'], request.form['message'], question_id)
    return redirect('/')


@app.route('/question/<question_id>/delete-question')
def delete_question(question_id):
    data_manager.delete_answer_by_question_id(question_id)
    data_manager.delete_question(question_id)
    return redirect('/')


@app.route('/question/<question_id>/add-answer', methods=['GET', 'POST'])
def add_answer(question_id):
    question = data_manager.get_question_by_id(question_id)
    if request.method == 'GET':
        return render_template('add_answer.html', question=question)

    message = request.form.get('message', '')
    dt = datetime.now()
    for dict in session['user_id']:
        for key, value in dict.items():
            data_manager.add_answer(question_id, message, dt, value)
            return redirect('/')


@app.route('/question/<question_id>/answer/<answer_id>/edit-answer', methods=['GET', 'POST'])
def edit_answer(question_id, answer_id):
    data_manager.get_question_by_id(question_id)
    if request.method == 'GET':
        answer = data_manager.get_answer_by_id(answer_id)
        return render_template('edit_answer.html', answer=answer)
    data_manager.edit_answer(answer_id, request.form['message'])
    return redirect('/')


@app.route('/question/<question_id>/answer/<answer_id>/delete-answer')
def delete_answer(question_id, answer_id):
    data_manager.get_question_by_id(question_id)
    data_manager.delete_answer(answer_id)
    return redirect('/')


@app.route("/registration", methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':
        usernames = data_manager.check_usernames()
        username = request.form.get('username', '')
        for dict in usernames:
            for key, values in dict.items():
                if values != username:
                    time = datetime.now()
                    hashedpw = pwhashing.hash_password(request.form.get('password', ''))
                    data_manager.registration(username, hashedpw, time)
                    return redirect('/')
                elif values == username:
                    used_name = 'False'
                    return render_template('registration.html', used_name=used_name)
    return render_template('registration.html')


@app.route("/logged_out", methods=['POST'])
def logged_out():
    session.clear()
    return redirect('/list')


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True,
    )