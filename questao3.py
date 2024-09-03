# 3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
# • O menor valor de faturamento ocorrido em um dia do mês;
# • O maior valor de faturamento ocorrido em um dia do mês;
# • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.


import json

with open('faturamento.json', 'r') as file:
    faturamento = json.load(file)

faturamento_filtrado = [dia['valor'] for dia in faturamento if dia['valor'] > 0]

menor_faturamento = min(faturamento_filtrado)
maior_faturamento = max(faturamento_filtrado)

media_mensal = sum(faturamento_filtrado) / len(faturamento_filtrado)

dias_acima_da_media = len([valor for valor in faturamento_filtrado if valor > media_mensal])

print(f"Menor valor de faturamento: R${menor_faturamento:.2f}")
print(f"Maior valor de faturamento: R${maior_faturamento:.2f}")
print(f"Número de dias com faturamento acima da média: {dias_acima_da_media}")



