first_name = input("Ваше имя: ")
middle_name = input("Ваше отчество: ")
last_name = input("Ваша фамилия: ")
a = last_name + first_name + middle_name
for i in range(len(a)):
    print(a[i])
