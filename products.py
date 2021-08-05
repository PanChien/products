# 建立記帳程式專案(二維清單)
# while true適合使用在使用者不知道要輸人幾次時使用，可以重複的執行的情況

import os # operating system作業系統模組，

products = [] # 建立清單，存放使用者輸入的商品名，要放在最外圈
# 檢查檔案是否存在
if os.path.isfile('products.csv'): # os的模組裡path模組的isfile(檢查檔案的功能)
    print('yeah! 找到檔案了!')
    # 讀取檔案
    with open('products.csv', 'r', encoding='utf-8') as f:
        for line in f:
            if '商品,價格' in line:
                continue # 迴圈內的continue為跳到下一回的意思，當if為true時，進到if的內，遇到continue時，不向下執行下面的程式，再跳回for loop迴圈開頭
            # s = line.strip().split(',') # .split('X')字串的切割，括號內的字串意思為要用什麼東西作為切割的標準，切割完後的結果為清單
            # name = s[0] # 可以用這個方式分別取出分別存在name/price
            # price = s[1]
            name, price = line.strip().split(',') # 最簡單的作法，也能達到相同的效果，有幾個分隔點就要用幾個變數來裝
                                          # .strip()是把換行符號「\n」去除
                                          # line.strip().split(',')：line的字串，先執行strip()，再執行split()
            products.append([name,price]) # 再把他存入products這個大清單
    print(products)
else:
    print('找不到檔案!!')


# 使用者輸入購買的商品與價格
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


# 印出所有的商品與價格
for p in products: # 用for loop把products清單內的內容，一個一個印出來
    print(p[0]) # 印出products清單內的小清單第[0]的內容
    print(p[1]) # 印出products清單內的小清單第[1]的內容
    print(p[0], '的價格是', p[1])


# 寫入商品與價格到檔案內
with open('products.csv', 'w', encoding = 'utf-8') as f: # 'products.txt'為打開這個文件、'w'為寫入模式、encoding='utf-8'指字寫入時的文字編碼
    f.write('商品,價格\n') # 讓第一個欄位顯示為商品、價格
    for p in products:
        f.write(p[0] + ',' + str(p[1]) + '\n') # f.write(x)為把內容x寫入f內，str(p[1])把整數轉成字串