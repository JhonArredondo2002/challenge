numero=0
while numero<=10:
	print(f"El numero es {numero}")
	numero=numero+1

print("fin")

#while con or
'''numero=int(input("Digite un numero "))

while numero<0 or numero>100:
	print("error")
	numero=int(input("Digite un numero "))

print("fin")'''	

#finalizar bucle

numero=int(input("Digite un numero "))
intentos=0
while numero<0 or numero>100:
	if numero<0 or numero>100:
		print("error")
		numero=int(input("Digite un numero "))
		intentos=intentos+1
		print(intentos)

	if intentos==1:
		print("fin del programa")
		break;
#continue

'''for letra in "python":
	if letra=="h":
		continue
	print("la letra es "+letra)'''

#pass
for letra in "python":
	pass

#else
for letra in "python":
	if letra=="h":
		continue
	print("la letra es "+letra)	
else:
	print("la letra final es "+letra)
	
#bucle infinito
'''while True:
	print(1+1)'''	
			