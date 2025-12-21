# Класс SavingsAccount
from CONTO_DAILY import Account


class SavingsAccount(Account):

    def __init__(self, account_holder, balance, interest_rate):
       super().__init__( account_holder , balance)    # Вызов конструктора базового класса
       self.interest_rate = interest_rate  # Ставка --5 -- (например 5%)

    def deposit(self, amount):
        super().deposit(amount)


    def add_interest( self):
        interest = self._Account__balance * self.interest_rate/100
        self._Account__balance += interest
        print(f"Начисление процентов: +{interest:.2f}. Новый баланс: {self._Account__balance:.2f}")
        return interest


    def withdraw(self, amount):
        super(). withdraw (amount)

    def get_balance(self):
        super().get_balance()

# Тестовый код
print("--- Тестирование SavingsAccount ---")

# 1. Создание объекта SavingsAccount
savings_acc = SavingsAccount (  "Оля Морозова" ,balance=0, interest_rate=5)

# 2. Вывод начальной информации
print("\n--- Начальное состояние ---")
savings_acc.get_balance()
print (savings_acc)

# 3. Операция пополнения счета
print("\n--- Пополнение счета ---")
savings_acc.deposit(1000)

# 4. Начисление процентов
print("\n--- Interest added ----")
savings_acc.add_interest()

# 5. Вывод информации после начисления
print("\n--- Состояние после начисления процентов ---")
savings_acc.get_balance()

# 6. Списание
print("\n--- Списание средств ---")
savings_acc.withdraw(200)

# 7. Вывод финального баланса
print("\n--- Финальный баланс ---")
savings_acc.get_balance()
print (savings_acc)