##
import unittest
from Figuras import Figuras
class FugurasTest(unittest.TestCase):

	def setUp(self):
		self.fig = Figuras()

	def test_valor_de_inicio_igual_a_cero(self):
		self.assertEquals(self.fig.obtener_resultado(), 0)

	def test_area_circulo(self):
		self.fig.obtener_area_circulo(2)
		self.assertEquals(self.fig.obtener_resultado(), 12.5664)

	def test_area_circulo_2(self):
		self.fig.obtener_area_circulo(16)
		self.assertEquals(self.fig.obtener_resultado(), 804.2496)
		
	def test_area_triangulo(self):
		self.fig.obtener_area_triangulo(4,4)
		self.assertEquals(self.fig.obtener_resultado(), 8)

	def test_area_triangulo_2(self):
		self.fig.obtener_area_triangulo(12,5)
		self.assertEquals(self.fig.obtener_resultado(), 30)

	def test_area_cuadrado(self):
		self.fig.obtener_area_cuadrado(5)
		self.assertEquals(self.fig.obtener_resultado(), 25)

	def test_area_cuadrado_2(self):
		self.fig.obtener_area_cuadrado(10)
		self.assertEquals(self.fig.obtener_resultado(), 100)

	def test_area_trapecio(self):
		self.fig.obtener_area_trapecio(5,5,5)
		self.assertEquals(self.fig.obtener_resultado(), 25)

	def test_area_trapecio_2(self):
		self.fig.obtener_area_trapecio(10,17,12)
		self.assertEquals(self.fig.obtener_resultado(), 140)

if __name__ == '__main__': # pragma: no cover
	unittest.main()
