
alphabets="abcdefghijklmnopqrstuvwxyz" #veri yığınını tanımlıyoruz.
message = "helloworld"
encrypt,decrypt="","" # şifreleme ve şifre çözme verisini kaydetmek için boş dizin açıyoruz.
key=5 #key değerimizi veriyoruz

for letter in message:
    new_position=(alphabets.find(letter)+key)%len(alphabets) #veri yığınımızın üzerine keyi ekleyip sonra verinin uzunluğunun modu alınıyor.
    encrypt+=alphabets[new_position]

for letter in encrypt:
    new_position=(alphabets.find(letter)-key)%len(alphabets)#veri yığınımızın üzerine keyi çıkartıp sonra verinin uzunluğunun modu alınıyor.
    decrypt+=alphabets[new_position]


print("Encrypted message:",encrypt)
print("Decrypted message:",decrypt)