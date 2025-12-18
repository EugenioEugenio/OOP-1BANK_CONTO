# Класс SavingsAccount
from CONTO_DAILY import Account


class SavingsAccount(Account):
    def __init__(self,  balance=0, interest_rate=0.03):
        # Вызов конструктора базового класса
        super().__init__( balance)
        # Новый атрибут
        self.__balance = balance
        self.interest_rate = interest_rate # Ставка в долях (например, 0.05 для 5%)

    def deposit(self, amount):
        """Пополняет счет на указанную сумму."""
        #Account.deposit(self,amount)
        if amount >= 0:
            self.__balance += amount
            print(f"Счет пополнен на {amount}. Новый баланс: {self.__balance}")
        else:
           print("Ошибка: Сумма пополнения должна быть положительной.")

    def withdraw(self, amount):
        """Снимает средства со счета."""
        if amount < 0:
            print("Ошибка: Сумма снятия должна быть положительной.")
        elif amount <= self.__balance:
            self.__balance -= amount
            print(f"Со счета снято {amount}. Новый баланс: {self.__balance}")
        else:
            print("Ошибка: Недостаточно средств на счете.")


    def add_interest(self):
        """Начисляет проценты на текущий баланс."""
        # Формула: interest = balance * interest_rate
        interest = self.__balance * self.interest_rate
        self.__balance += interest
        print(f"Начисление процентов: +{interest:.2f}. Новый баланс: {self.__balance:.2f}")
        return interest

    def get_balance(self):
        """Переопределенный метод для вывода баланса с процентами."""
        print(f"Баланс сберегательного счета : {self.__balance:.2f}")
        return self.__balance

# Тестовый код
print("--- Тестирование SavingsAccount ---")

# 1. Создание объекта SavingsAccount
savings_acc = SavingsAccount ( balance=1000, interest_rate=0.15) # 3% годовых

# 2. Вывод начальной информации
print("\n--- Начальное состояние ---")
savings_acc.get_balance()

# 3. Операция пополнения счета
print("\n--- Пополнение счета ---")
savings_acc.deposit(500)

# 4. Начисление процентов
print("\n--- Начисление процентов ---")
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