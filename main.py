import hashlib
a = input("Якщо потрібно зашифрувати натисніть 1, якщо потрібно порівняти натисніть 2: ")
if a == '1' :
    data = input('Введіть текст: ')
    result = hashlib.md5(data.encode())
    output = (result.hexdigest())
    print("Ваш hash : "+ output)
if a == '2' :
    data= input('Введіть текст: ')
    hash = hashlib.md5(data.encode())
    hashhex = (hash.hexdigest())
    ihash = input('ВВедіть hash: ')
    if hashhex == ihash:
        print('Hash співпадає')
    else:
        print('Hash не співпадає')
