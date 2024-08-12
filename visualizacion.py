import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as ticker

def visualizar_escenario_unico(ingresos_agrupados_un_escenario):
    plt.figure(figsize=(10, 6))
    plt.plot(ingresos_agrupados_un_escenario['Periodo'], ingresos_agrupados_un_escenario['Ingresos por Venta'], marker='o', linestyle='-')
    plt.title('Relación entre Periodo de Ingresos por Venta')
    plt.xlabel('Periodo de Venta')
    plt.ylabel('Ingresos por Venta')
    plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(format_to_currency))
    plt.gca().xaxis.set_major_formatter(ticker.FuncFormatter(format_to_currency))
    plt.grid(True)
    plt.show()

def visualizar_histograma_ventas(ventas_un_escenario, Periodo_Minimo_Venta, Periodo_Maximo_Venta):
    plt.figure(figsize=(10, 6))
    plt.hist(ventas_un_escenario['Periodo_de_Venta'], bins=range(Periodo_Minimo_Venta, Periodo_Maximo_Venta + 2), edgecolor='black', alpha=0.7)
    plt.title('Distribución de los Periodos de Venta')
    plt.xlabel('Periodo de Venta (meses)')
    plt.ylabel('Frecuencia')
    plt.xticks(range(Periodo_Minimo_Venta, Periodo_Maximo_Venta + 1))
    plt.grid(axis='y')
    plt.show()

def visualizar_distribucion_unidades(ventas_un_escenario, Periodo_Minimo_Venta, Periodo_Maximo_Venta):
    plt.figure(figsize=(14, 8))
    sns.histplot(data=ventas_un_escenario, x='Periodo_de_Venta', hue='Tipo de Unidad', multiple='dodge', 
                 bins=range(Periodo_Minimo_Venta, Periodo_Maximo_Venta + 2), edgecolor='black')
    plt.title('Distribución de los Periodos de Venta por Tipo de Unidad')
    plt.xlabel('Periodo de Venta (meses)')
    plt.ylabel('Frecuencia')
    plt.xticks(range(Periodo_Minimo_Venta, Periodo_Maximo_Venta + 1))
    plt.grid(axis='y')
    plt.show()

def format_to_currency(x, pos):
    return f'${x:,.0f}'