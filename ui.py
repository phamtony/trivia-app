from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.canvas = Canvas(width=300, height=250, highlightthickness=0, bg="white")

        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

        self.true_button_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=self.true_button_img, highlightthickness=0, bd=0, command=self.checking_true)
        self.true_button.grid(row=2, column=0)

        self.false_button_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=self.false_button_img, highlightthickness=0, bd=0, command=self.checking_false)
        self.false_button.grid(row=2, column=1)

        self.question = self.canvas.create_text(150, 125, width=280, fill="black", font=FONT, text="Question here")
        self.score = Label(text="Score: 0", bg=THEME_COLOR)
        self.score.grid(row=0, column=1)

        self.get_next_q()

        self.window.mainloop()


    def get_next_q(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q_text)
        else:
            self.canvas.itemconfig(self.question, text="You reached to the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def checking_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def checking_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback((is_right))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_q)