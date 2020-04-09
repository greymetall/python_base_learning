# -*- coding: utf-8 -*-

# (цикл while)

# Ежемесячная стипендия студента составляет educational_grant руб., а расходы на проживание превышают стипендию
# и составляют expenses руб. в месяц. Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца
# Составьте программу расчета суммы денег, которую необходимо единовременно попросить у родителей,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.
# Формат вывода:
#   Студенту надо попросить ХХХ.ХХ рублей

educational_grant, expenses = 10000, 12000
months = 1
balance = educational_grant - expenses
months += 1
while months <= 10:
    expenses += expenses*3/100
    expenses = round(expenses, 2)
    # print(f'Расходы в {months} месяце составляют {expenses} руб.')
    balance -= expenses - educational_grant
    balance = round(balance, 2)
    # print(f'Баланс в {months} месяце составляет {balance} руб.')
    months += 1

print(f'Студенту надо попросить {-balance} рублей')