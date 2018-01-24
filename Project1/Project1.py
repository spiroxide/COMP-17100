# name: Erich Ostendarp
# date: 10/4/17
# purpose: a currency converter that asks the user to enter the currency to convert from and to
# and the amount to be converted between US dollars, Canadian dollars, and Euros and vice versa.


CD_TO_EU = .69
CD_TO_US = .78
EU_TO_CD = 1.46
EU_TO_US = 1.13
US_TO_CD = 1.29
US_TO_EU = .88

end = False

while not end:
    from_currency = input("Enter a currency to convert from (CD, EU, US): ")
    to_currency = input("Enter a currency to convert to: ")
    conversion_amount = float(input("Enter an amount to convert from: "))

    valid = False

    while not valid:
        if (from_currency == 'CD' or from_currency == 'EU' or from_currency == 'US') and (to_currency == 'CD' or to_currency == 'EU' or to_currency == 'US'):
            if from_currency != to_currency:
                if conversion_amount > 0:
                    valid = True
                else:
                    print("Invalid amount to convert from")
                    conversion_amount = float(input("Enter an amount to convert from: "))
            else:
                print("A conversion is required")
                from_currency = input("Enter a currency to convert from (CD, EU, US): ")
                to_currency = input("Enter a currency to convert to: ")
        elif from_currency != 'CD' and from_currency != 'EU' and from_currency != 'US':
            print("Invalid currency to convert from")
            from_currency = input("Enter a currency to convert from (CD, EU, US): ")
        elif to_currency != 'CD' and to_currency != 'EU' and to_currency != 'US':
            print("Invalid currency to convert to")
            to_currency = input("Enter a currency to convert to (CD, EU, US): ")

    transaction = input("Enter a transaction type (cash/check): ")

    while transaction != "cash" and transaction != "check":
        print("Invalid transaction type")
        transaction = input("Enter a transaction type (cash/check): ")

    fee = -1

    if transaction == "cash":
        fee = conversion_amount * .05
    else:
        fee = conversion_amount * .01

    charged_amount = conversion_amount - fee

    converted_amount = -1

    if from_currency == 'CD':
        if to_currency == 'EU':
            converted_amount = charged_amount * CD_TO_EU
        else:
            converted_amount = charged_amount * CD_TO_US
    elif from_currency == 'EU':
        if to_currency == 'CD':
            converted_amount = charged_amount * EU_TO_CD
        else:
            converted_amount = charged_amount * EU_TO_US
    else:
        if to_currency == 'CD':
            converted_amount = charged_amount * US_TO_CD
        else:
            converted_amount = charged_amount * US_TO_EU

    print("You have converted " + str(conversion_amount) + ' ' + str(from_currency) + " to " + str(converted_amount) + ' ' + str(to_currency) + " with a fee of " + str(fee))

    if input("Enter \"quit\" if you would like to quit or press \'Enter\' to continue: ") == "quit":
        end = True
