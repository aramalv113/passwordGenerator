import string
import random

abc = string.ascii_letters + string.digits + string.punctuation

while True:
    try:
        dim_pass = int(input("Longitud de contraseña: "));
        
    except ValueError:
        print("El dato introducido no es numérico.")
        continue
    
    if dim_pass>0:
        break

passw = random.choices(abc, k=dim_pass)
print ("" .join(passw))