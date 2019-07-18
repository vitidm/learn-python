
# Conversor de divisas.
# Divisas: €, $, pounds

foreign_currencies = {
    'eur': [],
    'usd': [],
}

changes = {
    'eur_usd': 1.13,
    'usd_eur': 0.89,
}

def exchange (from_currency, amount):
    if from_currency == 'eur':
        foreign_currencies['eur'].append(amount)
    elif from_currency == 'usd':
        foreign_currencies['usd'].append(amount)

print('-------------------------------')
print('\t Only eur or usd')
print('-------------------------------')

from_currency = input('Enter your currency: ')

amount = input('Amount: ')

to_currency = input('Enter your change currency: ')  

if to_currency == 'usd' and from_currency == 'eur':
    print(float(changes['eur_usd']) * int(amount))
elif to_currency == 'eur' and from_currency == 'usd':
    print(float(changes['usd_eur']) * int(amount))





