import numpy as np
import pandas as pd

def proyectar_ventas(catalogo_venta, inventario, total_unidades, Alfa_Periodos_escenarios, Beta_Periodos_escenarios):
    # Parámetros adicionales
    Periodo_Minimo_Venta = 3
    Periodo_Maximo_Venta = 34
    enganche = 0.05
    meses_finiquito = 8
    escenario_unico = len(Alfa_Periodos_escenarios) // 2

    # Proyección de todos los escenarios de Venta
    ventas_data = []
    for tipo_unidad, df in inventario.items():
        num_unidades = int(df.iloc[0]['# de unidades'])
        precio_venta = df.iloc[0]['Precio de Venta']
        
        for i in range(len(Alfa_Periodos_escenarios)):
            alfa = Alfa_Periodos_escenarios[i]
            beta = Beta_Periodos_escenarios[i]
            escenario_label = i+1
            
            # Generar valores aleatorios siguiendo una distribución Beta
            beta_distribution = np.random.beta(alfa, beta, num_unidades)
            
            # Escalar la distribución Beta para que esté en el rango [Periodo_Minimo_Venta, Periodo_Maximo_Venta]
            periodos_de_venta = Periodo_Minimo_Venta + beta_distribution * (Periodo_Maximo_Venta - Periodo_Minimo_Venta)
            periodos_de_venta = periodos_de_venta.round().astype(int)
            
            for j in range(num_unidades):
                ventas_data.append([tipo_unidad, precio_venta, periodos_de_venta[j], escenario_label])

    # Crear el DataFrame final
    ventas_escenarios = pd.DataFrame(ventas_data, columns=['Tipo de Unidad', 'Precio de Venta', 'Periodo_de_Venta', 'Escenario'])
    
    # Calcular ingresos por ventas para todos los escenarios
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

    # Proyección de un solo escenario
    alfa_intermedio = Alfa_Periodos_escenarios[escenario_unico]
    beta_intermedio = Beta_Periodos_escenarios[escenario_unico]
    ventas_data = []
    for tipo_unidad, df in inventario.items():
        num_unidades = int(df.iloc[0]['# de unidades'])
        precio_venta = df.iloc[0]['Precio de Venta']
        ventas_data.extend([[tipo_unidad, precio_venta]] * num_unidades)
    ventas_un_escenario = pd.DataFrame(ventas_data, columns=['Tipo de Unidad', 'Precio de Venta'])
    beta_distribution = np.random.beta(alfa_intermedio, beta_intermedio, total_unidades)
    ventas_un_escenario['Periodo_de_Venta'] = Periodo_Minimo_Venta + beta_distribution * (Periodo_Maximo_Venta - Periodo_Minimo_Venta)
    ventas_un_escenario['Periodo_de_Venta'] = ventas_un_escenario['Periodo_de_Venta'].round().astype(int)
    ventas_un_escenario['Escenario'] = escenario_unico + 1

    # Calcular ingresos por ventas para un solo escenario
    ingresos_venta_un_escenario = ventas_un_escenario.copy()
    ingresos_venta_un_escenario['Ingresos por Venta'] = ingresos_venta_un_escenario['Precio de Venta'] * enganche
    ingresos_venta_un_escenario.drop(columns=['Precio de Venta'], inplace=True)
    ingresos_venta_un_escenario['Periodo'] = ingresos_venta_un_escenario['Periodo_de_Venta']
    ingresos_venta_un_escenario.drop(columns=['Periodo_de_Venta'], inplace=True)
    ingresos_venta_duplicado = ingresos_venta_un_escenario.copy()
    ingresos_venta_duplicado['Periodo'] += meses_finiquito
    ingresos_venta_duplicado['Ingresos por Venta'] /= (enganche / (1 - enganche))
    ingresos_venta_un_escenario = pd.concat([ingresos_venta_un_escenario, ingresos_venta_duplicado], ignore_index=True)
    ingresos_agrupados_un_escenario = ingresos_venta_un_escenario.groupby('Periodo')['Ingresos por Venta'].sum().reset_index()

    return ventas_escenarios, ingresos_venta, ingresos_agrupados, ventas_un_escenario, ingresos_venta_un_escenario, ingresos_agrupados_un_escenario