
def funcao(x):
    return x - (2**-x)

def calcularZero(a, b, tol):
    #teorema de Bolzano
    if(funcao(a)*funcao(b) < 0):

        while(True): #-> os "return" quebram o laço while quando estiver dentro da tolerancia escolhida
            refinamento = (a + b) / 2
            refinamento_aplicado = funcao(refinamento)

            #verifica se em algum dos eixos o refinamento provocou um resultado dentro do
            #intervalo de tolerancia
            tolY = abs(refinamento_aplicado) < tol #numero absoluto - modulo
            tolX = ((b - a) / 2) < tol

            #programação defensiva
            if(refinamento_aplicado == 0 or tolY or tolX):
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


#intervalo inicial
a = 0  #intervalo da esquerda
b = 2  #intervalo da direita

a = int(input("Digite o intervalo esquerdo:"))
b = int(input("Digite o intervalo direito:"))

#precisão
tol = 0.01

tol = float(input("Digite a tolerancia de erro desejada: "))

#resultado
x = calcularZero(a, b, tol)
print(x)

