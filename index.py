def ordenar_paises(lista_paises, criterio):
    if criterio == 'nome':
        return sorted(lista_paises, key=lambda x: x[0])
    elif criterio == 'pib':
        return sorted(lista_paises, key=lambda x: x[1])
    else:
        print("Critério inválido! Use 'nome' ou 'pib'.")
        return lista_paises

# Entrada de dados
paises = []
n = int(input("Quantos países deseja adicionar? "))

for _ in range(n):
    nome = input("Nome do país: ")
    pib = float(input(f"PIB de {nome} (em bilhões): "))
    paises.append((nome, pib))

# Escolha do critério de ordenação
criterio = input("Ordenar por 'nome' ou 'pib'? ").strip().lower()

# Ordenação e exibição
paises_ordenados = ordenar_paises(paises, criterio)
print("\nLista ordenada:")
for nome, pib in paises_ordenados:
    print(f"{nome}: {pib:.2f} bilhões")
