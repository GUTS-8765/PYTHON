salary = int(input("Введите зарплату за месяц: "))
credit_payment = int(input("Введите сумму платежа по кредиту: "))
utility_debt = int(input("Введите задолженность за коммунальные услуги: "))
sum = salary - credit_payment - utility_debt
print(sum)