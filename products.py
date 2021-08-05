# 建立記帳程式專案(二維清單)
# while true適合使用在使用者不知道要輸人幾次時使用，可以重複的執行的情況

products = [] # 建立清單，存放使用者輸入的商品名
while True:
    name = input('請輸入商品名稱： ')
    if name == 'q': # 可以讓使用者跳出迴圈
        break
    price = input('請輸入商品價格： ')
    price = int(price)
    p = [] # 建立一個清單，裡面存放name,price
    p.append(name)  # 先存name
    p.append(price) # 再存price
    # 上面3行可以用這個來取代 p = [name, price]，結果是相同的
    # 更簡潔的寫法，直接把下方的p放為[name, price]結果也是相同
    products.append(p) # 再把這個小清單p，存入products這個大清單
print(products)
# print(products[1][0]) # 清單的索引標韱(index)，第一個[1]是最外層的位置代號，第二個[0]是這裡面的小清單位置代號


for p in products: # 用for loop把products清單內的內容，一個一個印出來
    print(p[0]) # 印出products清單內的小清單第[0]的內容
    print(p[1]) # 印出products清單內的小清單第[1]的內容
    print(p[0], '的價格是', p[1])


with open('prodcuts.csv', 'w', encoding = 'utf-8') as f: # 'prodcuts.txt'為打開這個文件、'w'為寫入模式、encoding='utf-8'指字寫入時的文字編碼
    f.write('商品,價格\n') # 讓第一個欄位顯示為商品、價格
    for p in products:
        f.write(p[0] + ',' + str(p[1]) + '\n') # f.write(x)為把內容x寫入f內，str(p[1])把整數轉成字串