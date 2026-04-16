#gerador de senha!
import random
import string

for i in range(1):
    password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=12))
    print(f"senha gerada: {password}")
    while True:
        resposta= input("deseja gerar outras senhas s/n?")
        if resposta.lower() == 's':
            password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=12))
            print(f"senha gerada: {password}")
        elif resposta.lower() == 'n':
            print("obrigado por usar o gerador de senhas!")
            break
        else:
            print("resposta invalida tente novamente!")
            break


        
            
        