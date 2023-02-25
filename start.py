import csv
import graphviz
from info_peli import Pelicula
from filtrado import Filtrado
print("Lenguajes Formales y de Programación")
print("A-")
print("Carne: 202100639")
print("Francisco Daniel Peruch de León")
v1=input()
flag=True

while flag==True:
    print("--------------------MENU--------------------")
    print("A continuación se detallan las opciones que se\npueden realizar en el programa.\nIngrese el número de la opcion a realizar")
    print("1.Cargar Archivo de Entrada")
    print("2.Gestionar películas")
    print("3.Filtrado")
    print("4.Gráfica:")
    print("5.Salir")

    opcion=input()

    if opcion=="1":
        print("Ingrese el nombre del archivo")
        file=input()
        doc_open=open(str(file),'r')
        lector = csv.reader(doc_open, delimiter=';')
        lista_peliculas=[]
        for row in lector:
            nombre = row[0]
            actores = row[1]
            ano = row[2]
            genero = row[3]
            newPelicula = Pelicula(nombre,actores,ano,genero)
            lista_peliculas.append(newPelicula)
    elif opcion=="2":
        flag_opcion2=True
        while flag_opcion2==True:
            print("A continuación se muestra las opciones disponibles")
            print("Debe ingresar el número de la opción deseada")
            print("1.Monstra Peliculas")
            print("2.Mostrar Actores")
            print("3.Salir del Menú")
            
            opcion_gestionar=input()
            if opcion_gestionar=="1":
                for movie in lista_peliculas:
                    movie.print_info_peliculas()
            elif opcion_gestionar=="2":
                f=1
                print("A continuación se muestra las películas en el sistema")
                print("Seleccione el número de la película que desea ver los actores\nque participaron en la misma")
                for nombre in lista_peliculas:
                    print(f,".",str(nombre.print_nombre()))
                    f+=1
                nombre_movie=input()
                indice_movie=int(nombre_movie)-1
                print("Los actores que participaron en la película",str(lista_peliculas[indice_movie].print_nombre()),"son:")
                lista_peliculas[int(indice_movie)].print_actores()
                
            elif opcion_gestionar=="3":
                flag_opcion2=False
            else:
                print("Opción incorrecta, ingrese una opcion válida")

    elif opcion=="3":
        
        flag_option_3=True
        while flag_option_3==True:
            print("A continuación se muestra las opciones disponibles para filtrar las películas")
            print("Debe ingresar el número de la opción deseada")
            print("1.Actor")
            print("2.Año")
            print("3.Género")
            print("4.Salir del submenú")
            opcion_filtrado=input()
            if opcion_filtrado=="1":
                print("A continuación se muestran los actores:")
                lista_full_actores=[]
                lista_full=[]
                for actor_peli in lista_peliculas:
                    lista_full_actores+=actor_peli.grupo_actores()
        
                for ber in lista_full_actores:
                    if ber not in lista_full:
                        lista_full.append(str(ber).strip())
                for ar in lista_full:
                    print("**",ar)
                print("Escriba el nombre del actor")
                nombre_busqueda=input()
                peliculas_por_actores=""
                print("Las peliculas donde ha participado",nombre_busqueda)
                print("")

                print("*************************************** \n")
                for ab in lista_peliculas:
                    ab.imprimir_peliculas_actores(nombre_busqueda)
                print("*************************************** \n")
            
            elif opcion_filtrado=="2":
                print("A continuación se muestran los año de estreno:")
                lista_full_anos=[]
                lista_llena_anos=[]
                
                for ano_peli in lista_peliculas:
                    lista_full_anos+=ano_peli.grupo_anos()
                

                for ba in lista_full_anos:
                    if ba not in lista_llena_anos:
                        lista_llena_anos.append(str(ba).strip())

                for bb in lista_llena_anos:
                    print("**",bb)

                ano_estreno=input()
                print("")  
                print("Las películas que se estrenaron en el año",ano_estreno,"son")
                for bc in lista_peliculas:
                    bc.imprimir_peliculas_anos(ano_estreno)

            elif opcion_filtrado=="3":
                print("A continuación se muestan los géneros de las películas:")
                lista_full_generos=[]
                lista_llena_generos=[]
                
                for ca in lista_peliculas:
                    lista_full_generos+=ca.grupo_generos()
                

                for cb in lista_full_generos:
                    if cb not in lista_llena_generos:
                        lista_llena_generos.append(str(cb).strip())

                for cd in lista_llena_generos:
                    print("**",cd)

                genero_peli=input()
                print("")  
                print("Las películas del género",genero_peli,"son")
                for ce in lista_peliculas:
                    ce.imprimir_peliculas_generos(genero_peli)

            elif opcion_filtrado=="4":
                flag_option_3=False

            else:
                print("La opcion Ingresada es invalida, vuelva a ingresar la opción")

    elif opcion=="4":
        
        def graphRelations(lista_peliculas):
            grafo = graphviz.Digraph('ejemplo', filename="grafo");
            grafo.attr(rankdir="LR")

            lista_full_grafo=[]
            lista_full_true=[]
            for actor_peli in lista_peliculas:
                lista_full_grafo+=actor_peli.grupo_actores()
            
            for xd in lista_full_grafo:
                if xd not in lista_full_true:
                    lista_full_true.append(str(xd).strip())


            for fff in lista_full_true:
                grafo.node(str(fff), f'''<
                <TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="4">
                    <TR>
                        <TD COLSPAN="2"><FONT COLOR="red">{fff}</FONT></TD>
                    </TR>
                </TABLE>>''', shape="none")

            for pelicula in lista_peliculas:
                grafo.node(str(pelicula.nombre), f'''<
                <TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="4">
                    <TR>
                        <TD COLSPAN="2"><FONT COLOR="red">{pelicula.nombre}</FONT></TD>
                    </TR>
                    <TR>
                        <TD><FONT COLOR="red">{pelicula.ano}</FONT></TD>
                    <TD><FONT COLOR="red">{pelicula.genero}</FONT></TD>
                    </TR>
                </TABLE>>''', shape="none")
                
                for zzz in lista_full_true:
                    for yyy in pelicula.actores:
                        if (zzz==yyy):
                            grafo.edge(str(pelicula.nombre),zzz)

            grafo.view()

        graphRelations(lista_peliculas)

    elif opcion=="5":
        flag==False
    else:
        print("El valor ingresado es invalido, ingrese una opcion correcta")
        za=input()


    

    






