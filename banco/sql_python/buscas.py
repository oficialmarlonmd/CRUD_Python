import mysql.connector
import os

class DB:
    def __init__(self):
        self.connection = self.create_connection()
        self.cursor = self.connection.cursor()

    @staticmethod
    def create_connection():
        return mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='',
            database='senac'
        )
    
    def questao1(self):
        comando = f'SELECT * FROM senac.alunos'
        self.cursor.execute(comando)
        resultado = self.cursor.fetchall()
        print(resultado)

    def questao2(self):
        comando = f"select count(*)  as nascidos_Brasil  from alunos where nacionalidade = 'Brasil'"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchall()
        print(resultado)
    
    def questao3(self):
        comando = f"select nome, profissao, nascimento from alunos"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchall()
        print(resultado)

    def questao4(self):
        comando = f"select nome, nacionalidade from alunos where nacionalidade like 'Irlanda' or nacionalidade like 'Moçambique'"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchall()
        print(resultado)

    def questao5(self):
        comando = f"select nome, sexo, altura,peso from alunos where nacionalidade like 'Brasil' and peso >= 75"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchall()
        print(resultado)
    
    def questao6(self):
        comando = f"select nome, nacionalidade from alunos where nacionalidade = 'Brasil'"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchall()
        print(resultado)    

    def questao7(self):
        comando = f"select a.nome, a.profissao, a.nascimento, a.sexo, a.peso, a.altura, a.nacionalidade, a.curso_preferido, c.nome, c.descricao, c.carga, c.totaulas, c.ano from alunos a join cursos c on a.curso_preferido = c.idcurso where a.nome like '%SILVA%'"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchall()
        print(resultado)

    def questao8(self):
        comando = f"select a.nome, a.curso_preferido, c.nome from alunos a join cursos c on a.curso_preferido = c.idcurso where c.nome like 'JAVA'"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchall()
        print(resultado)

    def questao9(self):
        comando = f"select a.nome, a.curso_preferido, c.nome from alunos a join cursos c on a.curso_preferido = c.idcurso where c.nome like 'HTML5' or c.nome like 'PHP' or c.nome like 'Word'"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchall()
        print(resultado)

    def questao10(self):
        comando = f"select a.nome, a.curso_preferido, c.nome from alunos a join cursos c on a.curso_preferido = c.idcurso where c.nome like 'MySQL'"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchall()
        print(resultado)

    def questão11(self):
        comando = f"select a.nome, a.curso_preferido, c.nome, c.carga from alunos a join cursos c on a.curso_preferido = c.idcurso where c.carga >= 30"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchall()
        print(resultado)

    def questao12(self):
        comando = f"select a.nome, a.nacionalidade, c.totaulas, c.nome from alunos a join cursos c on a.curso_preferido = c.idcurso where a.nacionalidade like 'Brasil' and c.nome like 'Premiere'  or a.nacionalidade like 'Brasil' and c.nome like'After Effects' order by a.nome asc"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchall()
        print(resultado)

    def questao13(self):
        comando = f"select a.nome, a.profissao, a.nascimento, a.sexo, a.peso, a.altura, a.nacionalidade, a.curso_preferido, c.nome, c.descricao, c.carga, c.totaulas, c.ano from alunos a join cursos c on a.curso_preferido = c.idcurso order by c.nome asc"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchall()
        print(resultado)
    
    def questao14(self):
        comando = f"select a.nome, a.curso_preferido, c.nome, c.carga from alunos a join cursos c on a.curso_preferido = c.idcurso order by c.carga asc, a.nome desc"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchall()
        print(resultado)

    def questao15(self):
        comando = f'select a.nome, a.curso_preferido, c.nome from alunos a join cursos c on a.curso_preferido = c.idcurso where a.curso_preferido != 5 and a.curso_preferido != 17 and a.curso_preferido != 25'
        self.cursor.execute(comando)
        resultado = self.cursor.fetchall()
        print(resultado)

    def questao16(self):
        comando = f"select a.nome, c.nome, c.descricao from alunos a join cursos c on a.curso_preferido = c.idcurso order by a.nome asc"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchall()
        print(resultado)

    def questao17(self):
        comando = f"select c.nome, c.carga from cursos c where c.carga between '20' and '30'"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchall()
        print(resultado)

    def questao18(self):
        comando = f"select a.nome, c.nome, c.descricao, c.ano from alunos a join cursos c on a.curso_preferido = c.idcurso where a.nome like '%LUIZ%'"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchall()
        print(resultado)
    
    def questao19(self):
        comando = f"select nome, nascimento from alunos a where nascimento between '1999-01-01' and '2005-12-31'"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchall()
        print(resultado)




a = DB()
a.questao12()

