# TextAnalyzer 
## Для запуска сайта необходимо подключить базу данных, а так же установить Flask и SQLAlchemy 

### <em>Для подключения к базе в файл <b>config.py</b> необходимо вставить ссылку для подключения </em>

- По умолчанию вставлена ссылка: <b>postgresql+psycopg2://user_name:password@localhost:5432/db_name</b>
- <b>user_name </b> замените на свой 
- вместо <b> password </b> введите пароль если он есть
- если подключаетесь к локальной базе <b>localhost:5432</b> не меняйте
- вместо <b>db_name</b> вставьте имя базы

### <em>Команды для установки:</em> 
- драйвер для <b>PostgreSQL</b> <kbd> pip install psycopg2-binary </kbd>
- <b>Flask</b> <kbd> pip install flask </kbd>
- <b>SQLAlchemy</b>  <kbd> pip install sqlalchemy </kbd>
---
- для <b>всего сразу</b>  <kbd>pip install flask sqlalchemy psycopg2-binary</kbd>





