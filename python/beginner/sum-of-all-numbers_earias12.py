def lee_entero():
    while True:
        entrada=int(input("escribe tu primer num. entero:"))
        try: 
            entrada= int(entrada)
            return entrada
        except ValueError:
            print ("la entrada es incorrecta: inserte un numero entero")
                
def lee_entero2():
    while True:
        entrada2=int(input("escribe tu 2do num. entero:"))
        try:
            entrada2 = int(entrada2)
            return entrada2
        except ValueError:
            print ("La entrada es incorrecta: inserte un numero entero")

def sum_all(n1,n2):
    aux=0
    if n1>=n2:
        aux = n2
        n2 = n1
        n1 = aux
    
    acum = 0
    i = n1
    while i<=n2:
        acum = acum +i
        i=i+1
    
    if n1==n2 :
        acum =n1+n2
    
    return(str(acum))




num1 = lee_entero()
num2 = lee_entero2()
print (sum_all(num1,num2))
input ("enter pa terminar")
