import pandas as pd

def configurar_venta():
    # Parámetros de Venta
    catalogo_venta = {
        "Prototipo 1": {
            "# de unidades": 64,
            "Tamaño m2": 72.9,
            "Precio Base x m2": 20048,
            "Costo de Construcción m2": 7674,
            "Meses Construcción": 7
        },
        "Prototipo 2": {
            "# de unidades": 105,
            "Tamaño m2": 85.0,
            "Precio Base x m2": 20260,
            "Costo de Construcción m2": 7820,
            "Meses Construcción": 7
        },
        "Prototipo 3": {
            "# de unidades": 71,
            "Tamaño m2": 100.0,
            "Precio Base x m2": 19889,
            "Costo de Construcción m2": 7674,
            "Meses Construcción": 7
        }
    }
    
    # Crear inventario y total de unidades
    total_unidades = sum(item["# de unidades"] for item in catalogo_venta.values())
    inventario = {}
    for key, value in catalogo_venta.items():
        df = pd.DataFrame([value])
        df['Precio de Venta'] = df['Tamaño m2'] * df['Precio Base x m2']
        df['Costo de Construcción'] = df['Tamaño m2'] * df['Costo de Construcción m2']
        inventario[key] = df

    return catalogo_venta, inventario, total_unidades