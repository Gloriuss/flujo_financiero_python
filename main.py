import parametros_de_venta as pv
import configuracion_escenarios as ce
import ingresos_ventas as iv
import visualizacion as vz
import numpy as np


Escenarios_Periodos = 100
Alfa_Periodos_Optimista = 1.35
Beta_Periodos_Optimista = 3.76
Alfa_Periodos_Pesimista = 1.8
Beta_Periodos_Pesimista = 1.12
# Elegir el escenario intermedio o uno elegido
escenario_unico = Escenarios_Periodos // 2 # Índice intermedio (redondeado hacia arriba)
#escenario_unico = 0
# Generar valores interpolados para Alfa y Beta
Alfa_Periodos_escenarios = np.linspace(Alfa_Periodos_Optimista, Alfa_Periodos_Pesimista, Escenarios_Periodos)
Beta_Periodos_escenarios = np.linspace(Beta_Periodos_Optimista, Beta_Periodos_Pesimista, Escenarios_Periodos)
# Ejecutar las funciones de cada módulo
catalogo_venta, inventario, total_unidades = pv.configurar_venta()

# Llamar a la función para graficar los escenarios
ce.graficar_escenarios(Alfa_Periodos_escenarios, Beta_Periodos_escenarios)

ventas_escenarios, ingresos_venta, ingresos_agrupados, ventas_un_escenario, ingresos_venta_un_escenario, ingresos_agrupados_un_escenario = iv.proyectar_ventas(catalogo_venta, inventario, total_unidades, Alfa_Periodos_escenarios, Beta_Periodos_escenarios)
vz.visualizar(ventas_un_escenario, ingresos_agrupados_un_escenario)

# Imprimir resultados si es necesario
print(ventas_un_escenario)
print(ingresos_venta_un_escenario)
print(ingresos_agrupados_un_escenario)
print(ventas_escenarios)
print(ingresos_venta)
print(ingresos_agrupados)