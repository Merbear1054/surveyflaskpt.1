class Question:
    """A question in a survey."""

    def __init__(self, question, choices, allow_text=False):
        self.question = question
        self.choices = choices
        self.allow_text = allow_text

class Survey:
    """A survey containing multiple questions."""

    def __init__(self, title, instructions, questions):
        self.title = title
        self.instructions = instructions
        self.questions = questions

satisfaction_questions = [
    Question("Have you shopped here before?", ["Yes", "No"]),
    Question("How satisfied are you?", ["Very", "Somewhat", "Not at all"]),
    Question("How likely are you to shop here again?", ["Very likely", "Unlikely", "Never"]),
    Question("Would you recommend us to a friend?", ["Yes", "No"])
]

satisfaction_survey = Survey(
    "Customer Satisfaction Survey",
    "We value your feedback. Please answer honestly.",
    satisfaction_questions
)

