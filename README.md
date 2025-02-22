# Explorando IA Generativa em um Pipeline de ETL com Python

## Descrição

Este projeto tem como objetivo envolver os clientes de maneira mais personalizada usando IA Generativa para criar mensagens de marketing. Utilizamos a API do ChatGPT (OpenAI) para gerar mensagens personalizadas de marketing sobre a venda de seguros de vida para cada cliente.

## Estrutura do Projeto

A estrutura do projeto é a seguinte:

    L:\VSCode\PYTHON\DIO\Pipeline_ETL_Clientes
    │ main.py
    │ requirements.txt
    │ README.md
    │
    ├───config
    │ settings.py
    │
    ├───data
    │ ├───input
    │ │ clientes.csv
    │ └───output
    │
    └───scripts
    init.py
    extract.py
    generate_message.py
    load.py
    transform.py

## Pré-requisitos

- Python 3.8+
- Conta na OpenAI para obter a chave da API
- Endpoint de API para enviar os dados processados

## Instalação

1. Clone o repositório:

   git clone <URL_DO_REPOSITORIO>
   cd Pipeline_ETL_Clientes

2. Instale as dependências:

    pip install -r requirements.txt

## Configuração

    Obter a chave da API:
        Vá para OpenAI API Keys e gere sua chave.

    Atualizar o arquivo config/settings.py:
        Substitua 'sua-chave-da-api-aqui' pela chave da API obtida.
        Substitua 'seu-endpoint-aqui' pelo URL do seu endpoint de API.

        # config/settings.py
        OPENAI_API_KEY = 'sua-chave-da-api-aqui'
        API_ENDPOINT = 'https://seu-endpoint-aqui'

## Executando o Projeto

Para executar o projeto, use o seguinte comando:

    python main.py

## Observações

    Chave da API: Você precisa obter uma chave da API do OpenAI para gerar mensagens de marketing personalizadas.
    Endpoint da API: Você precisa configurar um endpoint de API para enviar os dados processados.

## Estrutura de Arquivos

    main.py

    Arquivo principal que coordena o processo de ETL.
    config/settings.py

    Contém as configurações, incluindo a chave da API e o endpoint.
    scripts/extract.py

    Script para extrair dados do arquivo CSV.
    scripts/transform.py

    Script para transformar os dados conforme necessário.
    scripts/load.py

    Script para carregar os dados processados para um endpoint de API.
    scripts/generate_message.py

    Script para gerar mensagens personalizadas de marketing usando a API do OpenAI.

## Autor

Izairton O de Vasconcelos

## Licença

Este projeto é licenciado sob a MIT License.
