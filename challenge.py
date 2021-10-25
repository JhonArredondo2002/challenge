from tkinter import *
from tkinter import messagebox
import sqlite3
import random

def crear():
	try:
		conexion=sqlite3.connect("USUARIOS")
		varcursor=conexion.cursor()
		
		varcursor.execute('''CREATE TABLE INFOUSERS (NOMBRE VARCHAR(20) PRIMARY KEY,
			PUNTAJE VARCHAR(4),
			FECHA_INI TEXT,
			FECHA_FIN TEXT)''')

		varcursor.execute("INSERT INTO INFOUSERS VALUES ('"+jugador.get().lower()+"',0,datetime('now','localtime'),NULL)")	
		conexion.commit()

		varcursor.execute("SELECT*FROM INFOUSERS WHERE NOMBRE='"+ jugador.get().lower()+"'")
		list_pun=varcursor.fetchall()

		for lista_punt in list_pun:
			global b
			b=lista_punt[0]
			a=lista_punt[1]	

		
		messagebox.showinfo("REGISTRO","El usuario ha sido creado")

	except:
		conexion=sqlite3.connect("USUARIOS")
		varcursor=conexion.cursor()
		try:
			varcursor.execute("INSERT INTO INFOUSERS VALUES ('"+jugador.get().lower()+"',0,datetime('now','localtime'),NULL)")	
			conexion.commit()

			varcursor.execute("SELECT*FROM INFOUSERS WHERE NOMBRE='"+ jugador.get().lower()+"'")
			list_pun=varcursor.fetchall()

			for lista_punt in list_pun:
				b=lista_punt[0]
				a=lista_punt[1]	

			messagebox.showinfo("REGISTRO","El usuario ha sido creado")

		except:
			varcursor.execute("UPDATE INFOUSERS SET FECHA_INI=datetime('now','localtime') WHERE NOMBRE='"+jugador.get()+"'")
			conexion.commit()

			varcursor.execute("SELECT*FROM INFOUSERS WHERE NOMBRE='"+ jugador.get().lower()+"'")
			list_pun=varcursor.fetchall()

			for lista_punt in list_pun:
				b=lista_punt[0]
				a=lista_punt[1]

			messagebox.showwarning("SELECCION","El usuario ha sido seleccionado\nSu record es "+str(a))

	frame1.destroy()
	frame2.pack()	

def salir():
	
	valor=messagebox.askquestion("SALIR","¿Desea salir de la aplicacion?")

	if valor=="yes":
		conexion=sqlite3.connect("USUARIOS")
		varcursor=conexion.cursor()

		varcursor.execute("UPDATE INFOUSERS SET PUNTAJE='"+str(puntaje)+"',FECHA_FIN=datetime('now','localtime') WHERE NOMBRE='"+b+"'")
		conexion.commit()
		root.destroy()

def info():
	messagebox.showinfo("Acerca de...","Autor: Jhon Arredondo\nDesarrollado en Python\nCorreo de contacto:jhonarredondo15@gmail.com")
        
#------------Ventana 1-------------
root=Tk()
root.title("Juego de preguntas")
root.iconbitmap("interrogacion.ico")
root.eval('tk::PlaceWindow . center')
bm=Menu(root)
root.config(menu=bm)

menu1=Menu(bm,tearoff=0)
menu1.add_command(label="Salir",command=salir)

menu2=Menu(bm,tearoff=0)
menu2.add_command(label="Acerca de...",command=info)

bm.add_cascade(label="Info",menu=menu2)
bm.add_cascade(label="Salir",menu=menu1)


frame1=Frame(root)
frame1.pack()

global puntaje
jugador=StringVar()
puntaj_fin=StringVar()
puntaje=0

cuadroid=Entry(frame1,textvariable=jugador)
cuadroid.grid(row=0,column=1,pady=10,padx=10)
etiquetaid=Label(frame1,text="Ingrese su nombre")
etiquetaid.grid(row=0,column=0,pady=10,padx=10)
butcrear=Button(frame1,text="Iniciar",command=crear)
butcrear.grid(row=1,column=0,pady=10,padx=10,columnspan=2)


