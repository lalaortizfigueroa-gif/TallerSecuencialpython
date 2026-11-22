# Algoritmo Valor E Intereses

dinero = (input("Ingrese el dinero: "))
dias = (input("Ingrese el Días: "))
porcen = (input("Ingrese el Porcen: "))

valorIntereses = (dinero * porcen * dias) / 100
impuestos = valorIntereses * 0.07
pagar = dinero + valorIntereses - impuestos

print("El pago es:", pagar)
print("El impuesto es:", impuestos)
print("El porcentaje de intereses es:", valorIntereses)