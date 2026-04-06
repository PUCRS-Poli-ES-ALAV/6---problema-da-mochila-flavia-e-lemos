def problema_mochila(capacidade, pesos, valores):
    num_produtos = len(pesos)

    maxTab = [[0 for _ in range (capacidade + 1)] for _ in range(num_produtos + 1)] 


    for i in range (1, num_produtos +1 ):
        for j in range (1, capacidade + 1):

            peso_item_atual = pesos[i-1]
            valor_item_atual = valores [i-1]
            if peso_item_atual <= j:
                maxTab[i][j] = max(maxTab[i-1][j], valor_item_atual + maxTab[i-1][j-peso_item_atual])
            else:
                maxTab[i][j] = maxTab[i-1][j]
    
    return maxTab[num_produtos][capacidade]

valores_ex = [60, 100, 120]
pesos_ex = [10, 20, 30]
capacidade_ex = 50

resultado = problema_mochila(capacidade_ex, pesos_ex, valores_ex)
print(f"O valor máximo do exemplo: {resultado}")

valores_aula = [2, 4, 2, 3]
pesos_aula = [5, 2, 2, 1]
capacidade_aula = 7

resultado_aula = problema_mochila(capacidade_aula, pesos_aula, valores_aula)
print(f"O valor máximo da aula: {resultado_aula}")