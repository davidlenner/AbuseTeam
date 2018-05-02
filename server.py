from flask import Flask, render_template, request, redirect
import data_manager


app = Flask(__name__)


@app.route("/")
@app.route("/list")
def list():
    questions = data_manager.get_question_and_title()
    return render_template('list.html', questions=reversed(questions))


@app.route("/add-question", methods=["GET", "POST"])
def add_question():

    if request.method == "GET":
        return render_template('add_question.html')

    data_manager.add_question(request.form['title'], request.form['message'])
    return redirect("/")


@app.route("/question/<question_id>", methods=['GET'])
def question(question_id):
    answer = data_manager.get_answers(question_id)
    question = data_manager.question_by_id(question_id)
    return render_template('question_id.html', question=question, answer=answer)


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
