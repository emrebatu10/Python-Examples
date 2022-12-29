"""
i = 0
# WHİLE DÖNGÜSÜ

while i < 10:
    print("i'nin değeri :",i)
    i += 1


while i < 10:
    if i ==5:
        break
    print("i :",i)
    i += 1

# FOR DÖNGÜSÜ


liste = [1,2,3,4,5]
kelime = "python"

for a in liste:
    print(a)

for a in kelime:
    print(a)
"""
# RANGE

for i in range(0,20):  # 0'dan başla ve 20 ye kadar giden bir liste oluşturur.
    print(i)

for i in range(0,20,2): # 0'dan başla ve 20 ye kadar 2 'şer atlayarak giden bir liste oluşturur.
    print(i)


