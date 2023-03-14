def currency_converter(currency, conv_coef):
    return currency*conv_coef


if __name__=="__main__":
    usd_to_Yuan = 6.84
    pound_to_kg= 0.15

    usd=[1,1500,25000]
    Yuan=[1,1750,28000]

    #Converting USD to Yuan
    print("\nConvert Currency in USD to Yuan:")

    for curr in usd:
        wght_pounds=currency_converter(curr, usd_to_Yuan)
        print(f"{curr} USD -> {wght_pounds} Yuan")

    #Converting Yuan to USD
    print("\nConvert Currency in Yuan to USD:")

    for curr in Yuan:
        wght_pounds=currency_converter(curr, pound_to_kg)
        print(f"{curr} Yuan -> {wght_pounds} USD")