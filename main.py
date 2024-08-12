from configuraciones import configuracion_inicial
from ingresos_y_ventas import simular_escenarios_ventas, calcular_ingresos
from visualizacion import visualizar_escenario_unico, visualizar_histograma_ventas, visualizar_distribucion_unidades

# Configuración inicial
periodo_inicial = configuracion_inicial()

#Simulación de ventas
ventas_escenarios = simular_escenarios_ventas()

#Cálculo de ingresos

ingresos_agrupados = calcular_ingresos(ventas_escenarios)

#Visualización de resultados

visualizar_escenario_unico(ingresos_agrupados)
visualizar_histograma_ventas(ventas_escenarios, 3, 34)
visualizar_distribucion_unidades(ventas_escenarios, 3, 34)