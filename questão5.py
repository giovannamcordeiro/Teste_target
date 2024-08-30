# 5) Escreva um programa que inverta os caracteres de um string.


def inverter_string(s):
    string_final = ""

    for i in range(len(s) - 1, -1, -1):
        string_final += s[i]

    return string_final

entrada = input("Digite a string para inverter: ")
print("String invertida:", inverter_string(entrada))