#------------Preguntas-------------

historia=["¿Cuánto duró la Guerra de los Cien Años?",
			"¿Quién fue el primer presidente de Estados Unidos?",
			"¿En qué año el hombre pisó la Luna por primera vez?",
			"¿Qué carabela no volvió del viaje en el que Colón arribó a América por primera vez?",
			"¿Quién fue el primer presidente de la democracia española tras el franquismo?"]

geografia=["¿Cuál es el monte más alto del mundo?",
			"¿Cuál es la capital de Brasil?",
			"¿Cuál es la capital de Nueva Zelanda?",
			"¿Cuál es la capital de Letonia?",
			"¿Cuál es la lengua más hablada del mundo?"]

entretenimiento=["¿Quién fue el famoso cantante del grupo musical Queen?",
				"¿Cómo se llama la madre de Simba en la película de Disney “El Rey León”?",
				"¿Cómo se llama la ciudad donde se encuentra el Mago de Oz?",
				" ¿Cómo se llama la protagonista de la saga de videojuegos The Legend of Zelda?",
				"¿A qué saga de películas pertenece el personaje conocido como Jack Sparrow?"]

deportes=[" ¿Quién es considerado el mejor jugador de baloncesto de todos los tiempos?",
			" ¿Cada cuántos años se celebran los Juegos Olímpicos?",
		    " ¿Qué equipo de fútbol ha ganado más Mundiales hasta el momento?",
			"¿Cuándo se celebró la primera Copa Mundial de Fútbol?",
		  " ¿Qué atleta tiene el record plusmarca de velocidad en los 100 metros lisos?"]	

ciencia=[" ¿Cuál es la velocidad de la luz?",
		"¿Cuál es el nombre técnico del miedo o fobia a las alturas?",
		"¿Por qué fue famosa Marie Curie?",
		"¿Cómo se llama la planta a partir de la cual suele ser elaborado el tequila?",
		"¿Cuáles una de las bases nitrogenadas del ADN?"]

#-----------------Funciones-----------------------
global n1
n1=["¿Cuánto duró la Guerra de los Cien Años?",
"¿Cuál es el monte más alto del mundo?",
"¿Quién fue el famoso cantante del grupo musical Queen?",
"¿Quién es considerado el mejor jugador de baloncesto de todos los tiempos?",
"¿Cuál es la velocidad de la luz?"]

global n2
n2=["¿Quién fue el primer presidente de Estados Unidos?",
"¿Cuál es la capital de Brasil?",
"¿Cómo se llama la madre de Simba en la película de Disney “El Rey León”?",
" ¿Cada cuántos años se celebran los Juegos Olímpicos?",
"¿Cuál es el nombre técnico del miedo o fobia a las alturas?"]

global n3
n3=["¿En qué año el hombre pisó la Luna por primera vez?",
"¿Cuál es la capital de Nueva Zelanda?",
"¿Cómo se llama la ciudad donde se encuentra el Mago de Oz?",
" ¿Qué equipo de fútbol ha ganado más Mundiales hasta el momento?",
"¿Por qué fue famosa Marie Curie?"]

global n4
n4=["¿Qué carabela no volvió del viaje en el que Colón arribó a América por primera vez?",
"¿Cuál es la capital de Letonia?",
" ¿Cómo se llama el protagonista de la saga de videojuegos The Legend of Zelda?",
"¿Cuándo se celebró la primera Copa Mundial de Fútbol?",
"¿Cómo se llama la planta a partir de la cual suele ser elaborado el tequila?"]

global n5
n5=["¿Quién fue el primer presidente de la democracia española tras el franquismo?",
"¿Cuál es la lengua más hablada del mundo?",
"¿A qué saga de películas pertenece el personaje conocido como Jack Sparrow?",
" ¿Qué atleta tiene el record plusmarca de velocidad en los 100 metros lisos?",
"¿Cuáles una de las bases nitrogenadas del ADN?"]


