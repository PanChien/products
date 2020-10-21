#記帳程式(二維清單)

products = []
while True:
	name = input('請輸入商品名稱： ')
	if name == 'q':		#跳出while迴圈
		break
	price = input('請輸入商品價格： ')
	price = int(price)
	# p = []
	# p.append(name)
	# p.append(price)
	# p = [name, price]
	# products.append(p) 
	products.append([name, price])
print(products)

for p in products:
	print(p[0], '的價格是', p[1])

with open('products.csv', 'w', encoding='utf-8') as f:
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')  
		#字串不能跟整數作加減
		#str(p[1]) 將整數轉字串

