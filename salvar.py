# IMPORTANDO AS CLASSES DOS ELEMENTOS
from agua import Agua
from fogo import Fogo
from ar import Ar
from terra import Terra

# FUNÇÃO PRA ORGANIZAR PRO USUÁRIO
def linha():
    print('°' * 80)

# CLASSE SALVAR
class Salvar:
    @staticmethod # DEIXA O MÉTODO ESTÁTICO
    # MÉTODO PRA SALVAR
    def salvar(jogadores):
        try: # TRATAMENTO DE ERRO
            abrir = open('nomes_salvos.txt', 'w+') # CRIA E ABRE UM ARQUIVO TXT
            sla2 = abrir.read()  # LER UM ARQUIVO TXT
            if len(sla2) != 0:
                while True:
                    try:
                        linha()
                        sla3 = int(input('JÁ TEM UM JOGO SALVO, QUER SUBSTITUIR?\n1 - SIM\n2 - NÃO\n'))
                        if sla3 == 1:
                            arq = open('nomes_salvos.txt', 'w')
                            arq.close()
                            break
                        elif sla3 == 2:
                            return
                        else:
                            print('OPÇÃO INVÁLIDA, POR FAVOR, TENTE NOVAMENTE!')
                    except:
                        linha()
                        print('UTILIZE APENAS NÚMEROS!')
                        linha()
                        break
            arquivo = open('nomes_salvos.txt', 'w') # CRIAR E ABRIR UM ARQUIVO TXT
            for k in range(len(jogadores)):
                arquivo.write(f'NOME:{jogadores[k].nome}\nELEMENTO:{jogadores[k].elemento}\n\n')
            linha()
            print('SALVO COM SUCESSO!')
        except:
            linha()
            print('ARQUIVO CORROMPIDO OU NÃO ENCONTRADO')
            linha()

    #DEIXA O MÉTODO ESTÁTICO
    @staticmethod
    # MÉTODO PRA CARREGAR OS JOGADORES
    def carregar(jogadores):
        qualquer = open('nomes_salvos.txt')
        outra = qualquer.read()
        if len(outra) == 0:
            print('NENHUM PERSONAGEM ENCONTRADO PARA PODER CARREGAR')
            return
        f = open('nomes_salvos.txt') # CRIAR E ABRIR UM ARQUIVO TXT
        nome, elemento = [], []
        for linha in f:
            if linha.startswith('NOME:'):
                boi = linha.find(':')
                nome.append(linha[boi + 1:].replace('\n', ''))
            elif linha.startswith('ELEMENTO:'):
                boi = linha.find(':')
                elemento.append(linha[boi + 1:].replace('\n', ''))
        for letra in range(len(nome)):
            n = str(nome[letra])
            e = str(elemento[letra])
            if e == 'AGUA':
                jogadores.append(Agua(n, e))
                jogadores[letra].Elemento()
                jogadores[letra].hab()
            elif e == 'FOGO':
                jogadores.append(Fogo(n, e))
                jogadores[letra].Elemento()
                jogadores[letra].hab()
            elif e == 'AR':
                jogadores.append(Ar(n, e))
                jogadores[letra].Elemento()
                jogadores[letra].hab()
            elif e == 'TERRA':
                jogadores.append(Terra(n, e))
                jogadores[letra].Elemento()
                jogadores[letra].hab()
        print('CARREGADO COM SUCESSO!')
