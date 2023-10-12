def salario_desconto_inss(salario_bruto):
    desconto_inss = salario_bruto * 0.11
    salario_liquido = salario_bruto - desconto_inss
    return salario_liquido, desconto_inss

salario_bruto = float(input("Digite o salário bruto: "))

salario_liquido, desconto_inss = salario_desconto_inss(salario_bruto)

print(f"Salário Bruto: R${salario_bruto:.2f}")
print(f"Desconto do INSS (11%): R${desconto_inss:.2f}")
print(f"Salário Líquido: R${salario_liquido:.2f}")