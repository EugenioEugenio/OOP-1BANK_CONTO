

from CONTO_DAILY import Account

class BusinessAccount(Account):

    def __init__(self, account_holder, balance , overdraft_limit ):
        super().__init__(account_holder, balance)
        self.overdraft_limit = overdraft_limit
        print(f"Бизнес-счет с лимитом овердрафта: {self.overdraft_limit}")

    def deposit(self, amount):
            super().deposit(amount)

    def withdraw(self, amount):
        """Переопределенный метод для снятия средств с учетом овердрафта."""
        if amount > 0:
            # Проверяем, находится ли сумма в пределах доступных средств + лимит овердрафта
            if amount <= self._Account__balance + self.overdraft_limit:
                self._Account__balance -= amount
                # Если баланс ушел в минус, выводим соответствующее сообщение
                if self._Account__balance < 0:
                    print(f"Withdrawn using overdraft: {amount}. Текущий баланс: {self._Account__balance}")
                else:
                    print(f"Снято {amount} в пределах баланса. Текущий баланс: {self._Account__balance}")
            else:
                print(f"Exceeds overdraft limit. Попытка снять {amount}, доступно {self._Account__balance + self.overdraft_limit}.")
        else:
            print("Сумма снятия должна быть положительной.")

    def get_balance(self):
        super().get_balance()


    def __str__(self):
        """Переопределенное строковое представление для включения лимита овердрафта."""
        #return f"BusinessAccount Holder: {self.account_holder}, Balance: {business_acc.get_balance()}, Overdraft Limit: {self.overdraft_limit}"
        return f"BusinessAccount Holder: {self.account_holder}, Баланс : {self._Account__balance}, Overdraft Limit: {self.overdraft_limit}"


# Тестовый код
print("--- Создание бизнес-счета ---")
# Создаем объект класса BusinessAccount с начальным балансом 100 и лимитом овердрафта 500
business_acc =BusinessAccount("Света Колотушкина", balance= 0, overdraft_limit=500)
print(business_acc)

print("\n--- Пополнение счета ---")
business_acc.deposit(100)
print(business_acc)

print("\n--- Снятие средств в пределах баланса ---")
business_acc.withdraw(150)
print(business_acc)

print("\n--- Withdrawn using overdraft: ---")
business_acc.withdraw(300)
print(business_acc)

print("\n--- Попытка превысить лимит овердрафта ---")
business_acc.withdraw(400)
print(business_acc)