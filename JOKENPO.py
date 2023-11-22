import random 

opcoes = ['pedra', 'papel', 'tesoura']

computador = random.choice(opcoes)

escolhaDoUsuario = input('Digite sua jogada (pedra papel ou tesoura): ')

if escolhaDoUsuario != 'pedra' and escolhaDoUsuario != 'papel' and escolhaDoUsuario != 'tesoura':
    print('ESCOLHA INVÁLIDA!')
elif escolhaDoUsuario == computador:
    print(f'O computador escolheu {computador} ----> EMPATE')
elif escolhaDoUsuario == 'pedra' and computador == 'papel':
    print(f'O computador escolheu {computador} ----> PC WINS')
elif escolhaDoUsuario == 'papel' and computador == 'tesoura':
    print(f'O computador escolheu {computador} ----> PC WINS')
elif escolhaDoUsuario == 'tesoura' and computador == 'pedra':
    print(f'O computador escolheu {computador} ----> PC WINS')
elif escolhaDoUsuario == 'pedra' and computador == 'tesoura':
    print(f'O computador escolheu {computador} ----> YOU WIN')
elif escolhaDoUsuario == 'papel' and computador == 'pedra':
    print(f'O computador escolheu {computador} ----> YOU WIN')
elif escolhaDoUsuario == 'tesoura' and computador == 'papel':
    print(f'O computador escolheu {computador} ----> YOU WIN')
