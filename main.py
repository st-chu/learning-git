print()
shopping_list = {
    'piekarnia' : ['chleb', 'bułka', 'pączek'],
    'warzywniak' : ['marchew', 'seler', 'rukola']
}
number_off_products = 0


for shop, products in shopping_list.items():
    number_off_products += len(products)
    shop = shop.capitalize()
    for i in range(len(products)):
        products[i] = products[i].capitalize()
    print(f'Idę do {shop} i kupuję tam : {products}.')
    

print(f'W sumie kupuję {number_off_products} produktów')


for s, p in shopping_list.items():
    #s = s.capitalaze()
    print(s.capitalize())
print('*' * 20)
print()
