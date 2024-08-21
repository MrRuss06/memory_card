from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QRadioButton,  
        QPushButton, QLabel, QButtonGroup,)
from random import shuffle,randint


class Question():
      def __init__(self,question,right_answer,wrong1,wrong2,wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = []
q1 = Question('Какого цвета нет на флаге росии','Зеленый','Синий','Красный','Белый')
question_list.append(q1)
q2 = Question('Какого классов нет в школе','14','9','1','12')
question_list.append(q2)
q3 = Question('Чего нету у ноутбука','блока','экрана','кнопка включения','клавиатуры')
question_list.append(q3)
q4 = Question('Какой планеты нету','круглый3000','марс','нептун','сатурн')
question_list.append(q4)

app = QApplication([])
btn_OK = QPushButton('Ответить')
lb_Question = QLabel('Самый сложный вопрос в мире!')

RadioGroupBox = QGroupBox("Варианты ответов")
rbtn_1 = QRadioButton('Вариант 1')
rbtn_2 = QRadioButton('Вариант 2')
rbtn_3 = QRadioButton('Вариант 3')
rbtn_4 = QRadioButton('Вариант 4')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)


layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1) # два ответа в первый столбец
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) # два ответа во второй столбец
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

# Создаем панель результата
AnsGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel('прав ты или нет?') 
lb_Correct = QLabel('ответ будет тут!') 

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)

# Размещаем все виджеты в окне:
layout_line1 = QHBoxLayout() # вопрос
layout_line2 = QHBoxLayout() # варианты ответов или результат теста
layout_line3 = QHBoxLayout() # кнопка "Ответить"

layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)   
layout_line2.addWidget(AnsGroupBox)  
RadioGroupBox.hide() 

layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2) 
layout_line3.addStretch(1)

layout_card = QVBoxLayout()

layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5) 

def show_result():
        AnsGroupBox.show()
        RadioGroupBox.hide()
        btn_OK.setText('Следующий вопрос')

def show_questoin():
        RadioGroupBox.show()
        AnsGroupBox.hide()
        btn_OK.setText('Ответить')
        RadioGroup.setExclusive(False)
        rbtn_1.setChecked(False)
        rbtn_2.setChecked(False)
        rbtn_3.setChecked(False)
        rbtn_4.setChecked(False)
        RadioGroup.setExclusive(True)

answer = [rbtn_1,rbtn_2,rbtn_3,rbtn_4]

def ask(q: Question):
        shuffle(answer)
        answer[0].setText(q.right_answer)
        answer[1].setText(q.wrong1)
        answer[2].setText(q.wrong2)
        answer[3].setText(q.wrong3)
        lb_Question.setText(q.question)
        lb_Correct.setText(q.right_answer)
        show_questoin()

def show_correct(res):
      lb_Result.setText(res)
      show_result()

def check_answer():
    '''если выбран какой-то вариант ответа, то надо проверить и покозать панель ответов'''
    if answer[0].isChecked():
        show_correct('Правильно!')
        window.score += 1
        print('Статитстика\n-Всего вопросов:', window.total, '\n-Правильных ответов:', window.score)
        print('Рейтинг:', (window.score/window.total*100), '%')
    else:
        if answer[1].isChecked() or answer[2].isChecked() or answer[3].isChecked():    
             show_correct('Неверно!')
        print('Рейтинг:', (window.score/window.total*100), '%')

def next_question():
        window.total += 1
        print('Статистика\n-Всего вопросов:', window.total, '\n-Правильных ответов: ', window.score)
        cur_question = randint(0, len(question_list) - 1)
        q = question_list[cur_question]
        ask(q)

def click_OK():
    if btn_OK.text() == 'Ответить':
            check_answer()
    else:
        next_question()

window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memory Card')
window.resize(400,300)

btn_OK.clicked.connect(click_OK)

window.score = 0
window.total = 0
next_question()
window.show()
app.exec()
