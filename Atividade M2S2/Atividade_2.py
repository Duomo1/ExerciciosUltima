import sqlite3
conexão = sqlite3.connect('Database')
cursor = conexão.cursor()
sql = 'CREATE TABLE EVENTOS (ID INT, PRIMARY KEY, AUTOINCREMENT, Titulo TEXT, data NUM, Local_evento TEXT, Organizador_responsavel TEXT(50), CONSTRAINT EVENTOS_PK PRIMARY KEY (Organizador_responsavel));'

'CREATE TABLE Organizadores (ID INT, PRIMARY KEY, AUTOINCREMENT, nome_organizador TEXT(50), email_organizador TEXT, CPF_organizador NUM, CONSTRAINT Organizadores_FK FOREIGN KEY (nome_organizador) REFERENCES EVENTOS(Organizador_responsavel));'

cursor.execute(sql)
conexão.commit()
conexão.close()
