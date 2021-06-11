import csv


def clean_data_hours(value):
    value = value.replace('h', '')
    return int(value)


def clean_data_float(value):
    value = value.replace('R$ ', '')
    return float(value)


def more_than_100_kg(cidade, data, weight):
    costs = {}
    if weight > 100:
        for item in data:
            if cidade in data[item].values():
                name = data[item][" Nome"]
                custo_total = clean_data_float(
                    data[item]["Custo de Frete mais de 100Kg [R$/Kg]"]) * weight
                costs[name] = {
                    'Cidade': data[item]["Cidade"],
                    'Peso': weight,
                    'Tempo': clean_data_hours(data[item]["Tempo para Entrega"]),
                    'Custo Total':  custo_total,
                }
        return costs
    return f'The {weight}kg must be grater than 100kg'


def less_than_100_kg(cidade, data, weight):
    costs = {}
    if weight <= 100:
        for item in data:
            if cidade in data[item].values():
                name = data[item][" Nome"]
                custo_total = clean_data_float(
                    data[item]["Custo de Frete até 100Kg [R$/Kg]"]) * weight
                costs[name] = {
                    'Transportadora': data[item][' Nome'],
                    'Cidade': data[item]["Cidade"],
                    'Valor por Kg': data[item]["Custo de Frete até 100Kg [R$/Kg]"],
                    'Peso': weight,
                    'Tempo': clean_data_hours(data[item]["Tempo para Entrega"]),
                    'Custo Total': custo_total,
                }
        return costs
    return f'O peso {weight}kg deve ser menor que 100kg'


def get_option_mais_em_conta(costs):

    minumo_value = min((d['Custo Total']) for d in costs.values())
    for item in costs:
        if minumo_value == costs[item]['Custo Total']:
            return costs[item]


def get_option_mais_rapida(costs):

    minumo_value = min((d['Tempo']) for d in costs.values())
    for item in costs:
        if minumo_value == costs[item]['Tempo']:
            return costs[item]


def calculate_cost_shipping(cidade, data, weight):
    if weight <= 100:
        return less_than_100_kg(cidade, data, weight)
    if weight > 100:
        return more_than_100_kg(cidade, data, weight)


def open_file(file_url):
    data = {}
    with open(file_url, encoding='utf-8', mode='r') as file:

        table = csv.DictReader(file)
        row_id = 0
        for rows in table:
            data[row_id] = rows
            row_id = row_id + 1
    return data


data = open_file('transportadoras.csv') # abrir o arquivo 
weight = 94
costs = calculate_cost_shipping('Campinas', data, weight) 
print(get_option_mais_em_conta(costs))

print(get_option_mais_rapida(costs))
