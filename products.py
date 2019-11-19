products = []
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')
	products.append([name, price])
	# 其他第1種
	# p = []
	# p.append(name)
	# p.append(price)
	
	# 其他第2種
	#p = [name, price]
	#products.append(p)
	
print(products)

for p in products:
	print(p[0], '的價格是', p[1])
