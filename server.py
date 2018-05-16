from flask import Flask, render_template, request, redirect
import data_manager
from datetime import datetime


app = Flask(__name__)
app.secret_key = 'AskMateSecretKey'

@app.route("/")
@app.route("/list", methods=['GET', 'POST'])
def route_list():
    if request.method == 'GET':
        questions = data_manager.get_question_and_title()
        return render_template('list.html', questions=reversed(questions))

    elif request.method == 'POST':
        user_input_username = request.form.get('user_input_username', None)
        user_input_password = request.form.get('user_input_password', None)
        hashed_password = pwhashing.hash_password(user_input_password)

        checking = data_manager.check_user()

        for dict in checking:
            for user in dict:
                if user in checking:
                    return render_template()
                else:
                    message = "Invalid username or password!"
                    return render_template("list.html", message=message)

        database_password = data_manager.get_password(user_input_username)
        is_registered = data_manager.check_user(user_input_username)
        checking_password = pwhashing.verify_password(user_input_password, database_password)

        if is_registered and checking_password:
            session['id'] = data_manager.get_user_id(user_input_username)
            return render_template("list/<username>")
        else:
            message = "Invalid username or password!"
            return render_template('list.html', message=message)

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
    question = data_manager.get_question_by_id(question_id)
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
        return render_template('edit_answer.html', question_id=question_id, answer=answer

    data_manager.update_answer(answer_id, request.form['message'])
    return redirect('/')


@app.route("/question/<question_id>/edit_question", methods=['GET', 'POST'])
def edit_question(question_id):
    if request.method == "GET":
        question = data_manager.question_by_id(question_id)
        return render_template('edit_question.html', question=question, question_id=question_id)
    data_manager.edit_question(request.form['title'], request.form['message'], question_id)
    return redirect('/')


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True,
    )