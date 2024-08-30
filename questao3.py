# 3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
# • O menor valor de faturamento ocorrido em um dia do mês;
# • O maior valor de faturamento ocorrido em um dia do mês;
# • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.


import json

with open('faturamento.json', 'r') as file:
    faturamento_diario = json.load(file)


faturamento_valores = [dia["valor"] for dia in faturamento_diario if dia["valor"] > 0]


menor_faturamento = min(faturamento_valores)
maior_faturamento = max(faturamento_valores)


media_faturamento = sum(faturamento_valores) / len(faturamento_valores)


superior_media = len([valor for valor in faturamento_valores if valor > media_faturamento])


print(f"Menor valor de faturamento: {menor_faturamento:.2f}")
print(f"Maior valor de faturamento: {maior_faturamento:.2f}")
print(f"Número de dias com faturamento acima da média: {superior_media}")



