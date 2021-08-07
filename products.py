# 建立記帳程式專案(二維清單)
# while true適合使用在使用者不知道要輸人幾次時使用，可以重複的執行的情況
# refactor 重構
import os # operating system作業系統模組


# 讀取檔案
def read_file(filename):
    products = [] # 建立清單，存放使用者輸入的商品名，要放在最外圈
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            if '商品,價格' in line:
                continue # 迴圈內的continue為跳到下一回的意思，當if為true時，進到if的內，遇到continue時，不向下執行下面的程式，再跳回for loop迴圈開頭
            name, price = line.strip().split(',') # line.strip().split(',')：line的字串，先執行strip()把換行符號「\n」去除，再執行split()進行切割
            products.append([name,price]) # 再把他存入products這個大清單
    return products


# 使用者輸入購買的商品與價格
def user_input(products):
    while True:
        name = input('請輸入商品名稱： ')
        if name == 'q': # 可以讓使用者跳出迴圈
            break
        price = input('請輸入商品價格： ')
        price = int(price)
        products.append([name, price]) # 再把這個小清單p，存入products這個大清單
    print(products)
    return products


# 印出所有的商品與價格
def print_products(products):
    for p in products: # 用for loop把products清單內的內容，一個一個印出來
        print(p[0], '的價格是', p[1])


# 寫入商品與價格到檔案內
def write_file(filename, products):
    with open(filename, 'w', encoding = 'utf-8') as f: # 'products.csv'為打開這個文件、'w'為寫入模式、encoding='utf-8'指字寫入時的文字編碼
        f.write('商品,價格\n') # 讓第一個欄位顯示為商品、價格
        for p in products:
            f.write(p[0] + ',' + str(p[1]) + '\n') # f.write(x)為把內容x寫入f內，str(p[1])把整數轉成字串


def main(): # 主要的程式進入點(真正的執行程式)
    filename = 'products.csv'
    if os.path.isfile(filename): # 檢查檔案在不在
        print('yeah! 找到檔案了!')
        products = read_file(filename)
    else:
        print('找不到檔案....')

    products = user_input(products)
    print_products(products)
    write_file(filename, products)

main()