from aluno import Aluno

class Escola:
    def __init__(self, nome: str, endereco: str):
        self.nome = nome
        self.endereco = endereco
        self.alunos = [Aluno('Jonas', 18, 'Python', 10)]
    
    def cadastrarAluno(self, aluno: Aluno):
        self.alunos.append(aluno)

    def editarAluno(self, aluno: Aluno):
        for a in self.alunos:
            if str(a.matricula) == str(aluno.matricula):
                a.nome = aluno.nome
                a.idade = aluno.idade
                a.curso = aluno.curso
                a.nota = aluno.nota
                return True
        return False
    
    def deletarAluno(self, matricula: str):
        for aluno in self.alunos:
            if str(aluno.matricula) == str(matricula):
                self.alunos.remove(aluno)
                return True
        return False
    
    def listarAlunos(self):
        return self.alunos

if __name__ == "__main__":
    escola = Escola('Infinity school', 'Av santos dumont')
    aluno = Aluno('Mariana', 23, 'Python', 10)
    escola.cadastrarAluno(aluno)
    print(escola.listarAlunos())
    aluno.nome = 'Mariana Oliveira'
    escola.editarAluno(aluno)
    print(escola.listarAlunos())
    escola.deletarAluno(aluno.matricula)
    print(escola.listarAlunos()) 