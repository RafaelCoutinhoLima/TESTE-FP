import funções
import os
os.system('cls')

funções.carregar_treinos()
while True:
    funções.menu_principal()
    try:
        escolha = int(input('\nDigite o que você deseja fazer (1-10): '))
        if escolha < 1 or escolha > 10:
            print('\nEscolha inválida! Digite um número de 1 a 10.')
            continue
    except ValueError:
        print('\nDigite um número válido (1-10)')
        continue
    
    if escolha == 1:
        funções.criar_treino()
    elif escolha == 2:
        funções.excluir_treino()
    elif escolha == 3:
        funções.visualizar_treino()
    elif escolha == 4:
        funções.editar_treino()
    elif escolha == 5:
        funções.filtrar_treino()
    elif escolha == 6:
        funções.criar_meta()
    elif escolha == 7:
        funções.visualizar_metas()
    elif escolha == 8:
        funções.sugestao_treino()
    elif escolha == 9:
        funções.analise_de_desempenho()
    elif escolha == 10:
        break



