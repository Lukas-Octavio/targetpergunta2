# Caso deseje inserir um valor, retirar o comentário da linha 2 e comentar a linha 3
# valor = int(input("Insira um valor para checar se ele existe na sequência de Fibonacci: "))
valor = 89
fibonacci = [0, 1]

for i in range(1, 1000):
    fibonacci.append(fibonacci[(i - 1)] + fibonacci[(i)])
    if fibonacci[i] == valor:
        print(f"Este valor existe na sequência! Sua posição é: {i + 1}")
        break
    elif valor == 0:
        print("Este valor existe na sequência! Sua posição é: 1")
        break
    elif i == 999:
        print("Este valor não existe na sequência de Fibonacci")
