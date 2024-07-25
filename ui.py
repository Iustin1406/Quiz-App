from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
GOOD_ANSWER_BG = "#90EE90"
WRONG_ANSWER_BG = "#f52727"


class Interface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quiz App")
        self.window.configure(background=THEME_COLOR)

        self.score_label = Label(text="Score: 0", font=("Arial", 20), background=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1, padx=20, pady=20)

        # Question Canvas
        self.canvas = Canvas(width=300, height=250, background="white")
        self.canvas.grid(row=1, column=0, padx=20, pady=20, columnspan=2)
        self.question = self.canvas.create_text(150, 125, width=280, text="Questioon Text",
                                                font=("Arial", 20, "italic"))

        # Buttons
        true_btn_path = PhotoImage(file="images/true.png")
        false_btn_path = PhotoImage(file="images/false.png")
        self.true_button = Button(image=true_btn_path, command=self.answer_true)
        self.true_button.grid(row=2, column=0)
        self.false_button = Button(image=false_btn_path, command=self.answer_false)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()
        self.window.mainloop()

    def answer_true(self):
        if self.quiz.current_question.answer == "True":
            self.quiz.score += 1
            self.score_label.configure(text=f"Score: {self.quiz.score}")
            self.canvas.config(background=GOOD_ANSWER_BG)
        else:
            self.canvas.config(background=WRONG_ANSWER_BG)
        self.window.after(1000, self.get_next_question)

    def answer_false(self):
        if self.quiz.current_question.answer == "False":
            self.quiz.score += 1
            self.canvas.config(background=GOOD_ANSWER_BG)
            self.score_label.configure(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.config(background=WRONG_ANSWER_BG)
        self.window.after(1000, self.get_next_question)

    def get_next_question(self):
        if self.quiz.still_has_questions():
            question_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=question_text)
            self.canvas.config(background="white")
        else:
            self.canvas.config(background="white")
            self.canvas.itemconfig(self.question, text=f"You've completed the quiz!\nFinal Score: {self.quiz.score}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
