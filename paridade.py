#challenge
#min() tem a responsabilidade de interação com o usr
def min():
   num = int(input("digite o número"))
   if eh_par(num):
       print("é par")
   else:
       print("é impar")    


# eh_par(num) tem a responsabilidade de verificar se o numero é par
def eh_par(num):
    #PROCESSAMENTO: verificar se o número é par
    if num % 2 == 0:
        return True
    else:
        return False
    

