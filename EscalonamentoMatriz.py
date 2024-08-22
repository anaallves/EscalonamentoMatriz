import numpy as np

def usuario():
    matriz = []
# O usuário irá inserir a quantidade de linhas e colunas ---------------------------------------------------------
    linhas = int(input("Digite a quantidade de linhas: "))
    colunas = int(input("Digite a quantidade de colunas: "))

    for i in range(linhas):
        matriz.append([])

# O usuário irá inserir os valores da matriz ------------------------------------------------------------------------
    for i in range(linhas):
        for j in range(colunas):
            matriz[i].append(int(input(f"Digite um valor para [{i},{j}]: ")))

# Matriz inicial ----------------------------------------------------------------------------------------------------- 
    print("Esta é sua matriz inicial:")
    print_matriz(matriz)

    return matriz

def trocar_linhas(linha_atual, pivot_linha, matriz):
    matriz[linha_atual], matriz[pivot_linha] = matriz[pivot_linha], matriz[linha_atual]

def multiplicar_linha(linha, k, matriz):
    if k == 0:
        return matriz
    for coluna in range(len(matriz[linha])):
        matriz[linha][coluna] *= k

    
def adicao_linha(linha_destino, linha_origem, k, matriz):
    for i in range(len(matriz[linha_destino])):
        matriz[linha_destino][i] += k * matriz[linha_origem][i]

    
def transformar_matriz(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])
    
    linha_atual = 0
    for coluna in range(colunas):
        if linha_atual >= linhas:
            break

# Encontrar o pivô -------------------------------------------------------------------------------------------
        pivot_linha = None
        for linha in range(linha_atual, linhas):
            if matriz[linha][coluna] != 0:
                pivot_linha = linha
                break
        
        if pivot_linha is None:
            continue
        
# A linha atual será trocada com a linha do pivô. -------------------------------------------------------------
        if pivot_linha != linha_atual:
            trocar_linhas(linha_atual, pivot_linha, matriz)
        
        
        pivot_valor = matriz[linha_atual][coluna]
        multiplicar_linha(linha_atual, 1 / pivot_valor, matriz)
        
# Os elementos abaixo do pivô serão eliminados --------------------------------------------------------------------
        for i in range(linha_atual + 1, linhas):
            if matriz[i][coluna] != 0:
                fator = -matriz[i][coluna]
                adicao_linha(i, linha_atual, fator, matriz)
        
        linha_atual += 1

# Os elementos acima do pivô serão eliminados ---------------------------------------------------------------------
    for coluna in range(colunas):
        for linha in range(linha_atual - 1, -1, -1):
            if matriz[linha][coluna] != 0:
                for i in range(linha):
                    if matriz[i][coluna] != 0:
                        fator = -matriz[i][coluna]
                        adicao_linha(i, linha, fator, matriz)
    
    return matriz

def print_matriz(matriz):
   
    print("")
    for row in matriz:
        print("| " + " | ".join(f"{str(cell).rjust(5)}" for cell in row) + " |")
    print("")

if __name__ == "__main__":
    while True:
        print("=" * 30)
        print("        Crie sua matriz!     ")
        print("=" * 30)
        matriz = usuario()

       
        transformar_matriz(matriz)
        print("Esta é sua matriz em forma escalonada:")
        print_matriz(matriz)

        print("=" * 60)

        break
