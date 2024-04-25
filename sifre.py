import random
karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

uzunluk = int(input("Şifreniz kaç karakterden oluşsun istiuorsunuz?"))
print(uzunluk)

password = ""
for i in range(uzunluk):
    password += random.choice(karakterler)
    
    
    
print("Sizin için oluşturduğum şifre:", password)