def enunciado():
	global enun
	enun=""	
	if (len(n1)-1)!=0:
		enun=n1[random.randint(0,(len(n1)-1))]
	elif (len(n2)-1)!=0:
			enun=n1[random.randint(0,(len(n1)-1))]	
	elif (len(n3)-1)!=0:
		enun=n3[random.randint(0,(len(n1)-1))]
	elif (len(n4)-1)!=0:
		enun=n4[random.randint(0,(len(n1)-1))]
	else:
		enun=n5[random.randint(0,(len(n1)-1))]						
	return enun
	

def respuestasn1():
	global resp
	
	if text_preg=="¿Cuánto duró la Guerra de los Cien Años?":
		resp=["116","100","90","102"]
		return resp[0]
	elif text_preg=="¿Cuál es el monte más alto del mundo?":
		resp=["K2","Kanchenjunga","Everest","Makalu"]
		return resp[2]	
	elif text_preg=="¿Quién fue el famoso cantante del grupo musical Queen?":
		resp=["John Deacon","Freddie Mercury","Brian May","Roger Taylor"]
		return resp[1]
	elif text_preg=="¿Quién es considerado el mejor jugador de baloncesto de todos los tiempos?":
		resp=["Damian Lillard ","Michael Jordan","Devin Booker","Kawhi Leonard"]
		return resp[1]
	else:
		resp=["300.000.000 ","400.000.000","200.000.000","500.000.000"]
		return resp[0]

def respuestasn2():
	global resp
	
	if text_preg=="¿Quién fue el primer presidente de Estados Unidos?":
		resp=["George Washington","John Adams","Thomas Jefferson","James Monroe"]
		return resp[0]
	elif text_preg=="¿Cuál es la capital de Brasil?":
		resp=["Brasil","São Paulo","Brasilia","Río de Janeiro"]
		return resp[2]	
	elif text_preg=="¿Cómo se llama la madre de Simba en la película de Disney “El Rey León”?":
		resp=["Nala","Sarabi","Zazú","Shenzi"]
		return resp[1]
	elif text_preg==" ¿Cada cuántos años se celebran los Juegos Olímpicos?":
		resp=["5 ","4","3","2"]
		return resp[1]
	else:
		resp=["acrofobia ","vertigo","panico","vuelofobia"]
		return resp[0]		

def respuestasn3():
	global resp
	
	if text_preg=="¿En qué año el hombre pisó la Luna por primera vez?":
		resp=["1969 ","1942","1988","1977"]	
		return resp[0]
	elif text_preg=="¿Cuál es la capital de Nueva Zelanda?":
		resp=["Wellington ","Christchurch ","Auckland","Dunedin"]
		return resp[2]	
	elif text_preg=="¿Cómo se llama la ciudad donde se encuentra el Mago de Oz?":
		resp=["Rubi","Esmeralda","Zafiro","Perla"]
		return resp[1]
	elif text_preg==" ¿Qué equipo de fútbol ha ganado más Mundiales hasta el momento?":
		resp=["Alemania  ","Brasil ","Italia ","Argentina"]
		return resp[1]
	else:
		resp=["Descubrio la radiactividad ","Gano 3 premios nobel","Invento la bateria",
		"Invento el computador"]
		return resp[0]

def respuestasn4():
	global resp
	
	if text_preg=="¿Qué carabela no volvió del viaje en el que Colón arribó a América por primera vez?":
		resp=["Santa María ","La Pinta","la Niña","El Venganza"]	
		return resp[0]
	elif text_preg=="¿Cuál es la capital de Letonia?":
		resp=["Ventspils  ","Liepāja  ","Riga ","Valmiera"]
		return resp[2]	
	elif text_preg==" ¿Cómo se llama el protagonista de la saga de videojuegos The Legend of Zelda?":
		resp=["Zelda","Link","Epona","Navi"]
		return resp[1]
	elif text_preg=="¿Cuándo se celebró la primera Copa Mundial de Fútbol?":
		resp=["1945  ","1930 ","1932 ","1920"]
		return resp[1]
	else:
		resp=["agave ","Lithops","Fo-ti","Diente sangrante"]
		return resp[0]	

