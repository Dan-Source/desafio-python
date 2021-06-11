import csv


class ShippingCost:

    def __init__(self):
        self.data = {}

    def __str__(self):
        return f'Dados de Custo de Prazos e Entregas'

    def open_file(self, file_url):
        with open(file_url, encoding='utf-8', mode='r') as file:

            table = csv.DictReader(file)
            row_id = 0
            for rows in table:
                self.data[row_id] = rows
                row_id = row_id + 1

    def print_data(self):
        for item in self.data:
            print(self.data[item])

    def get_data(self):
        return self.data

    def clean_data_float(self, value):
        value = value.replace('R$ ', '')
        value = float(value)
        return round(value, 2)

    def clean_data_hours(self, value):
        value = value.replace('h', '')
        return int(value)

    def less_than_100_kg(self, cidade, data, weight):
        costs = {}
        if weight <= 100:
            for item in data:
                if cidade in data[item].values():

                    name = data[item][" Nome"]
                    valor_por_peso = self.clean_data_float(
                        data[item]["Custo de Frete até 100Kg [R$/Kg]"])
                    custo_total = valor_por_peso * weight
                    prazo_de_entrega = self.clean_data_hours(
                        data[item]["Tempo para Entrega"])

                    costs[name] = {
                        'Transportadora': data[item][' Nome'],
                        'Cidade': data[item]["Cidade"],
                        'Valor por Kg': valor_por_peso,
                        'Peso': weight,
                        'Prazo de Entraga': prazo_de_entrega,
                        'Custo Total': round(custo_total, 2),
                    }
            return costs
        return f'O peso {weight} ou {cidade} deve estar incorreto'

    def more_than_100_kg(self, cidade, data, weight):
        costs = {}
        if weight > 100:
            for item in data:
                if cidade in data[item].values():

                    name = data[item][" Nome"]
                    valor_por_peso = self.clean_data_float(
                        data[item]["Custo de Frete mais de 100Kg [R$/Kg]"])
                    custo_total = valor_por_peso * weight
                    prazo_de_entrega = self.clean_data_hours(
                        data[item]["Tempo para Entrega"])

                    costs[name] = {
                        'Cidade': data[item]["Cidade"],
                        'Peso': weight,
                        'Valor por Kg': valor_por_peso,
                        'Prazo de Entraga': prazo_de_entrega,
                        'Custo Total':  round(custo_total, 2),
                    }
            return costs
        return f'O peso {weight} ou {cidade} deve estar incorreto'

    def calculate_cost_shipping(self, cidade, data, weight):
        if weight <= 100:
            return self.less_than_100_kg(cidade, data, weight)
        if weight > 100:
            return self.more_than_100_kg(cidade, data, weight)

    def get_best_option_cost(self, costs):
        minumo_value = min((d['Custo Total']) for d in costs.values())
        for item in costs:
            if minumo_value == costs[item]['Custo Total']:
                return costs[item]

    def get_fast_option(self, costs):
        minumo_value = min((d['Prazo de Entraga']) for d in costs.values())
        for item in costs:
            if minumo_value == costs[item]['Prazo de Entraga']:
                return costs[item]
