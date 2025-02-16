# Defina uma interface para a estratégia de cálculo do salário
#interface PaycheckStrategy {
    #calculatePay(hoursWorked: number, baseSalary: number): number;

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