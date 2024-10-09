
import math

#def funcao(x):
#    return x**3+x-8

def funcao(x):
    return 1-x*math.log(x)

def calcularZero(a, b, tol):
    #iterações
    i=0
    #teorema de Bolzano
    if(funcao(a)*funcao(b) < 0):
        while(True): #-> os "return" quebram o laço while quando estiver dentro da tolerancia escolhida
            refinamento = (a + b) / 2
            refinamento_aplicado = funcao(refinamento)
            i += 1

            #verifica se em algum dos eixos o refinamento provocou um resultado dentro do
            #intervalo de tolerancia
            tolY = abs(refinamento_aplicado) < tol #numero absoluto - modulo
            tolX = abs((b - a) / 2) < tol

            #programação defensiva
            if(refinamento_aplicado == 0 or tolY or tolX):
                print(f"Número de iterações: {i}")
                return refinamento
            #+++
            elif(refinamento_aplicado > 0):
                #busca saber qual extremo do intervalo é o positivo
                if funcao(b) > 0:
                    b = refinamento
                else:
                    a = refinamento
            #---
            else:
                #busca saber qual extremo do intervalo é o negativo
                if funcao(a) < 0:
                    a = refinamento
                else:
                    b = refinamento
    else:  
        return("(ERROR : Intervalo não satisfaz o teorema de bolzano)")
            

#intervalo inicial
a = float(input("Digite o intervalo esquerdo:")) #inserir decimal com ponto ex 0.5
b = float(input("Digite o intervalo direito:"))

#precisão
tol = float(input("Digite a tolerancia de erro desejada: "))

#resultado
x = calcularZero(a, b, tol)

#impressão
print(f"No intervalo [{a}, {b}] com precisão de {tol} a raiz será {x}")
