from BinaryTree import BinaryTree
from Node import Node

ROOT = "root"

class BinarySearchTree(BinaryTree):

    def insert(self, value):
        parent = None
        x = self.root

        while(x):
            parent = x
            if(value < x.data):
                x = x.left
            else:
                x = x .right

        if parent is None:
            self.root = Node(value)
        elif(value < parent.data):
            parent.left = Node(value)
        else:
            parent.right = Node(value)

    def search(self, value, node=ROOT):
        if node == ROOT:
            node = self.root
        if node is None:
            return None
        if node.data == value:
            return BinarySearchTree(node)
        if value < node.data:
           return self.search(value, node.left)
        return self.search(value, node.right)
    
    
    def min(self, node=ROOT): #eu posso querer procurar um mínimo que não seja em relação a raiz da árvore.
        if node == ROOT:
            node = self.root
        if node is None:
            return None
        while node.left:
            node = node.left
        return node.data
    
    def max(self , node=ROOT):
        if node == ROOT:
            node = self.root
        if node is None:
            return None
        while node.right:
            node = node.right
        return node.data
    
    def remove(self, value, node=ROOT):
        if node == ROOT:
            node = self.root

        if node is None: #caso base da recursão
            print("ERRO NA REMOÇÃO: Valor informado não encontrado")
            return node
        
        if value < node.data:
            node.left = self.remove(value, node.left)
        elif value > node.data:
            node.right = self.remove(value, node.right)
        else:
            #cai nos tres casos para remoção

            # caso sem filho
            #if node.left is None and node.right is None:
               # return None
            
            # caso com 1 filho / caso sem filho -> left= none pode ser que left= none and right = none, se right for none tb, já retorna none
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            
            # caso com 2 filhos
            substitute = self.min(node.right)
            node.data = substitute
            node.right = self.remove(substitute, node.right)

        return node #caso não ache retorna o nó pro mesmo lugar(left, right) 
    
    
    def prune(self, value): #restringindo para sempre começar com a raiz                                                                                                                                                                                                                                                    
        self._prune(value, self.root)
        
    
    def _prune(self, value, node):

        if node is None:
            print("ERRO NA PODA: Valor informado não encontrado") #LEMBRE QUE NÃO É BOM ESCREVER EM MÉTODOS (generalizar x especializar)
            return None
            
        if value < node.data:
            node.left = self._prune(value, node.left)
        if value > node.data:
            node.right = self._prune(value, node.right)

        if(node.data == value):
            if node == self.root:
                self.root = None
            return None
        else:
            return node

            

