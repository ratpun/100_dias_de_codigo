n = int(input("Digite o número: "))

def fatorial(n):
   if n == 0 or n == 1:
        return 1
   else:
        return n * fatorial(n - 1)
 	
resultado = fatorial(n)
print("O fatorial é: ", resultado)
