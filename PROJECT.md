# Desafio


##  Tecnologias e Recursos utilizados

- Para utilizar este projeto utilize Python 3.9.5


## Escopo do Programa

- Receber um arquivo csv com dados de uma tranportadora.
- Utilizar seus dados para retornar a melhor opção de transportadora:
    -   Qual tem o menor preço de acordo com a cidade?
    -   Qual a melhor prazo de entrega acordo com cidade?
- A respostas são impresas no console composta de.
    - Transportadora
    - Cidade de destino
    - Peso da Carga
    - Prazo de Entrega
    - Custo total do Frete

## Como usar

1. Clone do  repositório
2. Entre na pasta do projeto
3. Procure o arquivo main.py
4. Siga a instruções a seguir.

### Inicializando ShippingCost

Uma instancia do **ShippingCost** é usada para obter o retorno de acordo com os dados inseridos. Incialize o objeto:

```python
from shipping_cost import ShippingCost

shipping_cost = ShippingCost()
```
### Inserindo a url do CVS
Depois de instanciar o objeto você deve passar como parametro a url de arquivo .cvs.

```python
shipping_cost.open_file('transportadoras.csv')
```

Para verificar se os dados foram lidos você pode utilizar o método **print_data**, que deve retorna um dicionário com os dados da tabela inserida:

```python
shipping_cost.print_data()
```

### Calculando

#### **Pegando os dados de custo**

Para calcular os custo de acordo com tranpostadora e a cidade de destino, voce deve primeiro executar o método **calculate_cost_shipping**, que recebe como paramento o nome de uma cidade, um dicionário de dados, e valor float peso. E retorna os dados presentes sobre a cidade, transportadora, valores de custo de envio e prazo de entrega.

```python
costs = shipping_cost.calculate_cost_shipping('São Paulo', data, 10)
```

#### **Calculando o menor custo**

Para pegar o menor custo no valor do frete por transportadora utilize como parametro a dados retornados pelo metodo **calculate_cost_shipping**, que deve retorna uma linha de dicionário com os dados sobre a nome da transportadora, nome da cidade, custo por peso, peso, prazo de entrega e custo total:

```python
costs = shipping_cost.calculate_cost_shipping('São Paulo', data, 10)
response = shipping_cost.get_best_option_cost(costs)
```
#### **Buscando pelo prazo mais rápido de frete**

Para pegar o prazo mais rápido de frete por transportadora utilize o método **get_fast_option** que recebe como parametro a dados retornados pelo método **calculate_cost_shipping**, dessa forma deve retorna uma linha de dicionário com os dados sobre a nome da transportadora, nome da cidade, custo por peso, peso, prazo de entrega e custo total:

```python
costs = shipping_cost.calculate_cost_shipping('São Paulo', data, 10)
response = shipping_cost.get_fast_option(costs)
```

## Exemplo

Para testar rapidamente se tudo está ok, deixei um arquivo "main.py" que segue o fluxo de funcionamento de acordo com este tutorial. Basta executar no terminal:

```bash
python3 main.py
```

