# 建立記帳程式專案(二維清單)
# while true適合使用在使用者不知道要輸人幾次時使用，可以重複的執行的情況

products = [] # 建立清單，存放使用者輸入的商品名
while True:
    name = input('請輸入商品名稱： ')
    if name == 'q': # 可以讓使用者跳出迴圈
        break
    price = input('請輸入商品價格： ')
    p = [] # 建立一個清單，裡面存放name,price
    p.append(name)  # 先存name
    p.append(price) # 再存price
    # 上面3行可以用這個來取代 p = [name, price]，結果是相同的
    products.append(p) # 再把這個小清單p，存入products這個大清單
print(products)

print(products[1][0]) # 清單的索引標韱(index)，第一個[1]是最外層的位置代號，第二個[0]是這裡面的小清單位置代號