# 2D list

import os # operating system

# 讀取檔案
def read_file(filename):
    products = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            if '商品,價格' in line:
                continue # 這次迴圈下面的程式碼跳過，從上面再重新執行一次。
            name, price = line.strip().split(',')
            products.append([name, price])
    return products

# 讓使用者輸入
def user_input(products):
    while True:
        name = input('Please input the product name: ')
        if name == 'q':
            break
        price = input('Please input the price: ')
        price = int(price)
        products.append([name, price])
    print(products)
    return products

# 印出所有購買紀錄
def print_products(products):
    for p in products:
        print(p[0], '的價格是', p[1])

# 寫入檔案
def write_file(filename, products):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write('商品, 價格\n')
        for p in products:
            f.write(p[0] + ',' + str(p[1]) + '\n')



def main():
    filename = 'products.csv'
    if os.path.isfile(filename):
        print('Yeah! Found it!')
        products = read_file(filename)
    else:
        print('Can not found file.')

    products = user_input(products)
    print_products(products)
    write_file(filename, products)

main()