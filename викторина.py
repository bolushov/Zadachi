import tkinter as tk
from tkinter import ttk

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("История Кыргызстана Викторина")
        self.score = 0  # Инициализируем счет
        self.current_question_index = 0  # Индекс текущего вопроса

        self.questions =[
            {
                'question': 'Когда была проведена Туз-тапшир?',
                'options': ['1927', '1948', '1956', '1972'],
                'correct_option': 1  # Индекс правильного ответа
            }
        ]    
        self.questions = [
            {
                'question': 'Когда была проведена Туз-тапшир?',
                'options': ['1927', '1948', '1956', '1972'],
                'correct_option': 1
            },
            {
               'question': 'Какая гора является самой высокой в Кыргызстане?',
               'options': ['Победа', 'Ленин', 'Комсомол', 'Северная Тянь-Шань'],
               'correct_option': 0
           },
           {
               'question': 'Какая река является длиннейшей в Кыргызстане?',
               'options': ['Иссык-Куль', 'Чуй', 'Нарын', 'Талас'],
               'correct_option': 1
           },
           {
               'question': 'Какая дата является Днем Независимости Кыргызстана?',
               'options': ['7 апреля', '31 августа', '24 июня', '9 мая'],
               'correct_option': 1
           },
           {
              'question': 'Какой язык является официальным в Кыргызстане?',
              'options': ['Русский', 'Казахский', 'Киргизский', 'Узбекский'],
              'correct_option': 2
           },
           {
             'question': 'Кто является первым президентом Кыргызстана?',
             'options': ['Атамбаев', 'Акаев', 'Бакиев', 'Джээнбеков'],
             'correct_option': 1
           },
           {
             'question': 'Какая традиционная кыргызская игра использует жеребьевку?',
             'options': ['Улаан кара', 'Кок бору', 'Тогуз кумалак', 'Теннис'],
             'correct_option': 2
           },
           {
             'question': 'Как называется национальное блюдо Кыргызстана из мяса и теста?',
             'options': ['Борщ', 'Плов', 'Манты', 'Салат'],
             'correct_option': 2
           },
           {
             'question': 'Как называется высокогорное озеро в Кыргызстане, одно из самых глубоких в мире?',
             'options': ['Байкал', 'Иссык-Куль', 'Каспийское', 'Чандык'],
             'correct_option': 1
           },
           {
             'question': 'Кто написал национальный гимн Кыргызстана?',
             'options': ['Токтогул Сатылганов', 'Чингиз Айтматов', 'Таалай Исакунов', 'Апас Джумагулов'],
             'correct_option': 0
           }


         ]

        self.question_label = ttk.Label(root, text='', font=('Arial', 16))
        self.question_label.grid(row=0, padx=10, pady=10)

        self.radio_var = tk.IntVar()
        self.radio_buttons = []
        for i in range(4):
            radio_button = ttk.Radiobutton(root, text='', variable=self.radio_var, value=i)
            self.radio_buttons.append(radio_button)
            radio_button.grid(row=i + 1, padx=10, pady=5)

        self.submit_button = ttk.Button(root, text='Ответить', command=self.check_answer)
        self.submit_button.grid(row=5, padx=10, pady=10)

        self.next_question()  # Начнем с первого вопроса

    def next_question(self):
        if self.current_question_index < len(self.questions):
            question_data = self.questions[self.current_question_index]
            self.question_label['text'] = question_data['question']
            for i in range(4):
                self.radio_buttons[i]['text'] = question_data['options'][i]
            self.radio_var.set(-1)  # Сбрасываем выбор
        else:
            self.show_result()

    def check_answer(self):
        selected_option = self.radio_var.get()
        if selected_option == self.questions[self.current_question_index]['correct_option']:
            self.score += 1
        self.current_question_index += 1
        self.next_question()

    def show_result(self):
        result_label = ttk.Label(self.root, text=f'Ваш результат: {self.score}/{len(self.questions)}', font=('Arial', 16))
        result_label.grid(row=6, padx=10, pady=10)
        self.submit_button['state'] = 'disabled'

def main():
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
