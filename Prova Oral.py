def password_maiuscula (pwd):
    for i in pwd:
        if i.isupper():
            return True
    else:
        return False

pwd=input("Digite sua senha: ")
password_maiuscula(pwd)
print(password_maiuscula(pwd))