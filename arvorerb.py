PRETO = 0
VERMELHO = 1

def main():
    rbtree = ARVORE()
    rbtree.insert(7)
    rbtree.insert(6)
    rbtree.insert(5)
    rbtree.insert(4)
    rbtree.insert(3)
    rbtree.insert(2)
    rbtree.insert(1)
    rbtree.tranverse()
    if __name__ == '__main__':
        main()


class nodos(object):
	def __init__(self, cor, dados, left=None, right=None, pai=None):
		super(nodos, self).__init__()
		self.cor = cor
		self.dados = dados 
		self.left = left
		self.right = right
		self.pai = pai

	def __repr__(self):
		return str(self.dados)+str(self.cor)

class ARVORE(object):
	def __init__(self, raiz=None):
		super(ARVORE, self).__init__()
		self.raiz = raiz

	def Inserir(self, dados):
		def Arvore_Binaria(raiz, novo):
			if raiz == None:
				return novo
			elif novo.dados < raiz.dados:
				raiz.left = Arvore_Binaria(raiz.left, novo)				
				raiz.left.pai = raiz
			elif novo.data > raiz.dados:
				raiz.right = Arvore_Binaria(raiz.right, novo)
				raiz.right.pai = raiz	
			return raiz

		nodo = nodos(VERMELHO, dados)
		self.raiz = Arvore_Binaria(self.raiz, nodo)
		self.ajustamentos(self.raiz, nodo)# not working

	def deletar(self, dados):
		pass

	def Rotacao_Esquerda(self, raiz, nodo):
		pass

	def Rotacao_Direita(self, raiz, nodo):
		pass

	def tranverse(self, l=[]):
		if self.raiz == None:
			return
		else:
			l.append(self.raiz)		
			while len(l) != 0:
				current_node = l.pop()
				print(current_node)
				if current_node.left is not None : l.append(current_node.left)
				if current_node.right is not None : l.append(current_node.right)

	def ajustamentos(self, raiz, nodo):
		def trocar(first, second):
			current = first
			first = second
			second = current

		while nodo is not raiz and nodo.cor is not PRETO and nodo.pai.cor is VERMELHO:
			pai = nodo.pai
			avo = nodo.pai.pai
			if pai is avo.left:
				tio = avo.right
				if tio is not None and tio.cor is VERMELHO:
					tio.cor = PRETO
					pai.cor = PRETO
					avo.cor = VERMELHO
					nodo = avo
				else:
					if nodo is pai.right:
						self.Rotacao_Esquerda(raiz, pai)
						nodo = pai
						pai = nodo.pai

					self.Rotacao_Direita(raiz, avo)
					trocar(pai.color, avo.cor)
					nodo = pai

			else:
				tio = avo.left
				if tio is not None and tio.cor is VERMELHO:
					tio.cor = PRETO
					pai.cor = PRETO
					avo.color = VERMELHO
					nodo = avo
				else:
					if nodo is pai.left:
						self.Rotacao_Direita(raiz, pai)
						nodo = pai
						pai = nodo.pai
					self.Rotacao_Esquerda(raiz, avo)
					trocar(pai.cor, avo.cor)
					nodo = pai

		raiz.cor = PRETO
