#---------------------------------------------------------4 EJERCICIO ----------------------------------------------------------------------
print("--------------------------------------4 Ejercicio -------------------------------------------------")
#Descuento en el supermercado
#Un supermercado tiene una promoción especial: si una compra supera los $3500 entonces se aplica un descuento del 10% a la venta. 
#Por ejemplo, si un cliente realiza una compra por $3000, pagará $3000, pero si realiza una compra por $3600, entonces pagará $3240, 
#ya que tendrá un descuento del 10% (en este caso $360) sobre el total. Escribir un programa que permita ingresar 
#el monto de la compra e informe el importe final que deberá pagar el cliente, con o sin el descuento según corresponda.

monto_gastado = float(input("Ingrese el monto gastado: "))
if (monto_gastado > 3500):
    total_a_pagar = monto_gastado - (monto_gastado * 0.10)
    print(f"El total a pagar es: ${total_a_pagar}")
else:
    print(f"El total a pagar es: ${monto_gastado}")