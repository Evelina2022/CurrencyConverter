def currency_converter(currency, conv_coef):
   return currency * conv_coef


if __name__ == "__main__":
   USD_to_yuan = 6.84
   yuan_to_USD =0.15
   currency_in_USD =[1, 1500, 25000]
   currency_in_yuan = [1, 1750, 28000]

   #converting USD to Yuan
   print("\nConvert currensy in USD to Yuan's:")

   for curr in currency_in_USD:
      curr_USD = currency_converter(curr, USD_to_yuan)
      print(f"{curr} USD -> {curr_USD}  Yuan's")

   #converting Yuan to USD
   print("\nConvert currensy in Yuan's to USD:")

   for curr in currency_in_yuan:
      curr_yuan = currency_converter(curr, yuan_to_USD)
      print(f"{curr} Yuan's -> {curr_yuan}  USD")
