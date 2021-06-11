from shipping_cost import ShippingCost

if __name__ == '__main__':
    shipping_cost = ShippingCost()  # Inicialize o objeto

    # Adicionando a url do arquivo .csv
    shipping_cost.open_file('transportadoras.csv')

    print("-------------------------------------------------")
    shipping_cost.print_data()  # Imprimindo os dados
    print("-------------------------------------------------")

    data = shipping_cost.get_data()  # Pegando os dados

    # Calculando os dados com cidade São Paulo
    costs = shipping_cost.calculate_cost_shipping('São Paulo', data, 10)
    print("-------------------------------------------------")
    print(f"Dados filtrados por cidade e transportadora:\n{costs}")

    print("-------------------------------------------------")
    best_cost = shipping_cost.get_best_option_cost(costs)
    print(f'Menor valor de Frete:\n{best_cost}')

    print("-------------------------------------------------")
    fast_option = shipping_cost.get_fast_option(costs)
    print(f'Menor prazo de Entrega:\n{fast_option}')
