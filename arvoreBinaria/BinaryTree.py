from Node import Node
from collections import deque

ROOT = "root"


# a diferença é que a árvores binária de busca os menores vão a esquerda e os maiores a direita, aqui isso não é obrigado.
class BinaryTree:

    def __init__(self, data=None, node=None):
        if node:
            self.root = node
        elif data:
            node = Node(data)
            self.root = node
        else:
            self.root = None

    #um tipo de percurso para imprimir o nó: primeiro esquerda, ele próprio , depois direita
    def inorder_traversal(self, node=ROOT):
        #se eu não passar um nó o padrão é a raiz
        if node == ROOT:
            node = self.root
        if node is None:
            return None
        #se o nó da esquerda existir
        if node.left:
            self.inorder_traversal(node.left)
        #Quando é o último printa e vai desfazendo a recursão
        print(node, end=' ')
        if node.right:
        #já aproveita a recursão
            self.inorder_traversal(node.right)

    #outro tipo de percurso, vc visita todos decendentes antes de visitar a raiz
    #olha a esquerda, olha a direita(ambos com recursão) e depois imprime, dai vem em cascata
    def postorder_traversal(self, node=ROOT):
        if node == ROOT:
            node = self.root
        if node.left:
            self.postorder_traversal(node.left)
        if node.right:
            self.postorder_traversal(node.right)
        print(node,end='')

    def levelorder_traversal(self, node=ROOT):
        if node == ROOT:
            node = self.root
        if node is None: #impresão de um árvore vazia - remoção || poda
            return None
        
        queue = deque()
        queue.append(node)
        while len(queue):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            print(node, end=' ')

    #usa-se o pos order 
    def height(self, node=ROOT):
        if node == ROOT:
            node = self.root
        hleft = 0
        hright = 0
        if node.left:
           hleft = self.height(node.left)
        if node.right:
           hright = self.height(node.right)
        if hright > hleft:
            return hright + 1
        return hleft + 1
        
    
