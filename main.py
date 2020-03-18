from invoice import Invoice

products = {}
total_amount = 0
repeat = ''
while True:
    product = input('What is your product : ')
    unit_price = Invoice().inputNumber('Please enter unit price : ')
    qnt = Invoice().inputNumber('Please enter quantity : ')
    discount = Invoice().inputNumber('Please enter discount % : ')
    repeat = Invoice().inputAnswer('Another product? y,n : ')
    result = Invoice().addProduct(qnt, unit_price, discount)
    products[product] = result
    if repeat == 'n':
        break

total_amount = Invoice().totalPurePrice(products)

print("Your total pure price is: ", total_amount)