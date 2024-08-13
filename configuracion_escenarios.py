import numpy as np

def configurar_escenarios():
    Escenarios_Periodos = 100
    Alfa_Periodos_Optimista = 1.35
    Beta_Periodos_Optimista = 3.76
    Alfa_Periodos_Pesimista = 1.8
    Beta_Periodos_Pesimista = 1.12
    
    # Generar valores interpolados para Alfa y Beta
    Alfa_Periodos_escenarios = np.linspace(Alfa_Periodos_Optimista, Alfa_Periodos_Pesimista, Escenarios_Periodos)
    Beta_Periodos_escenarios = np.linspace(Beta_Periodos_Optimista, Beta_Periodos_Pesimista, Escenarios_Periodos)

    return Alfa_Periodos_escenarios, Beta_Periodos_escenarios