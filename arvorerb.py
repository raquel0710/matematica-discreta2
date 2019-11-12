BLACK = 0
RED = 1

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

		nodo = nodos(RED, dados)
		self.raiz = Arvore_Binaria(self.raiz, nodo)
		self.ajustamentos(self.raiz, nodo)# not working

	def deletar(self, dados):
		pass

	#check params
	# if pass by value doesnt work return the new parent
	def Rotacao_Esquerda(self, raiz, nodo):
		pass

	def Rotacao_Direita(self, raiz, nodo):
		pass

	def level_order_traverse(self, l=[]):
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
		while nodo is not raiz and nodo.cor is not BLACK and nodo.pai.cor is RED:
			pai = nodo.pai
			avo = nodo.pai.pai
			# Case A - parent is left child of grandparent
			if pai is avo.left:
				tio = avo.right
				# Case 1 - Uncle is red
				if tio is not None and tio.cor is RED:
					tio.cor = BLACK
					pai.cor = BLACK
					avo.cor = RED
					nodo = avo
				else:
					# Case 2 - X is the right child of the parent
					if nodo is pai.right:
						self.Rotacao_Esquerda(raiz, pai)
						nodo = pai
						pai = nodo.pai

					# Case 3 - X is the left child of the parent
					self.Rotacao_Direita(raiz, avo)
					trocar(pai.color, avo.cor)
					nodo = pai

			# Case B - parent is right child of grandparent
			else:
				tio = avo.lef
				# Case 1 - Uncle is red
				if tio is not None and tio.cor is RED:
					tio.cor = BLACK
					pai.cor = BLACK
					avo.color = RED
					nodo = avo
				else:
					# Case 2 - X is the left child of the parent
					if nodo is pai.left:
						self.Rotacao_Direita(raiz, pai)
						nooe = pai
						pai = nodo.pai
					# Case 3 - X is the right child of the parent
					self.Rotacao_Esquerda(raiz, avo)
					trocar(pai.cor, avo.cor)
					nodo = pai

		raiz.cor = BLACK		
