import matplotlib.pyplot as plt

# Dados
jogos = ['Grand Theft Auto V', 'Call of Duty: Black Ops 3', 'Red Dead Redemption 2',
         'Call of Duty: WWII', 'FIFA 18']
vendas = [19.39, 15.09, 13.94, 13.4, 11.8]

# Gráfico 1: Gráfico de Barras
plt.figure(figsize=(10, 6))
plt.bar(jogos, vendas)
plt.xlabel('Jogos')
plt.ylabel('Vendas (em milhões)')
plt.title('Vendas de Jogos (Gráfico de Barras)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# Gráfico 2: Gráfico de Linhas
plt.figure(figsize=(10, 6))
plt.plot(jogos, vendas, marker='o', linestyle='-')
plt.xlabel('Jogos')
plt.ylabel('Vendas (em milhões)')
plt.title('Vendas de Jogos (Gráfico de Linhas)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# Gráfico 3: Gráfico de Pizza
plt.figure(figsize=(8, 8))
plt.pie(vendas, labels=jogos, autopct='%1.1f%%', startangle=90)
plt.title('Vendas de Jogos (Gráfico de Pizza)')
plt.show()