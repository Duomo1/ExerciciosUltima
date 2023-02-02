import sqlite3
conexão = sqlite3.connect('Database')
cursor = conexão.cursor()
sql = 'CREATE TABLE TAREFAS (id INT, NOT NULL, PRIMARY KEY, AUTOINCREMENT, id_tarefa INT, NOT NULL, data NUM, NOT NULL, categoria TEXT, NOT NULL, conclusao TEXT, NOT NULL);'
cursor.execute(sql)
conexão.commit()
conexão.close()