def respuestasn5():
	global resp
	
	if text_preg=="¿Quién fue el primer presidente de la democracia española tras el franquismo?":
		resp=["Adolfo Suárez ","Francisco Franco","Luis Carrero Blanco","Rey Juan"]	
		return resp[0]
	elif text_preg=="¿Cuál es la lengua más hablada del mundo?":
		resp=["ingles ","español ","mandarín","portugues"]
		return resp[2]	
	elif text_preg=="¿A qué saga de películas pertenece el personaje conocido como Jack Sparrow?":
		resp=["Harry Potter","Piratas del Caribe","Señor de los anillos","Star wars"]
		return resp[1]
	elif text_preg==" ¿Qué atleta tiene el record plusmarca de velocidad en los 100 metros lisos?":
		resp=["Mo Farah  ","Usain Bolt ","Michael Phelps ","Katie Ledecky"]
		return resp[1]
	else:
		resp=["guanina ","Flavina","Uracilo","Gene"]
		return resp[0]			


#------------Ventana 2-------------
frame2=Frame(root)
frame2.config(width=650,height=350)
	
global respues
global text_preg
global num
global alea
text_preg=enunciado()
respues=respuestasn1()
alea=[0,1,2,3]
num=random.randint(0,(len(alea)-1))



etiqueta_puntaje=Label(frame2,text="Puntaje: ")
etiqueta_puntaje.grid(row=0,column=0,pady=10,padx=10)
etiqueta_puntaje2=Label(frame2,text=puntaje)
etiqueta_puntaje2.grid(row=0,column=1,pady=10,padx=5)

etiqueta_nivel=Label(frame2,text="Nivel 1, valor de puntos=1")
etiqueta_nivel.grid(row=0,column=2,pady=10,padx=5)

enun_pregu=Label(frame2,text=text_preg)
enun_pregu.grid(row=1,column=0,pady=10,padx=10,columnspan=4)




