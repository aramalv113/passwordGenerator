import string
import random

def preguntar (frase, tabla):
    while True:
        
        r = input(frase + " s/n: ")
        
        if (r=='s'):
            return tabla
        elif (r=='n'):
            return ''
        else:
            print("Por favor, responde sí (s) o no (n) únicamente.")
            continue

def caracteres ():
    aux = ""
    aux += preguntar("Mayusculas?", string.ascii_uppercase)  
    aux += preguntar("Minusculas?", string.ascii_lowercase)           
    aux += preguntar("Digitos?", string.digits)                     
    aux += preguntar("Símbolos de puntuación?", string.punctuation)
    
    return aux

def generator (dimension, abc):
    aux = random.choices(abc, k=dimension)
    
    passw = "" .join(aux)
    
    return passw

if __name__ == "__main__":
    abc = ""

    while True:
        try:     
            dim_pass = int(input("Longitud de contraseña: "))
            
            if dim_pass <= 0:
                print ("\nPor favor, introduce una cantidad mayor a 0.\n")
                continue
            
            abc = caracteres()
            
            if abc=="":
                print("\n\nVAS A QUERER ALGO? ._. \n\n")
                continue
            
            passw = generator(dim_pass, abc)
            
        except ValueError:
            print("El dato introducido no es numérico.")
            continue
        
        if dim_pass>0:
            break
        
    print("\nTu contraseña es: ", passw)