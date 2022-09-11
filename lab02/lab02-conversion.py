# Tendencias e Innovacion en Tecnologia Agricola (TEA)
minutos = input("minutos jugados? ")
valorporminuto = input("valor por minuto? ")

# se utiliza la conversion de tipo a int 
# sino se hace la conversion existiria error porque trata de multiplicar strings 
# calculando el valor total de las minutos jugados 
total = int(minutos) * int(valorporminuto)