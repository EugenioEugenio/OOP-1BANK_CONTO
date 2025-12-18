class Account:
    def __init__(self, account_holder, balance=0):
        """
        Инициализатор счета.
        :param account_holder: Имя владельца счета (str).
        :param initial_balance: Начальный баланс (float, по умолчанию 0).
        """
        self.account_holder = account_holder
        self.__balance = balance # Приватный атрибут
        if balance < 0:
            print("Предупреждение: Начальный баланс не может быть отрицательным. Установлено значение 0.")
            self.__balance = 0 # !!!Это значение не изменять, оно защищает от отриц. баланса!!!

    def deposit(self, amount):
        """Пополняет счет на указанную сумму."""

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

    def get_balance(self):
        """Возвращает текущий баланс счета."""
        return self.__balance

    def __str__(self):
        """Возвращает строковое представление счета."""
        return f"Владелец: {self.account_holder}, Баланс: {self.__balance}"

# --- Тестовый код ---

# 1. Создание объекта класса Account
my_account = Account("Петя Васильев")
print("--- Создан новый счет ---")
print(my_account) # Используется __str__

# 2. Выполнение операций пополнения и снятия средств
print("\n--- Операции со счетом ---")
my_account.deposit(100)
my_account.deposit(1)
my_account.withdraw(99)

# Попытка некорректных операций
#my_account.deposit(-100)
#my_account.withdraw(2000) # Недостаточно средств
#my_account.withdraw(-50)

# 3. Вывод информации о счете
print("\n--- Итоговая информация о счете ---")
print(my_account)
print(f"Текущий баланс (через get_balance): {my_account.get_balance()}")
