# 2D list


products = []
while True:
    name = input('Please input the product name: ')
    if name == 'q':
        break
    price = input('Please input the price:')
    products.append([name, price])
print(products)

for p in products:
    print(p[0], '的價格是', p[1])


