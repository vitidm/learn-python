
# Conversor de divisas.
# Divisas: €, $, pounds

foreign_currencies = {
    '€': [],
    '$': [],
    'pound': [],
}

eur_changes = {
    'eur_usd': 1.13,
    'eur_gbp': 0.90,
}

usd_changes = {
    'usd_eur': 0.89,
    'usd_gbp': 0.80,
}

gbp_changes = {
    'gbp_eur': 1.11,
    'gbp_usd': 1.23,
}

print('-------------------------------')
print('\t Only €, $ and Pounds')
print('-------------------------------')


while True:
    input_currency = input('Enter your currency: ')

    if input_currency == 'exit':
        break

    if input_currency not in ['€', '$', 'pound']:
        print('Enter €, $ or pound')
        continue

    input_amount = input('Amount: ')

    if input_amount == 'exit':
        break
    
    if input_currency == '€':
        foreign_currencies['€'].append(input_amount)
    elif input_currency == '$':
        foreign_currencies['$'].append(input_amount)
    elif input_currency == 'pound':
        foreign_currencies['pound'].append(input_amount)

    input_change_currency = input('Enter your change currency: ')  
    break

if input_change_currency not in ['€', '$', 'pound']:
    print('Enter €, $ or pound')

if input_change_currency == '$' and input_currency == '€':
    print(float(eur_changes['eur_usd']) * int(input_amount))
elif input_change_currency == 'pound' and input_currency == '€':
    print(float(eur_changes['eur_gbp']) * int(input_amount))
elif input_change_currency == '€' and input_currency == '$':
    print(float(usd_changes['usd_eur']) * int(input_amount))
elif input_change_currency == 'pound' and input_currency == '$':
    print(float(usd_changes['usd_gbp']) * int(input_amount))
elif input_change_currency == '$' and input_currency == 'pound':
    print(float(gbp_changes['gbp_usd']) * int(input_amount))
elif input_change_currency == '€' and input_currency == 'pound':
    print(float(gbp_changes['gbp_eur']) * int(input_amount))



