# IMPORTANDO CLASSES USADAS EM OUTROS ARQUIVOS FONTE E METODOS DE BIBLIOTECAS DO PYTHON
from time import sleep
from agua import Agua
from fogo import Fogo
from ar import Ar
from terra import Terra
from random import randint
from salvar import Salvar
from personagem import Personagens


# FUNÇÃO PRA PRINTAR OS NEGÓCIO PRA ORGANIZAR PRO USUÁRIO
def linha():
    print('º' * 80)


linha()
print('SEJA BEM VINDO(A) AO JOGO AVATAR!')
linha()
jogadores = []

while True:
    try:  # TRATAMENTO DE ERRO
        operacao = int(input(
            'QUE OPERAÇÃO DESEJA FAZER?\n1 - JOGAR\n2 - CRIAR PERSONAGENS\n3 - EDITAR PERSONAGENS\n4 - MOSTRAR PERSONAGENS\n5 - DELETAR PERSONAGENS\n6 - SALVAR\n7 - CARREGAR\n8 - SAIR DO JOGO\n'))

        # JOGAR
        if operacao == 1:

            # VAI INICIAR O JOGO
            while True:

                # TRATAMENTO DE ERRO
                try:
                    if n_jogadores == 1:
                        linha()
                        print('QUANTIDADE DE JOGADORES INSUFICIENTES')
                        linha()
                        break

                    # DECLARA O VENCEDOR
                    if len(jogadores) == 1:
                        linha()
                        print('TEMOS UM VENCEDOR :D -> {}'.format(jogadores[0].nome))
                        sleep(2)
                        linha()
                        # SALVA O JOGO
                        linha()
                        salvar_jogo = int(input('VOCÊ QUER SALVAR O JOGO?\n1 - SIM\n2 - NÃO\n'))
                        if salvar_jogo == 1:
                            Salvar.salvar(jogadores)
                            linha()
                        break

                    # SORTEIO DOS JOGADORES
                    j1 = randint(0, len(jogadores) - 1)
                    j2 = randint(0, len(jogadores) - 1)
                    if j1 == j2:
                        if (j2 + 1) == len(jogadores) == (j1 + 1):
                            j2 -= 1
                        else:
                            j2 += 1
                    linha()
                    print('JOGADOR 1 ESCOLHIDO:\n - {}'.format(jogadores[j1].nome))
                    print()
                    print('JOGADOR 2 ESCOLHIDO:\n - {}'.format(jogadores[j2].nome))
                    linha()
                    sleep(2)
                    rodada = 0

                    # INICIA A BATALHA
                    while True:

                        # TRATAMENTO DE ERRO
                        try:
                            rodada += 1

                            # DA O GAME OVER PRO JOGADOR 1 SE ELE MORRER
                            if jogadores[j1].vida <= 0:
                                print('GAME OVER PARA: {}'.format(jogadores[j1].nome))
                                sleep(1.5)
                                jogadores[j2].vida = 1000
                                jogadores[j2].ataque = 100
                                jogadores[j2].defesa = 50
                                del jogadores[j1]
                                break

                            while True:

                                # TRATAMENTO DE ERRO
                                try:

                                    # DECIDE SE O JOGADOR 1, NA RODADA 3 OU A CADA 3, QUER USAR O POWER UP
                                    if rodada % 3 == 0:
                                        hab = int(input(
                                            'DESEJA UTILIZAR SUA HAB ESPECIAL (POWER UP) JOGADOR 1?\n1 - Sim\n2 - Nao\n'))
                                        linha()
                                        if hab == 1:
                                            jogadores[j1].power_up(j2, jogadores)
                                            linha()
                                            break
                                        elif hab == 2:
                                            pass

                                    # DECIDE QUAL HABILIDADE O JOGADOR 1 VAI ESCOLHER (DEFESA OU ATAQUE)
                                    hab = int(input(
                                        'DESEJA UTILIZAR QUAL HABILIDADE JOGADOR 1?:\n1 - {}\n2 - {}\n'.format(
                                            jogadores[j1].hab1[0], jogadores[j1].hab2[0])))
                                    linha()
                                    if hab == 1 or hab == 2:
                                        jogadores[j1].hab_especial(hab)
                                        jogadores[j2].vida -= jogadores[j1].ataque - jogadores[j2].defesa
                                        if jogadores[j2].vida <= 0:
                                            break
                                        else:
                                            print('A VIDA DO JOGADOR {} é: {}'.format(jogadores[j2].nome,
                                                                                      jogadores[j2].vida))
                                            linha()
                                        break
                                    else:
                                        print('OPÇÃO INVÁLIDA\n')
                                        linha()
                                except:
                                    linha()
                                    print('OCORREU UM ERRO INESPERADO, POR FAVOR TENTE NOVAMENTE!')
                                    break

                            # DA O GAME OVER PRO JOGADOR 2 SE ELE MORRER
                            if jogadores[j2].vida <= 0:
                                print('GAME OVER PARA: {}'.format(jogadores[j2].nome))
                                sleep(1.5)
                                jogadores[j1].vida = 1000
                                jogadores[j1].ataque = 100
                                jogadores[j1].defesa = 50
                                del jogadores[j2]
                                break

                            while True:

                                # TRATAMENTO DE ERRO
                                try:

                                    # DECIDE SE O JOGADOR 2, NA RODADA 3 OU A CADA 3, QUER USAR O POWER UP
                                    if rodada % 3 == 0:
                                        hab = int(input(
                                            'DESEJA UTILIZAR SUA HAB ESPECIAL (POWER UP) JOGADOR 2?:\n1 - SIM\n2 - NÃO\n'))
                                        linha()
                                        if hab == 1:
                                            jogadores[j2].power_up(j1, jogadores)
                                            linha()
                                            break
                                        elif hab == 2:
                                            pass

                                    # DECIDE QUAL HABILIDADE O JOGADOR 2 VAI ESCOLHER (DEFESA OU ATAQUE)
                                    hab = int(
                                        input('DESEJA UTILIZAR QUAL HABILIDADE JOGADOR 2?\n1 - {}\n2 - {}\n'.format(
                                            jogadores[j2].hab1[0], jogadores[j2].hab2[0])))
                                    linha()
                                    if hab == 1 or hab == 2:
                                        jogadores[j2].hab_especial(hab)
                                        jogadores[j1].vida -= jogadores[j2].ataque - jogadores[j1].defesa
                                        if jogadores[j1].vida <= 0:
                                            break
                                        else:
                                            print('A VIDA DO JOGADOR {} é: {}'.format(jogadores[j1].nome,
                                                                                      jogadores[j1].vida))
                                            linha()
                                        break
                                    else:
                                        print('OPÇÃO INVÁLIDA\n')
                                        linha()
                                except:
                                    linha()
                                    print('OCORREU UM ERRO INESPERADO, POR FAVOR TENTE NOVAMENTE!')
                                    break
                        except:
                            linha()
                            print('OCORREU UM ERRO INESPERADO, POR FAVOR TENTE NOVAMENTE!')
                            break
                except:
                    linha()
                    print('OCORREU UM ERRO INESPERADO, POR FAVOR TENTE NOVAMENTE!')
                    linha()
                    break

        # CRIAR PERSONAGENS
        elif operacao == 2:
            while True:
                try:  # TRATAMENTO DE ERRO
                    linha()
                    n_jogadores = int(input('DIGITE A QUANTIDADE DE PERSONAGENS QUE VOCÊ DESEJA CRIAR:\n'))
                    linha()
                    for i in range(n_jogadores):

                        # O USUÁRIO ESCOLHE O NOME E O ELEMENTO QUE ELE QUER PRO PERSONAGEM DELE
                        nome = str(input('DÊ UM NOME AO PERSONAGEM {}:\n'.format(i + 1))).upper()

                        while True:
                            try:  # TRATAMENTO DE ERRO
                                elemento = input(
                                    'QUAL ELEMENTO VOCÊ GOSTARIA DE DAR AO SEU PERSONAGEM {}?\nAGUA, FOGO, AR OU TERRA:\n'.format(
                                        i + 1)).upper()
                                if elemento == 'AGUA':
                                    jogadores.append(Agua(nome, elemento))
                                    jogadores[i].Elemento()
                                    jogadores[i].hab()
                                    break
                                elif elemento == 'FOGO':
                                    jogadores.append(Fogo(nome, elemento))
                                    jogadores[i].Elemento()
                                    jogadores[i].hab()
                                    break
                                elif elemento == 'AR':
                                    jogadores.append(Ar(nome, elemento))
                                    jogadores[i].Elemento()
                                    jogadores[i].hab()
                                    break
                                elif elemento == 'TERRA':
                                    jogadores.append(Terra(nome, elemento))
                                    jogadores[i].Elemento()
                                    jogadores[i].hab()
                                    break
                                else:
                                    linha()
                                    print('ELEMENTO FORA DO NOSSO BANCO DE DADOS, POR FAVOR, TENTE NOVAMENTE!')
                                    linha()
                                    continue
                            except:
                                linha()
                                print('ELEMENTO FORA DO NOSSO BANCO DE DADOS, POR FAVOR, TENTE NOVAMENTE!')
                                linha()
                                continue
                        linha()
                    if n_jogadores != 1:
                        print('PERSONAGENS CRIADOS!')
                        linha()
                    else:
                        print('PERSONAGEM CRIADO!')
                        linha()
                    break
                except:
                    linha()
                    print('OCORREU UM ERRO INESPERADO, POR FAVOR TENTE NOVAMENTE!')
                    break

        # EDITAR PERSONAGENS
        elif operacao == 3:
            while True:
                try:  # TRATAMENTO DE ERRO
                    linha()
                    if len(jogadores) > 0:
                        for i in range(len(jogadores)):
                            print('{:^10}'.format(i + 1))
                            jogadores[i].mostrar()
                            print()
                        linha()
                    else:
                        print('IMPOSSÍVEL EDITAR PERSONAGENS AINDA NÃO CRIADOS.')
                        linha()
                        break
                    delete = int(input('QUAL PERSONAGEM VOCE GOSTARIA DE EDITAR?\n'))
                    del jogadores[delete - 1]
                    linha()

                    nome = str(input('QUAL NOME VOCE QUER DAR A ELE(A)?\n')).upper().strip()
                    linha()
                    elemento = input(
                        'QUAL O NOVO ELEMENTO VOCÊ GOSTARIA DE DAR AO SEU PERSONAGEM?\nAGUA, FOGO, AR OU TERRA:\n').upper().strip()
                    for l in range(1):
                        if elemento == 'AGUA':
                            jogadores.append(Agua(nome, elemento))
                            jogadores[l].Elemento()
                            jogadores[l].hab()

                        elif elemento == 'FOGO':
                            jogadores.append(Fogo(nome, elemento))
                            jogadores[l].Elemento()
                            jogadores[l].hab()

                        elif elemento == 'AR':
                            jogadores.append(Ar(nome, elemento))
                            jogadores[l].Elemento()
                            jogadores[l].hab()

                        elif elemento == 'TERRA':
                            jogadores.append(Terra(nome, elemento))
                            jogadores[l].Elemento()
                            jogadores[l].hab()
                        else:
                            print()
                            print('ELEMENTO FORA DO NOSSO BANCO DE DADOS, POR FAVOR, TENTE NOVAMENTE!')
                            print()
                    linha()
                    print('PERSONAGEM EDITADO COM SUCESSO!\nSALVE O JOGO, FECHE-O, ABRA-O E CARREGUE PARA PODER JOGAR')
                    linha()
                    break
                except:
                    linha()
                    print('OCORREU UM ERRO INESPERADO, POR FAVOR TENTE NOVAMENTE!')
                    break

        # MOSTRAR PERSONAGENS
        elif operacao == 4:
            while True:
                try:
                    linha()
                    if len(jogadores) > 0:
                        for i in range(len(jogadores)):
                            print('{:^10}'.format(i + 1))
                            jogadores[i].mostrar()
                            print()
                        linha()
                        break
                    else:
                        print('IMPOSSÍVEL MOSTRAR PERSONAGENS AINDA NÃO CRIADOS.')
                        linha()
                        break
                except:
                    print('IMPOSSÍVEL MOSTRAR PERSONAGENS AINDA NÃO CRIADOS.')
                    linha()
                    break

        # DELETAR PERSONAGENS
        elif operacao == 5:
            while True:
                try:
                    linha()
                    if len(jogadores) > 0:
                        for i in range(len(jogadores)):
                            print('{:^10}'.format(i + 1))
                            jogadores[i].mostrar()
                            print()
                        linha()
                    else:
                        print('IMPOSSÍVEL DELETAR PERSONAGENS AINDA NÃO CRIADOS.')
                        linha()
                        break
                    delete = int(input('QUAL PERSONAGEM VOCE DESEJA DELETAR?\n'))
                    del jogadores[delete - 1]
                    linha()
                    print('JOGADOR SELECIONADO DELETADO!')
                    linha()
                    Personagens.deletar(jogadores)
                    linha()
                    break
                except:
                    linha()
                    print('OCORREU UM ERRO INESPERADO, POR FAVOR TENTE NOVAMENTE!')

        # SALVAR O JOGO - PERSONAGENS
        elif operacao == 6:
            while True:
                try:
                    Salvar.salvar(jogadores)
                    linha()
                    break
                except:
                    linha()
                    print('OCORREU UM ERRO INESPERADO, POR FAVOR TENTE NOVAMENTE!')
                    linha()
                    break

        # CARREGAR O JOGO - PERSONAGENS
        elif operacao == 7:
            while True:
                try:  # TRATAMENTO DE ERRO
                    linha()
                    Salvar.carregar(jogadores)
                    linha()
                    break
                except:
                    linha()
                    print('OCORREU UM ERRO INESPERADO, POR FAVOR TENTE NOVAMENTE!')

        # SAIR DO JOGO
        elif operacao == 8:
            while True:
                linha()
                print('ATÉ A PRÓXIMA!')
                linha()
                break
            break

        # CASO O USUÁRIO DIGITAR UM NÚMERO ALÉM DOS QUE TEM NO MENU
        else:
            try:  # TRATAMENTO DE ERRO
                linha()
                print('AÇÃO NÃO CONHECIDA, POR FAVOR, TENTE NOVAMENTE!')
                linha()
            except:
                linha()
                print('OCORREU UM ERRO INESPERADO, POR FAVOR TENTE NOVAMENTE!')
                break

    except:
        linha()
        print('OCORREU UM ERRO INESPERADO, POR FAVOR TENTE NOVAMENTE!')
        linha()
