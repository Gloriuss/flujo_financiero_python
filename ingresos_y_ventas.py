import numpy as np
import pandas as pd
from scipy.stats import beta
from configuraciones import obtener_inventario, Escenarios_Periodos, Alfa_Periodos_Optimista, Beta_Periodos_Optimista, Alfa_Periodos_Pesimista, Beta_Periodos_Pesimista, Periodo_Minimo_Venta, Periodo_Maximo_Venta, enganche, meses_finiquito

def simular_escenarios_ventas():
    inventario = obtener_inventario()
    total_unidades = sum(item["# de unidades"] for item in inventario.values())
    Alfa_Periodos_escenarios = np.linspace(Alfa_Periodos_Optimista, Alfa_Periodos_Pesimista, Escenarios_Periodos)
    Beta_Periodos_escenarios = np.linspace(Beta_Periodos_Optimista, Beta_Periodos_Pesimista, Escenarios_Periodos)
    ventas_data = []

    for tipo_unidad, df in inventario.items():
        num_unidades = int(df.iloc[0]['# de unidades'])
        precio_venta = df.iloc[0]['Precio de Venta']
        
        for i in range(Escenarios_Periodos):
            alfa = Alfa_Periodos_escenarios[i]
            beta_param = Beta_Periodos_escenarios[i]
            escenario_label = i+1
            
            beta_distribution = np.random.beta(alfa, beta_param, num_unidades)
            periodos_de_venta = Periodo_Minimo_Venta + beta_distribution * (Periodo_Maximo_Venta - Periodo_Minimo_Venta)
            periodos_de_venta = periodos_de_venta.round().astype(int)
            
            for j in range(num_unidades):
                ventas_data.append([tipo_unidad, precio_venta, periodos_de_venta[j], escenario_label])

    ventas_escenarios = pd.DataFrame(ventas_data, columns=['Tipo de Unidad', 'Precio de Venta', 'Periodo_de_Venta', 'Escenario'])
    return ventas_escenarios

def calcular_ingresos(ventas_escenarios):
    ingresos_venta = ventas_escenarios.copy()
    ingresos_venta['Ingresos por Venta'] = ingresos_venta['Precio de Venta'] * enganche
    ingresos_venta.drop(columns=['Precio de Venta'], inplace=True)
    ingresos_venta['Periodo'] = ingresos_venta['Periodo_de_Venta']
    ingresos_venta.drop(columns=['Periodo_de_Venta'], inplace=True)
    
    ingresos_venta_duplicado = ingresos_venta.copy()
    ingresos_venta_duplicado['Periodo'] += meses_finiquito
    ingresos_venta_duplicado['Ingresos por Venta'] /= (enganche / (1 - enganche))
    
    ingresos_venta = pd.concat([ingresos_venta, ingresos_venta_duplicado], ignore_index=True)
    ingresos_agrupados = ingresos_venta.groupby(['Escenario', 'Periodo'])['Ingresos por Venta'].sum().reset_index()
    return ingresos_agrupados