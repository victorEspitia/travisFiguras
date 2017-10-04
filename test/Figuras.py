class Figuras(object):

	def __init__(self):
		self.resultado = 0

	def obtener_resultado(self):
		return self.resultado

	def obtener_area_circulo(self,radio):
		self.resultado = 3.1416 * (radio ** 2)

	def obtener_area_triangulo(self,base,altura):
		self.resultado = (base * altura) / 2

	def obtener_area_cuadrado(self,lado):
		self.resultado = lado * lado
		
	def obtener_area_trapecio(self,altura,base1,base2):
		self.resultado = altura * ((base1 + base2) / 2)

