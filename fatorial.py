## Cálculo de Fatorial
def fatorial(n):
    # Caso base: se n for 0 ou 1, o fatorial é 1
    if n == 0 or n == 1:
        return 1
    # Caso recursivo: n! = n * (n-1)!
    else:
        return n * fatorial(n - 1)
    
#Exemplo de uso
numero = 3
resultado = fatorial(numero)
print(f"O fatorial de {numero} é {resultado}")