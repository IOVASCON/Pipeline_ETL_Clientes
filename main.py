# -*- coding: utf-8 -*-
import os
from scripts.extract import extract_data
from scripts.transform import transform_data
from scripts.load import load_data
from scripts.generate_message import generate_message
from config.settings import API_ENDPOINT

def main():
    input_file = 'L:/VSCode/PYTHON/DIO/Pipeline_ETL_Clientes/data/input/clientes.csv'
    
    # Extraindo dados
    data = extract_data(input_file)
    if data is None:
        print("Erro ao extrair dados. Verifique o arquivo de entrada e tente novamente.")
        return
    
    # Transformando dados
    transformed_data = transform_data(data)
    
    # Gerando mensagens personalizadas (limitar a 2 clientes para testes)
    transformed_data = transformed_data.head(2)
    transformed_data['message'] = transformed_data.apply(generate_message, axis=1)
    
    # Carregando dados
    status_code, response_text = load_data(API_ENDPOINT, transformed_data.to_dict(orient='records'))
    
    print(f'Status Code: {status_code}')
    print(f'Response Text: {response_text}')

if __name__ == '__main__':
    main()