#-------------------Funciones-----------------------
def correcto1():
	global respues	
	global enun
	global text_preg
	global num
	global alea
	global puntaje
	
	alea=[0,1,2,3]
	num=random.randint(0,(len(alea)-1))
	
	if (len(n1)-1)!=0:
		puntaje+=1
		etiqueta_puntaje2.config(text=puntaje)
		n1.remove(enun)
		enun=n1[random.randint(0,(len(n1)-1))]
		enun_pregu.config(text=enun)
		text_preg=enun

		respues=respuestasn1()
	
	
		b1.config(text=respues)
		b1.grid(row=2,column=alea[num],pady=10,padx=10,)

		posicion()

		b2.config(text=respues)
		b2.grid(row=2,column=alea[num],pady=10,padx=10,)

		posicion()

		b3.config(text=respues)
		b3.grid(row=2,column=alea[num],pady=10,padx=10,)

		posicion()

		b4.config(text=respues)
		b4.grid(row=2,column=alea[num],pady=10,padx=10,)
		
	elif(len(n2)-1)!=0:
		if puntaje<=4:
			messagebox.showinfo("Felicidades","Siguiente nivel")
			puntaje+=2
			etiqueta_puntaje2.config(text=puntaje)
			etiqueta_nivel.config(text="Nivel 2, valor de puntos 2")
			enun=n2[random.randint(0,(len(n1)-1))]
			enun_pregu.config(text=enun)
			text_preg=enun

			respues=respuestasn2()

	
			b1.config(text=respues)
			b1.grid(row=2,column=alea[num],pady=10,padx=10,)

			posicion()

			b2.config(text=respues)
			b2.grid(row=2,column=alea[num],pady=10,padx=10,)

			posicion()

			b3.config(text=respues)
			b3.grid(row=2,column=alea[num],pady=10,padx=10,)

			posicion()

			b4.config(text=respues)
			b4.grid(row=2,column=alea[num],pady=10,padx=10,)

		else:
			puntaje+=2
			etiqueta_puntaje2.config(text=puntaje)
			n2.remove(enun)
			enun=n2[random.randint(0,(len(n1)-1))]
			enun_pregu.config(text=enun)
			text_preg=enun

			respues=respuestasn2()
	
	
			b1.config(text=respues)
			b1.grid(row=2,column=alea[num],pady=10,padx=10,)

			posicion()

			b2.config(text=respues)
			b2.grid(row=2,column=alea[num],pady=10,padx=10,)

			posicion()

			b3.config(text=respues)
			b3.grid(row=2,column=alea[num],pady=10,padx=10,)

			posicion()

			b4.config(text=respues)
			b4.grid(row=2,column=alea[num],pady=10,padx=10,)
	elif(len(n3)-1)!=0:
		if puntaje<=16:
			messagebox.showinfo("Felicidades","Siguiente nivel")
			puntaje+=3
			etiqueta_puntaje2.config(text=puntaje)
			etiqueta_nivel.config(text="Nivel 3, valor de puntos 3")
			enun=n3[random.randint(0,(len(n1)-1))]
			enun_pregu.config(text=enun)
			text_preg=enun

			respues=respuestasn3()

	
			b1.config(text=respues)
			b1.grid(row=2,column=alea[num],pady=10,padx=10,)

			posicion()

			b2.config(text=respues)
			b2.grid(row=2,column=alea[num],pady=10,padx=10,)

			posicion()

			b3.config(text=respues)
			b3.grid(row=2,column=alea[num],pady=10,padx=10,)

			posicion()

			b4.config(text=respues)
			b4.grid(row=2,column=alea[num],pady=10,padx=10,)

		else:
			puntaje+=3
			etiqueta_puntaje2.config(text=puntaje)
			n3.remove(enun)
			enun=n3[random.randint(0,(len(n1)-1))]
			enun_pregu.config(text=enun)
			text_preg=enun

			respues=respuestasn3()
	
	
			b1.config(text=respues)
			b1.grid(row=2,column=alea[num],pady=10,padx=10,)

			posicion()

			b2.config(text=respues)
			b2.grid(row=2,column=alea[num],pady=10,padx=10,)

			posicion()

			b3.config(text=respues)
			b3.grid(row=2,column=alea[num],pady=10,padx=10,)

			posicion()

			b4.config(text=respues)
			b4.grid(row=2,column=alea[num],pady=10,padx=10,)
	elif(len(n4)-1)!=0:
		if puntaje<=29:
			messagebox.showinfo("Felicidades","Siguiente nivel")
			puntaje+=4
			etiqueta_puntaje2.config(text=puntaje)
			etiqueta_nivel.config(text="Nivel 4, valor de puntos 4")
			enun=n4[random.randint(0,(len(n1)-1))]
			enun_pregu.config(text=enun)
			text_preg=enun

			respues=respuestasn4()

	
			b1.config(text=respues)
			b1.grid(row=2,column=alea[num],pady=10,padx=10,)

			posicion()

			b2.config(text=respues)
			b2.grid(row=2,column=alea[num],pady=10,padx=10,)

			posicion()

			b3.config(text=respues)
			b3.grid(row=2,column=alea[num],pady=10,padx=10,)

			posicion()

			b4.config(text=respues)
			b4.grid(row=2,column=alea[num],pady=10,padx=10,)

		else:
			puntaje+=4
			etiqueta_puntaje2.config(text=puntaje)
			n4.remove(enun)
			enun=n4[random.randint(0,(len(n1)-1))]
			enun_pregu.config(text=enun)
			text_preg=enun

			respues=respuestasn4()
	
	
			b1.config(text=respues)
			b1.grid(row=2,column=alea[num],pady=10,padx=10,)

			posicion()

			b2.config(text=respues)
			b2.grid(row=2,column=alea[num],pady=10,padx=10,)

			posicion()

			b3.config(text=respues)
			b3.grid(row=2,column=alea[num],pady=10,padx=10,)

			posicion()

			b4.config(text=respues)
			b4.grid(row=2,column=alea[num],pady=10,padx=10,)
	elif(len(n5)-1)!=0:
		if puntaje<=49:
			messagebox.showinfo("Felicidades","Siguiente nivel")
			puntaje+=5
			etiqueta_puntaje2.config(text=puntaje)
			etiqueta_nivel.config(text="Ultimo Nivel, valor de puntos 5")
			enun=n5[random.randint(0,(len(n1)-1))]
			enun_pregu.config(text=enun)
			text_preg=enun

			respues=respuestasn5()

	
			b1.config(text=respues)
			b1.grid(row=2,column=alea[num],pady=10,padx=10,)

			posicion()

			b2.config(text=respues)
			b2.grid(row=2,column=alea[num],pady=10,padx=10,)

			posicion()

			b3.config(text=respues)
			b3.grid(row=2,column=alea[num],pady=10,padx=10,)

			posicion()

			b4.config(text=respues)
			b4.grid(row=2,column=alea[num],pady=10,padx=10,)

		else:
			puntaje+=5
			etiqueta_puntaje2.config(text=puntaje)
			n5.remove(enun)
			enun=n5[random.randint(0,(len(n1)-1))]
			enun_pregu.config(text=enun)
			text_preg=enun

			respues=respuestasn5()
	
	
			b1.config(text=respues)
			b1.grid(row=2,column=alea[num],pady=10,padx=10,)

			posicion()

			b2.config(text=respues)
			b2.grid(row=2,column=alea[num],pady=10,padx=10,)

			posicion()

			b3.config(text=respues)
			b3.grid(row=2,column=alea[num],pady=10,padx=10,)

			posicion()

			b4.config(text=respues)
			b4.grid(row=2,column=alea[num],pady=10,padx=10,)
	else:
		conexion=sqlite3.connect("USUARIOS")
		varcursor=conexion.cursor()

		varcursor.execute("UPDATE INFOUSERS SET PUNTAJE='"+str(puntaje)+"',FECHA_FIN=datetime('now','localtime') WHERE NOMBRE='"+b+"'")
		conexion.commit()
		messagebox.showinfo("Felicidades","Has completado el juego\nTu puntaje final fue"+str(puntaje))
		root.destroy()

