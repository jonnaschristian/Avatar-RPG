# IMPORTANDO A CLASSE PERSONAGENS
from personagem import Personagens
# IMPORTANDO MÓDULO PRO INCREMENTO ALEATÓRIO
from random import randint
# FOGO ESTÁ HERDANDO DA CLASSE PERSONAGENS (HERANÇA)
class Fogo(Personagens):
# POLIMORFISMO DOS MÉTODOS
    # MÉTODO
    def Elemento(self):
        self.ataque = 100
        self.defesa = 50

    # MÉTODO
    def hab(self):
        self.hab1, self.hab2 = [], []
        self.hab1.extend(('DEFESA -> ESCUDO FLAMEJANTE', randint(0, 40)))
        self.hab2.extend(('ATAQUE -> BOLAS DE FOGO', randint(0, 110)))

    # MÉTODO HABILIDADE DA FOGO
    def hab_especial(self, hab):
        if hab == 1:
            self.defesa += self.hab1[1]
            return
        elif hab == 2:
            self.ataque += self.hab2[1]
            return
    # MÉTODO POWER UP DO FOGO
    def power_up(self, alvo, jogadores):
        print('{} DIZ: VOU TE TRANSFORMAR EM CINZAS, BOLAS DE FOGO X2 ATIVAR!'.format(self.nome))
        jogadores[alvo].vida -= (self.ataque + self.ataque) - jogadores[alvo].defesa
        print('A VIDA DO JOGADOR {} é: {}'.format(jogadores[alvo].nome, jogadores[alvo].vida))

    # MÉTODO
    def mostrar(self):
        Personagens.mostrar(self)

    # MÉTODO
    def deletar(jogadores):
        Personagens.deletar(jogadores)
