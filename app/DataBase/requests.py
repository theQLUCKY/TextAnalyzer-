from app.DataBase.models import Document
from app.DataBase.models import session_start


def add_document(filename: str, content: str)-> None:
    """Принимает имя и содержимое файла, добавляет файл в базу и сохраняет в талицу documents"""
    document = Document(filename=filename, content=content)
    try:
        with session_start() as session:
            session.add(document)
            session.commit()
    except Exception:
        print('При добавлении документа произошла ошибка')


def get_documents():
    """Достает все файлы из таблицы documents"""
    try:
        with session_start() as session:
            all_documents = session.query(Document).all()
            return all_documents
    except Exception:
        print('При попытке Получения файлов из базы произошла ошибка')