def posicion():
	global num
	global respues
	global alea

	if (len(alea)-1)==0:
		alea=[0,1,2,3]

	alea.remove(alea[num])
	num=random.randint(0,(len(alea)-1))

	resp.remove(respues)
	respues=resp[random.randint(0,(len(resp)-1))]

def error():
	conexion=sqlite3.connect("USUARIOS")
	varcursor=conexion.cursor()

	varcursor.execute("UPDATE INFOUSERS SET PUNTAJE='"+str(puntaje)+"',FECHA_FIN=datetime('now','localtime') WHERE NOMBRE='"+b+"'")
	conexion.commit()
	messagebox.showinfo("Perdiste","Respuesta incorrecta\nTu puntaje final fue de "+str(puntaje))
	root.destroy()

#-------------------Botones respuesta----------------

b1=Button(frame2,text=respues,command=correcto1)
b1.grid(row=2,column=alea[num],pady=10,padx=10,)

posicion()

b2=Button(frame2,text=respues,command=error)
b2.grid(row=2,column=alea[num],pady=10,padx=10,)

posicion()

b3=Button(frame2,text=respues,command=error)
b3.grid(row=2,column=alea[num],pady=10,padx=10,)

posicion()

b4=Button(frame2,text=respues,command=error)
b4.grid(row=2,column=alea[num],pady=10,padx=10,)




root.mainloop()





