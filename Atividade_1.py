# Defina uma interface para a estratégia de cálculo do salário
# interface PaycheckStrategy {
# calculatePay(hoursWorked: number, baseSalary: number): number;

# Os alunos devem implementar pelo menos três estratégias diferentes:
# - Funcionário Horista
# - Funcionário Assalariado
# - Funcionário Comissionado

# Criar uma classe Employee que utilize uma estratégia de pagamento
# A classe deve armazenar nome, salário base e a estratégia de pagamento
# Além disso, deve ter um método que calcula o salário com base na estratégia

# Os alunos também devem adicionar uma funcionalidade extra:
# - Criar uma classe para aplicar bônus aos funcionários
# - O bônus deve ser aplicado como um decorador, sem modificar a classe original

# Instruções:
# 1. Criar as classes necessárias para a estrutura acima.
# 2. Implementar os diferentes tipos de estratégias de pagamento.
# 3. Criar testes unitários para validar os cálculos de pagamento.
# 4. Demonstrar o funcionamento com pelo menos três tipos de funcionários diferentes.

# Exemplo de uso esperado:
# const employee = new Employee("Nome", 3000, new SalariedPayStrategy());
# console.log(employee.calculateSalary());


# Salário Base:

def S_funcionarios():

    S_funcionario_horista = float(
        input("Quanto será a hora do Funcionário Horista? "))
    S_funcionario_assalariado = float(
        input("Qual será o salário do Funcionário Assalariado? "))
    S_funcionario_comissionado = float(
        input("Qual será o salário do Funcionário Comissionado? "))
    horas = float(
        input("(Em horas) Qual será o tempo que o funcionário horista trabalhará? "))

    salario_horista = S_funcionario_horista * horas

    print("O Salário do Funcionário Horista foi de: R$",
          salario_horista, "e trabalhou:", horas, "horas")
    print("O Salário do Funcionário Assalariado foi de: R$",
          S_funcionario_assalariado)
    print("O Salário do Funcionário Comissionado foi de: R$",
          S_funcionario_comissionado)

    return salario_horista, S_funcionario_assalariado, S_funcionario_comissionado


def bonus(salario_horista, salario_assalariado, salario_comissionado):

    if salario_horista > 1800:
        salario_horista += 200
        print("Parabéns, foi concedido R$200 de bônus para o Funcionário Horista!")
    if salario_assalariado > 1800:
        salario_assalariado += 200
        print("Parabéns, foi concedido R$200 de bônus para o Funcionário Assalariado!")
    if salario_comissionado > 1800:
        salario_comissionado += 200
        print("Parabéns, foi concedido R$200 de bônus para o Funcionário Comissionado!")

    print("Novo salário do Funcionário Horista: R$", salario_horista)
    print("Novo salário do Funcionário Assalariado: R$", salario_assalariado)
    print("Novo salário do Funcionário Comissionado: R$", salario_comissionado)


salario_horista, salario_assalariado, salario_comissionado = S_funcionarios()

bonus(salario_horista, salario_assalariado, salario_comissionado)
