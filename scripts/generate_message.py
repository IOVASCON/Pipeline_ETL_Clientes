# -*- coding: utf-8 -*-
import openai
from config.settings import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def generate_message(customer_data, test_mode=True):
    if test_mode:
        # Mensagem simulada para testes
        return f"Mensagem simulada para o cliente com dados: {customer_data}"
    
    # Código real para fazer a chamada à API OpenAI
    prompt = f"Crie uma mensagem personalizada de marketing sobre venda de seguros de vida para o cliente com os seguintes dados: {customer_data}"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Você é um assistente útil."},
            {"role": "user", "content": prompt}
        ]
    )
    message = response['choices'][0]['message']['content'].strip()
    return message
