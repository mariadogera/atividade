nome = input("digite seu nome:")
#print("olá,", end=" ")
#print(nome)

 #aula de methods_string
 #nome = nome.title().strip()
 #print(f"olá, {nome.lower}")
 #print(f"olá, {nome.upper}")
 #print(f"olá, {nome.titler}")
 
 #".split"fatia" os espaços vazios
nome, sobrenome = nome.split()
#esse "nome+" + sobrenome" se chama contatenar
nome_completo = nome + " " + sobrenome

#".title" deixa em formato de texto: "ok, amigo" => "ok, amigo"
print(f"olá, {nome_completo.title()}")

