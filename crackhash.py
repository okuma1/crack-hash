import crypt


print("Hashcrack~v1")
print("OBS: Ferramenta que possivelmente irie atualizar futuramente")
print("=="*30)
print("=="*10, "Hashcrack~v1", "=="*13)
print("=="*30)

i = input("Deseja pesquisar por quantidade de caracteres?(s/n): ").upper()


if i == "S":
    qtd_i = float(input("Caracteres: "))
    hash = input("hash:")
    list = str(input("Wordlist:"))
    file = open(list, 'r')
    
    for senhas in file:
        if len(senhas) == qtd_i+1:
            c = crypt.crypt(senhas[:-1], hash)
            if c == hash:
                print("\nSenha: {}".format(senhas))
else:
    hash = input("hash:")
    list = str(input("Wordlist:"))
    file = open(list, 'r')
    for senhas in file:
        c = crypt.crypt(senhas[:-1], hash)
        if c == hash:
            print("\nSenha: {}".format(senhas))