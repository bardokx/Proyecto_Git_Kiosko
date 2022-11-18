#accionador del codigo
Click = True
#ejemplo de fila
fila = ["Pedro_master_69", "Ramon_Piñera", "Juan_destroyer"]
#ejemplo de numerador de fila(variable)
ticket_number = 1
#ejemplo de limite de clientes de la tienda
customer_limit = 5

if Click == True and len(fila) <= customer_limit:
    user = input("Nombre de usuario: ")
    if user not in fila:
        fila += [user]

position = (fila.index(user)+1)

def numero_de_fila(request):
    return position