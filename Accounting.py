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

with open('products.csv', 'w', encoding='utf-8') as f:
    f.write('商品, 價格\n')
    for p in products:
        f.write(p[0] + ',' + p[1] + '\n')

