#記帳程式(二維清單)

products = []
while True:
	name = input('請輸入商品名稱： ')
	if name == 'q':		#跳出while迴圈
		break
	price = input('請輸入商品價格： ')
	p = []
	p.append(name)
	p.append(price)
	# p = [name, price]
	products.append(p) 
	# products.append([name, price])
print(products)