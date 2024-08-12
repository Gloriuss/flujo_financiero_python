import pandas as pd
import numpy as np
import random
from scipy.stats import beta
from datetime import datetime

# Configuración inicial
def configuracion_inicial():
    seed = 44
    random.seed(seed)
    np.random.seed(seed)
    periodo_inicial = datetime(2022, 10, 1)
    return periodo_inicial

def obtener_inventario():
    catalogo_venta = {
        "Pinar": {
            "# de unidades": 64,
            "Tamaño m2": 72.9,
            "Precio Base x m2": 20048,
            "Costo de Construcción m2": 7674,
            "Meses Construcción": 7
        },
        "Olmo": {
            "# de unidades": 105,
            "Tamaño m2": 85.0,
            "Precio Base x m2": 20260,
            "Costo de Construcción m2": 7820,
            "Meses Construcción": 7
        },
        "Mezquite": {
            "# de unidades": 71,
            "Tamaño m2": 100.0,
            "Precio Base x m2": 19889,
            "Costo de Construcción m2": 7674,
            "Meses Construcción": 7
        }
    }
    inventario = {}
    for key, value in catalogo_venta.items():
        df = pd.DataFrame([value])
        df['Precio de Venta'] = df['Tamaño m2'] * df['Precio Base x m2']
        df['Costo de Construcción'] = df['Tamaño m2'] * df['Costo de Construcción m2']
        inventario[key] = df
    return inventario

# Otros parámetros y configuraciones
enganche = 0.05
meses_finiquito = 8
Periodo_Minimo_Venta = 3
Periodo_Maximo_Venta = 34
Escenarios_Periodos = 100
Alfa_Periodos_Optimista = 1.35
Beta_Periodos_Optimista = 3.76
Alfa_Periodos_Pesimista = 1.8
Beta_Periodos_Pesimista = 1.12