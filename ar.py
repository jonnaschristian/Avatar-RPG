# IMPORTANDO A CLASSE PERSONAGENS
from personagem import Personagens
# IMPORTANDO MÓDULO PRO INCREMENTO ALEATÓRIO
from random import randint

# FOGO ESTÁ HERDANDO DA CLASSE PERSONAGENS (HERANÇA)
class Ar(Personagens):
# POLIMORFISMO DOS MÉTODOS
    def Elemento(self):
        self.ataque = 100
        self.defesa = 50

    # MÉTODO
    def hab(self):
        self.hab1, self.hab2 = [], []
        self.hab1.extend(('DEFESA -> Parede de Vento', randint(0, 75)))
        self.hab2.extend(('ATAQUE -> Furacão', randint(0, 75)))

    # MÉTODO HABILIDADE DA AR
    def hab_especial(self, hab):
        if hab == 1:
            self.defesa += self.hab1[1]
            return
        elif hab == 2:
            self.ataque += self.hab2[1]
            return

    # MÉTODO POWER UP DO AR
    def power_up(self, alvo, jogadores):
        print('{} DIZ: VOCÊ ESTÁ CONTRA O VENTO, NEUTRALIZAR SEU ATAQUE ATIVAR!'.format(self.nome))
        jogadores[alvo].defesa -= self.ataque
        print('{} NEUTRALIZOU O ATAQUE DO {}'.format(self.nome, jogadores[alvo].nome))

    # MÉTODO
    def mostrar(self):
        Personagens.mostrar(self)

    # MÉTODO
    def deletar(jogadores):
        Personagens.deletar(jogadores)
