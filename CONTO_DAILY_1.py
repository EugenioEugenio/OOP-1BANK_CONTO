class Account:
    def __init__(self, account_holder, balance ):
        self.account_holder = account_holder
        self._Account__balance = balance # Приватный атрибут
        #self.__balance = 0
        #if balance < 0:
           # print("Предупреждение: Начальный баланс не может быть отрицательным. Установлено значение 0.")
           # self.__balance = 0 # !!!Это значение не изменять, оно защищает от отриц. баланса!!!

    def deposit(self, amount):
        if amount >= 0:
            self._Account__balance += amount
            print(f"Счет пополнен на {amount}. Новый баланс: {self._Account__balance}")
        else:
            print("Ошибка: Сумма пополнения должна быть положительной.")

    def withdraw(self, amount):
        if amount < 0:
            print("Ошибка: Сумма снятия должна быть положительной.")
        elif amount <= self._Account__balance:
            self._Account__balance -= amount
            print(f"Со счета снято {amount}. Новый баланс: {self._Account__balance}")
        else:
            print("Ошибка: Недостаточно средств на счете.")

    def get_balance(self):
        return self._Account__balance

    def __str__(self):
        return f"Владелец: {self.account_holder}, Баланс: {self._Account__balance}"



# 1. Создание объекта класса Account
my_account = Account("Петя Васильев",0 )
print("--- Создан новый счет ---")
print(my_account) # Используется __str__

# 2. Выполнение операций пополнения и снятия средств
print("\n--- Операции со счетом ---")
my_account.deposit(100)
my_account.deposit(1)
my_account.withdraw(99)


# 3. Вывод информации о счете
print("\n--- Итоговая информация о счете ---")
print(my_account)
print(f"Текущий баланс (через get_balance): {my_account.get_balance()}")
