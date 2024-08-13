import matplotlib.pyplot as plt

def visualizar(ventas_un_escenario, ingresos_agrupados_un_escenario):
    # Visualización de Ventas en un solo escenario
    plt.figure(figsize=(12, 6))
    plt.hist(ventas_un_escenario['Periodo_de_Venta'], bins=range(min(ventas_un_escenario['Periodo_de_Venta']), max(ventas_un_escenario['Periodo_de_Venta']) + 1, 1))
    plt.xlabel('Periodo de Venta')
    plt.ylabel('Número de Unidades Vendidas')
    plt.title('Distribución de Ventas en un Escenario Único')
    plt.grid(True)
    plt.show()

    # Visualización de Ingresos en un solo escenario
    plt.figure(figsize=(12, 6))
    plt.bar(ingresos_agrupados_un_escenario['Periodo'], ingresos_agrupados_un_escenario['Ingresos por Venta'])
    plt.xlabel('Periodo')
    plt.ylabel('Ingresos por Venta')
    plt.title('Distribución de Ingresos en un Escenario Único')
    plt.grid(True)
    plt.show()