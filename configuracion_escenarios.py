import numpy as np
import matplotlib.pyplot as plt

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


def graficar_escenarios(Alfa_Periodos_escenarios, Beta_Periodos_escenarios):
    plt.figure(figsize=(10, 6))

    # Iterar sobre los valores de Alfa y Beta para cada escenario
    for i in range(Escenarios_Periodos):
        alfa = Alfa_Periodos_escenarios[i]
        beta_param = Beta_Periodos_escenarios[i]
        
        # Generar valores para la distribución Beta
        x = np.linspace(0, 1, 1000)
        y = beta.pdf(x, alfa, beta_param)
        
        # Escalar la distribución Beta al rango [Periodo_Minimo_Venta, Periodo_Maximo_Venta]
        x_scaled = Periodo_Minimo_Venta + x * (Periodo_Maximo_Venta - Periodo_Minimo_Venta)
        
        # Ajustar la densidad para que represente el número esperado de unidades
        y_scaled = y * total_unidades / (Periodo_Maximo_Venta - Periodo_Minimo_Venta) # Multiplicar por el rango del periodo

        # Determinar el color de la línea
        color = 'orange' if i == escenario_unico else 'blue'
        label = 'Escenario intermedio' if i == escenario_unico else ''

        # Graficar la distribución escalada
        plt.plot(x_scaled, y_scaled, color=color, label=label)

    # Añadir título y etiquetas
    plt.title('Distribuciones Beta Escaladas por Escenario')
    plt.xlabel('Periodo de Venta')
    plt.ylabel('Número Esperado de Unidades')
    plt.grid(True)
    plt.legend()
    plt.show()