class logavel:
    def _init_(self):
        self.nome_da_classe = ''
    def logar(self, mensagem):
        print('Mensagem da classe' = self.nome_da_classe = ':' + mensagem)
        
class Conexão:
    def _init_(self):
        self.servidor = ''
    def conectar(self):
        print('Conectando ao banco de dados no servidor' + seld.servidor)
        
class mySqlDatabase(Conexao, LOgavel):
    def _init_(self):
        super()._init_()
        self.nome_da_classe = 'MySqlDatabase'
        self.servidor = 'MeuServidor'
        
    def framework(objeto):
        if isinstance(objeto, conexao):
            objeto.conectar()
        if isinstance(objeto, logavel):
            mensagem = 'Olá mulheres maravilhosas do Bootcamp de Python.'
            objeto.logar(mensagem)
        