#記帳程式(二維清單)
import os	#operating system

#讀取檔案
def read_file(filename):
	products = []
	with open(filename, 'r', encoding='utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue #繼續
			name, price = line.strip().split(',')
			'''
			s = line.strip().split(',')
			name = s[0]
			price = s[1]
			'''
			products.append([name, price])
	return products

	
#讓使用者輸入資料
def user_input(products):
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
	return products

#印出所有購買記錄
def print_products(products):
	for p in products:
		print(p[0], '的價格是', p[1])

#寫入檔案
def write_file(filename, products):
	with open(filename, 'w', encoding='utf-8') as f:
		f.write('商品,價格\n')
		for p in products:
			f.write(p[0] + ',' + str(p[1]) + '\n')  
			#字串不能跟整數作加減
			#str(p[1]) 將整數轉字串


def main():
	filename = 'products.csv'
	if os.path.isfile(filename):	#檢查檔案在不在
		print('Yeah!! 找到檔案。')
		products = read_file(filename)
	else:
		print('Oh no!!找不到檔案。')

	products = user_input(products)
	print_products(products)
	write_file(filename, products)

main()
