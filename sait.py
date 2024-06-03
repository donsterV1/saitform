# -*- coding: utf-8 -*-

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Получаем данные из формы
        name = request.form['name']
        age = request.form['age']
        university = request.form['university']
        like_university = request.form['like_university']

        # Записываем ответы в файл
        with open('answers.txt', 'a', encoding='utf-8') as f:
            f.write(f'Имя: {name}, Возраст: {age}, ВУЗ: {university}, Нравится ВУЗ: {like_university}\n')

        # Возвращаем шаблон с благодарностью за заполнение анкеты
        return render_template('thanks.html')
    return render_template('form.html')

if __name__ == '__main__':

    app.run(debug=True)
