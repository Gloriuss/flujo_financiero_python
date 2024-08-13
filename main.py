import parametros_de_venta as pv
import configuracion_escenarios as ce
import ingresos_ventas as iv
import visualizacion as vz

# Ejecutar las funciones de cada módulo
catalogo_venta, inventario, total_unidades = pv.configurar_venta()
Alfa_Periodos_escenarios, Beta_Periodos_escenarios = ce.configurar_escenarios()

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