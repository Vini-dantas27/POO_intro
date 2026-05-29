class Tarefa:
    tarefas = []
    def __init__(self, titulo, descricao):
        self.titulo = titulo
        self.descricao = descricao
        self.concluido = False
        Tarefa.tarefas.append(self)
    def __str__(self):
        return f"Tarefa: {self.titulo} - {self.descricao}"
    
    @classmethod
    def listar_tarefas(cls):
        for tarefa in cls.tarefas:
            print(tarefa)
        
    @classmethod        
    def obter_quantidade_tarefas(cls):
        return len(cls.tarefas)
    
tarefa01 = Tarefa("atividade 01", "ativdade com laços de repetição")
tarefa02 = Tarefa("atividade de Poo", "revendo POO em Python")
          
quantidade = Tarefa.obter_quantidade_tarefas()
print(f"Você tem {quantidade} tarefas.")

Tarefa.listar_tarefas()
  
class Pessoa:
    def __init__(self, nome, idade, profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao
    def __str__(self):
        return f"Nome: {self.nome} - Idade {self.idade} - Profissão {self.profissao}"
    
    def aniversario(self):
        self.idade += 1
        return self.idade
    
pessoa1 = Pessoa("Lucas", 18)
print(f"Sua idade atual: {pessoa1.idade}")

pessoa1.aniversario()
print(f"Idade após o aniversário: {pessoa1.idade}")