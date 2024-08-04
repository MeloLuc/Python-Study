from BinaryTree import BinaryTree
from Node import Node
from BinarySearchTree import BinarySearchTree
import random

def inorder_traversal():
    #um tipo de percurso para imprimir o nó: primeiro esquerda, ele próprio , depois direita
    tree = BinaryTree()
    n1 = Node('a')
    n2 = Node('+')
    n3 = Node('*')
    n4 = Node('b')
    n5 = Node('-')
    n6 = Node('/')
    n7 = Node('c')
    n8 = Node('d')
    n9 = Node('e')

    tree.root = n2
    n2.right = n3
    n2.left = n1
    n3.right = n5
    n3.left = n4
    n5.right = n9
    n5.left = n6
    n6.right = n8
    n6.left = n7

    print('Percurso inorder:', end=" ")
    tree.inorder_traversal()
    print('')

def posOrderTraversal():
    tree = BinaryTree()
    n1 = Node('S')
    n2 = Node('A')
    n3 = Node('C')
    n4 = Node('U')
    n5 = Node('L')

    tree.root = n1
    n1.right = n2
    n1.left = n3
    n3.right = n4
    n3.left = n5

    print('Percurso post order:', end=" ")
    tree.postorder_traversal()
    print('')

def level_traversal():
    values = [61, 89, 66, 43, 51, 16, 55, 11, 79, 77, 82, 32]

    bst = BinarySearchTree()

    for v in values:
        bst.insert(v)

    print('Percurso in level:', end=" ")
    #61 43 89 16  51 66 11 32 55 79 82
    bst.levelorder_traversal()
    print('')

def altura():
    tree = BinaryTree()
    n1 = Node('S')
    n2 = Node('A')
    n3 = Node('C')
    n4 = Node('U')
    n5 = Node('L')

    tree.root = n1
    n1.right = n2
    n1.left = n3
    n3.right = n4
    n3.left = n5
    print(tree.height())
    
def inserir():
    random.seed(77)

    values = random.sample(range(1, 1000), 42)

    bst = BinarySearchTree()
    for v in values:
        bst.insert(v)

    #conhecido com simetrico ele retorna os numeros em forma crescente
    print('Percurso inorder:', end=" ")
    bst.inorder_traversal()
    print('')
    return bst

def busca():
    #como a arvore vai ser aleatoria pode ser que não encontre nenhum elemento de 'items' na árvore.
    bst = inserir()

    items = [1, 3, 435, 100, 1000]
    for item in items:
        r = bst.search(item)
        if r is None:
            print(item , "não encontrado")
        else:
            print(r.root.data, "encontrado")

def max_min():
    bst = inserir()
    print("----")
    print("Máximo: ", bst.max())
    print("Mínimo: ", bst.min())
    
def remocao():

    #CRIANDO A ÁRVORE
    bst = BinarySearchTree()
    values = [61, 89, 66, 43, 51, 16, 55, 11, 79, 77, 82, 32, 100, 90]
    for v in values:
        bst.insert(v)

    #IMPRIMINDO A ÁRVORE
    #remove_value = 1000 #valor inexistente
    #remove_value = 11 #CASO SEM FILHO
    #remove_value = 66 #CASO 1 FILHO
    remove_value = 61 #CASO 2 FILHO

    print(f"-- Antes de remover {remove_value} --")
    print('Percurso inorder:', end=" ")
    bst.inorder_traversal()
    print('')
    print('Percurso in level:', end=" ")
    bst.levelorder_traversal()

    print('')
    print('')

    bst.remove(remove_value)
    print(f"-- Após remover {remove_value} --")
    print('Percurso inorder:', end=" ")
    bst.inorder_traversal()
    print('')
    print('Percurso in level:', end=" ")
    bst.levelorder_traversal()

def poda():

    #CRIANDO A ÁRVORE
    bst = BinarySearchTree()
    values = [20, 10, 30, 5, 15, 40, 25, 1, 35, 45]
    for v in values:
        bst.insert(v)

    prune_value = 10 #poda sub-árvore esquerda
    #prune_value = 100 #valor inexistente
    #prune_value = 20 #árvore fica vazia
    #prune_value = 30 #poda sub-árvore direita
    #prune_value = 1 #poda folha

    print(f"-- Antes de podar {prune_value} --")
    print('Percurso inorder:', end=" ")
    bst.inorder_traversal()
    print('')
    print('Percurso in level:', end=" ")
    bst.levelorder_traversal()

    print('')
    print('')

    bst.prune(prune_value)
    print(f"-- Após podar {prune_value} --")
    print('Percurso inorder:', end=" ")
    bst.inorder_traversal()
    print('')
    print('Percurso in level:', end=" ")
    bst.levelorder_traversal()


# --- TESTES DOS METODOS DA ÁRVORE BINARIA DE BUSCA --

#inorder_traversal()
#posOrderTraversal()
#level_traversal()
#altura()
#inserir()
#busca()
#max_min()
remocao()
poda()