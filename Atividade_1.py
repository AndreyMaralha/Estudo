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

# fazer varias interfaces dependendo da resposta

funcionarios = str(input("Qual será o funcionário escolhido? "))


def funcionario_Horista():
    if funcionarios == "horista":
        hora_cobrada = int(input("Quanto tempo ele trabalhará? "))
        valor_hora = int(input("Quanto vai receber por hora? "))
        horista = (hora_cobrada * valor_hora)
        print("O funcionário horistá recebera um total de:", horista)
        if horista >= 1800:
            horista += 200
            print("Recebeu um bônus de R$200!!")
            print("O funcionário recebera um total de:", horista)

def funcionario_assalariado():
    if funcionarios == "assalariado":
        salario = int(input("Qual será o salário? "))
        if salario >= 1800:
            salario += 200
            print("Recebeu um bônus de R$200!!")
            print("O funcionário recebera um total de:", salario)


def funcionario_comissionado():
    if funcionarios == "comissionado":
        q_vendas = int(input("Quantas vendas foram feitas? "))
        v_vendas = int(input("Qual o valor de cada venda? "))
        s_comissionado = (q_vendas * v_vendas)
        if s_comissionado >= 1800:
            s_comissionado += 200
            print("Recebeu um bônus de R$200!!")
            print("O funcionário comissionado recebera um total de:", s_comissionado)


funcionario_Horista()
funcionario_assalariado()
funcionario_comissionado()
