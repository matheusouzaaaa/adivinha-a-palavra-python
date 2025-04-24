import json
import random

# Cores para ficar mais bonitinho
cor_padrao = '\033[0;0m'
fundo_preto = '\033[40m'     
fundo_amarelo = '\033[43m'  
fundo_verde = '\033[42m'
fundo_vermelho = '\033[41m'     

#array (no python acho que é tupla) com as palavras para se adivinhar (legal seria depois criar um json, ou procurar algum json, que disponibilize palavras com 5 letras).
with open("5-letter-words.json") as file:
    possiveis_palavras = json.load(file)
# possiveis_palavras = ["grama","trave","gamer","mouse","bolas"]

#to colocando tudo em maiusculo, pq acho que fica mais bonito que tudo pequeno (preferencia pessoal)
palavra_sorteada = random.choice(possiveis_palavras).upper()

fim_de_jogo = False
tentativas = 10

while not fim_de_jogo:
    # crio um array (tupla) e nele vou colocar todas as letras do chute
    retorno = []

    #escolha do usuario
    chute = str(input("Digite uma palavra com 5 letras: "))

    # funcao que pega o que o usuário escreveu, e já limpa o excedente de 5 caracteres. (se ele escreveu futebol, só vai ser contabilizado FUTEB)
    chute = chute.upper()[:5]

    #já desconto uma tentativa do usuário
    tentativas -= 1

    #se acabaram as tentativas, mostra a mensagem.
    if tentativas == 0:
        print("Ah que pena, você é péssimo nesse jogo :/")
        print("\n")
        print("A palavra era:", fundo_vermelho + palavra_sorteada + cor_padrao)
        fim_de_jogo = True
                                  
    # se acertou o chute com a palavra sorteada eu coloco o fundo verde em toda o chute realizado e volto pra cor padrão (acho que n precisava, mas é uma boa prática)
    elif chute == palavra_sorteada:
        print("Parabéns, você é bom demais! :)")
        print(fundo_verde + chute + cor_padrao)
        fim_de_jogo = True

    # se tem tentativas e ainda não acertou qual é a palavra, entra aqui
    else:
        i = 0
        for c in chute:
            # coloco a primeira letra do chute na posição zero do array retorno (retorno[0], depois retorno[1], retorno[2]....)
            retorno.append(c)

            # verifico se esse caracter (retorno[0].. retorno[1]... retorno[2]) não está na palavra (significa que ele errou tudo.. letra e posicionamento)
            if c not in palavra_sorteada:
                # substituo a primeira letra da palavra pela mesmo letra só que "formatada bonitinha"
                retorno[i] = fundo_preto + retorno[i] + cor_padrao

            # se ele passou pelo if de cima, é um bom sinal. quer dizer que existe a letra na frase.. agora basta ver se tá no lugar certo, ou não
            elif retorno[i] == palavra_sorteada[i]:
                # verifica se a letra (retorno[0].. retorno[1]) está na mesma posição da palavra que foi sorteada (palavra_sorteada[0].. palavra_sorteada[1])
                
                # se entrar aqui, é pq a letra está no lugar certo. então substituo ela por ela mesmo, com o fundo verde
                retorno[i] = retorno[i] = fundo_verde + retorno[i] + cor_padrao

            # se entrar aqui embaixo, é pq acertou a letra, mas nao acertou a posição
            else:
                # entao eu substituo a letra por ela mesmo, com o fundo amarelo
                retorno[i] = retorno[i] = fundo_amarelo + retorno[i] + cor_padrao

            # vai para a proxima letra
            i += 1


        for c in retorno:
            #mostra na tela o chute com as formatações (fundo preto, fundo verde ou fundo amarelo)
            print(c, end='')

        #quebra de linha só.
        print("\n")

if(fim_de_jogo==True):
    print('Boa sorte na próxima tentativa')
