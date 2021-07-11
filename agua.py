# IMPORTANDO A CLASSE PERSONAGENS
from personagem import Personagens
# IMPORTANDO MÓDULO PRO INCREMENTO ALEATÓRIO
from random import randint

# AGUA ESTÁ HERDANDO DA CLASSE PERSONAGENS (HERANÇA)
class Agua(Personagens):
# POLIMORFISMO DOS MÉTODOS
    # MÉTODO
    def Elemento(self):
        self.ataque = 100
        self.defesa = 50
    # MÉTODO
    def hab(self):
        self.hab1, self.hab2 = [], []
        # HABILIDADES DO ELEMENTO ÁGUA
        self.hab1.extend(('DEFESA -> DOMO DE ÁGUA', randint(0, 50)))
        self.hab2.extend(('ATAQUE -> MAREMOTO', randint(0, 100)))
    # MÉTODO HABILIDADE DA ÁGUA
    def hab_especial(self, hab):
        if hab == 1:
            self.defesa += self.hab1[1]
            return
        elif hab == 2:
            self.ataque += self.hab2[1]

            return
    # MÉTODO POWER UP DA ÁGUA
    def power_up(self, alvo, jogadores):
        print('{} DIZ: VOU ME PURIFICAR, SUGANDO ENERGIA DO SEU ATAQUE PARA AUMENTAR MINHA VIDA ATIVAR!'.format(self.nome))
        self.vida += jogadores[alvo].ataque
        print('A VIDA DO JOGADOR {} AGORA É {}'.format(self.nome, self.vida))
    # MÉTODO
    def mostrar(self):
        Personagens.mostrar(self)

    # MÉTODO
    def deletar(jogadores):
        Personagens.deletar(jogadores)
