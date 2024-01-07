import pandas as pd
import random
import datetime

# Dados fictícios
data = {
    'Nome': ['João', 'Maria', 'Pedro', 'Ana', 'Lucas', 'Carla', 'Marcos', 'Laura', 'Rafael', 'Julia'],
    'RG': [str(random.randint(1000000, 9999999)) for _ in range(10)],
    'CPF': [str(random.randint(10000000000, 99999999999)) for _ in range(10)],
    'Data_Admissao': [datetime.date(2023, random.randint(1, 12), random.randint(1, 28)) for _ in range(10)],
    'Data_Alteracao': [datetime.datetime.now() for _ in range(10)],
    'Coordenada_X': [random.uniform(-46.200, -46.300) for _ in range(10)],  # Exemplo de coordenadas para Mogi das Cruzes
    'Coordenada_Y': [random.uniform(-23.500, -23.600) for _ in range(10)]   # Exemplo de coordenadas para Mogi das Cruzes
}

# Criar um DataFrame
df = pd.DataFrame(data)

# Salvar o DataFrame em um arquivo CSV
df.to_csv('Clientes.csv', index=False)