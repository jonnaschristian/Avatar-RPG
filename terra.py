# IMPORTANDO A CLASSE PERSONAGENS
from personagem import Personagens
# IMPORTANDO MÓDULO PRO INCREMENTO ALEATÓRIO
from random import randint

# TERRA ESTÁ HERDANDO DA CLASSE PERSONAGENS (HERANÇA)
class Terra(Personagens):
# POLIMORFISMO DOS MÉTODOS
    def Elemento(self):
        self.ataque = 100
        self.defesa = 50

    # MÉTODO
    def hab(self):
        self.hab1, self.hab2 = [], []
        self.hab1.extend(('DEFESA -> MURO DE LAMA', randint(0, 110)))
        self.hab2.extend(('ATAQUE -> TERREMOTO', randint(0, 40)))

    # MÉTODO HABILIDADE DA TERRA
    def hab_especial(self, hab):
        if hab == 1:
            self.defesa += self.hab1[1]
            return
        elif hab == 2:
            self.ataque += self.hab2[1]
            return

    # MÉTODO POWER UP DA TERRA
    def power_up(self, alvo, jogadores):
        print('{} DIZ: VOU ME DEFENDER DE SEU ATAQUE, DEFESA AUMENTAR!'.format(self.nome))
        self.defesa += self.defesa
        print('A DEFESA DO(A) {} AUMENTOU EM {}'.format(self.nome, abs(self.defesa)))

    # MÉTODO
    def mostrar(self):
        Personagens.mostrar(self)

    # MÉTODO
    def deletar(jogadores):
        Personagens.deletar(jogadores)
