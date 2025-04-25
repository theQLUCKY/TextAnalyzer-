from flask import Flask
from flask import render_template, request
from collections import Counter

from app.handlers import get_words, get_idf
from app.DataBase.models import start
from app.DataBase.requests import get_documents, add_document


app = Flask(__name__)

text ='Загрузите txt файл и узнайте TF, IDF, количество слов в файле и Количество встреч слова в файле'

@app.route('/', methods=['GET', 'POST'])
def index() :
    """Функция принимает файл и отдает результат в index.html для формирования таблицы"""
    if request.method == 'POST':

        file = request.files['file']
        filename = file.filename

        if file and filename.endswith('.txt'):

            content = file.read().decode('utf-8')

            if content:

                add_document(filename=filename,content=content)

                all_docs = get_documents()
                all_words = [get_words(doc.content) for doc in all_docs]

                idf_score = get_idf(all_words)
                words = get_words(content)
                word_counts = Counter(words).items()

                table_data = [{
                    'word': word,
                    'tf': round(count / len(words), 6),
                    'count': count,
                    'length': len(words),
                    'idf': round(idf_score.get(word, 0.0), 4)
                } for word, count in word_counts]
                # Создаем список со словарями для каждого слова с результатами

                table_data = sorted(table_data, key=lambda x: x['idf'], reverse=True)[:50]
                # Сортируем в порядке убывания и ограничиваем 50-ю словами

                return render_template('index.html', table_data=table_data)
            file_empty = 'Файл пуст'
            return render_template('index.html',file_empty=file_empty)
        bad_format = 'Файл не в формате txt'
        return render_template('index.html',bad_format=bad_format)
    return render_template('index.html', new=text)


if __name__ == '__main__':
    start()
    app.run(debug=True)
    #debug служит для отладки сайта (показывает информацию об ошибках на сайте)

