# -*- coding: utf-8 -*-
import pandas as pd

def extract_data(file_path):
    try:
        data = pd.read_csv(file_path, encoding='latin1', dtype={'CNPJ': str})  # Usar codificação 'latin1' e definir tipo de dados
        print(f"Arquivo CSV lido com sucesso: {file_path}")
        print(data.head())  # Exibir as primeiras linhas do DataFrame para verificação
        return data
    except FileNotFoundError:
        print(f"Erro: Arquivo não encontrado em {file_path}")
    except Exception as e:
        print(f"Erro ao ler o arquivo CSV: {e}")
    return None
