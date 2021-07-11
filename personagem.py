# IMPORTANDO MÓDULO PRA DEIXAR ABSTRATO ALGO
from abc import ABC
# IMPORTANDO MÓDULO PRA USAR UMA PSEUDO-INTERFACE
from abc import abstractmethod

#CLASSE ABSTRATA
class Personagens(ABC):

    # CONSTRUTOR COM OS ATRIBUTOS QUE SERÁ USADO NO JOGO
    def __init__(self, nome, elemento, vida=800, ataque=0, defesa=0):
        # ATRIBUTOS ENCAPSULADOS
        self.__nome = nome
        self.__elemento = elemento
        self.__vida = vida
        self.__ataque = ataque
        self.__defesa = defesa

    # ENCAPSULAMENTO
    # PROPRIETÁRIO
    @property
    def nome(self):
        return self.__nome
    # MODIFICADOR DE ACESSO
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    # PROPRIETÁRIO
    @property
    def elemento(self):
        return self.__elemento

    # MODIFICADOR DE ACESSO
    @elemento.setter
    def elemento(self, elemento):
        self.__elemento = elemento

    # PROPRIETÁRIO
    @property
    def vida(self):
        return self.__vida

    # MODIFICADOR DE ACESSO
    @vida.setter
    def vida(self, vida):
        self.__vida = vida

    # PROPRIETÁRIO
    @property
    def ataque(self):
        return self.__ataque

    # MODIFICADOR DE ACESSO
    @ataque.setter
    def ataque(self, ataque):
        self.__ataque = ataque

    # PROPRIETÁRIO
    @property
    def defesa(self):
        return self.__defesa

    # MODIFICADOR DE ACESSO
    @defesa.setter
    def defesa(self, defesa):
        self.__defesa = defesa

    # MÉTODO ABSTRATO (INTERFACE)
    @abstractmethod
    def Elemento(self):
        pass

    #MÉTODO ABSTRATO (INTERFACE)
    @abstractmethod
    def hab_especial(self, hab):
        pass

    #MÉTODO ABSTRATO (INTERFACE)
    @abstractmethod
    def power_up(self, alvo, jogadores):
        pass

    # MÉTODO MOSTRAR
    def mostrar(self):
        print('Nome: {}\nElemento: {}\nVida: 1000\nAtaque: 100\nDefesa: 50'.format(self.nome, self.elemento))

    # MÉTODO DELETAR
    def deletar(jogadores):
        try:
            abrir = open('nomes_salvos.txt') # CRIAR E ABRIR UM ARQUIVO TXT
            sla2 = abrir.read() # LER UM ARQUIVO TXT
            if len(sla2) != 0:
                while True:
                    try: # TRATAMENTO DE ERRO
                        sla3 = int(input('DESEJA SALVAR ALTERAÇÕES?\n1 - SIM\n2 - NÃO\n'))
                        if sla3 == 1:
                            arq = open('nomes_salvos.txt', 'w') # CRIAR E ABRIR UM ARQUIVO TXT
                            arq.close() # FECHAR UM ARQUIVO TXT
                            break
                        elif sla3 == 2:
                            return
                        else:
                            print('OPÇÃO INVÁLIDA, POR FAVOR, TENTE NOVAMENTE!')
                    except:
                        print('UTILIZE APENAS NÚMEROS!')
                        break
            arquivo = open('nomes_salvos.txt', 'w') # CRIAR UM ARQUIVO TXT
            for k in range(len(jogadores)):
                arquivo.write(f'NOME:{jogadores[k].nome}\nELEMENTO:{jogadores[k].elemento}\n\n') # ESCREVER EM UM ARQUIVO TXT
            print('°' * 80)
            print('SALVO COM SUCESSO!')

        except:
            print('ARQUIVO CORROMPIDO OU NÃO ENCONTRADO')

