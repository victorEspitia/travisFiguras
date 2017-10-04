# -*- coding: utf-8 -*-
from lettuce import step, world
from Figuras import Figuras

@step(u'cuando realizo la operacion')
def cuando_realizo_la_operacion(step):
    pass

# Area Circulo
@step(u'Dado el radio de un circulo es "([^"]*)" cm.')
def dado_que_ingreso_el_numero_group1(step, num1):
    world.fig = Figuras()
    world.fig.obtener_area_circulo(int(num1))
@step(u'el area del circulo es "([^"]*)" cm.')
def entonces_obtengo_el_resultado_group1(step, esperado):
    obtenido = float(world.fig.obtener_resultado())
    assert float(esperado) == obtenido,'El resultado esperado de '+esperado+" y el obtenido es "+str(obtenido)

# Area Triangulo
@step(u'Dada la base y altura de un triangulo es "([^"]*)" y "([^"]*)" cm.')
def dado_que_ingreso_el_numero_group1_group2(step, num1, num2):
    world.fig = Figuras()
    world.fig.obtener_area_triangulo(int(num1),int(num2))
@step(u'el area del triangulo es "([^"]*)" cm.')
def entonces_obtengo_el_resultado_group1(step, esperado):
    obtenido = float(world.fig.obtener_resultado())
    assert float(esperado) == obtenido,'El resultado esperado de '+esperado+" y el obtenido es "+str(obtenido)

# Area Cuadrado
@step(u'Dado el lado de un cuadrado es "([^"]*)" cm.')
def dado_que_ingreso_el_numero_group1(step, num1):
    world.fig = Figuras()
    world.fig.obtener_area_cuadrado(int(num1))
@step(u'el area del cuadrado es "([^"]*)" cm.')
def entonces_obtengo_el_resultado_group1(step, esperado):
    obtenido = float(world.fig.obtener_resultado())
    assert float(esperado) == obtenido,'El resultado esperado de '+esperado+" y el obtenido es "+str(obtenido)

# Area Trapecio
@step(u'Dada la altura, base mayor, base menor de un trapecio es "([^"]*)" , "([^"]*)" y "([^"]*)" cm.')
def dado_que_ingreso_el_numero_group1_group2_group3(step, num1, num2, num3):
    world.fig = Figuras()
    world.fig.obtener_area_trapecio(int(num1),int(num2),int(num3))
@step(u'el area del trapecio es "([^"]*)" cm.')
def entonces_obtengo_el_resultado_group1(step, esperado):
    obtenido = float(world.fig.obtener_resultado())
    assert float(esperado) == obtenido,'El resultado esperado de '+esperado+" y el obtenido es "+str(obtenido)
