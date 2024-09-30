Salario = float(input("informe o salário:") )

if Salario <= 3000:
    print("programador junior")
elif Salario > 4000 and Salario <= 6000:
    print('programador pleno')
elif Salario > 7000 and Salario <= 15000:
    print("programador senior")
else:
    print("gerente de projetos")