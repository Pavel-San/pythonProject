def currency_exchange(usd):
    ref1 = usd / 1.17
    return ref1


usd = float(input("Введите сумму в долларах США: "))

print("Сумма в Euro = ", '{:.2f}'.format(currency_exchange(usd)))

