from flask import Flask, request, render_template, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret-key"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

responses = []

@app.route("/")
def show_start():
    """Show survey start page."""
    return render_template("start.html", survey=satisfaction_survey)

@app.route("/questions/<int:qid>")
def show_question(qid):
    """Show current question."""
    if len(responses) == len(satisfaction_survey.questions):
        return redirect("/thank-you")

    if qid != len(responses):
        flash("You're trying to access an invalid question.")
        return redirect(f"/questions/{len(responses)}")

    question = satisfaction_survey.questions[qid]
    return render_template("question.html", question=question, qid=qid)

@app.route("/answer", methods=["POST"])
def handle_answer():
    """Handle answer and redirect to next question."""
    answer = request.form["answer"]
    responses.append(answer)

    if len(responses) == len(satisfaction_survey.questions):
        return redirect("/thank-you")
    else:
        return redirect(f"/questions/{len(responses)}")

@app.route("/thank-you")
def thank_you():
    """Thank the user for completing the survey."""
    return render_template("thank_you.html")

