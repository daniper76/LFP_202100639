class Pelicula:
    def __init__(self,nombre,actores,ano,genero):
        self.nombre =str(nombre).strip()
        self.actores=actores.split(",")
        self.ano=str(ano).strip()
        self.genero=str(genero).strip()
        self.busca_actor=""
        self.busca_ano=""
        self.busca_genero=""

    def print_info_peliculas(self):
        print("Nombre de la película: ",self.nombre)
        print("Actores de la película: ")
        for actors in self.actores:
            print(str(actors).strip())
        print("Año de Estreno: ",self.ano)
        print("Genero de la Película: ",self.genero,"\n")
    
    def print_nombre(self):
        return self.nombre

    
    def print_actores(self):
        for i in self.actores:
            print(str(i).strip())
    
    def grupo_actores(self):
        lista_actores=[]
        for a in self.actores:
            lista_actores.append(str(a).strip())
        return lista_actores
    
    def imprimir_peliculas_actores(self,busca_actor):
        self.busca_actor=busca_actor
        for actorillos in self.actores:
            if self.busca_actor==str(actorillos).strip():
                print(self.nombre)
    
    def grupo_anos(self):
        lista_anos=[]
        lista_anos.append(self.ano)
        return lista_anos
    
    def imprimir_peliculas_anos(self,busca_ano):
        self.busca_ano=str(busca_ano).strip()
        if self.busca_ano==self.ano:
            print(self.nombre)
    
    def grupo_generos(self):
        lista_generos=[]
        lista_generos.append(self.genero)
        return lista_generos
    
    def imprimir_peliculas_generos(self,busca_genero):
        self.busca_genero=str(busca_genero).strip()
        if self.busca_genero==self.genero:
            print(self.nombre)
        
    

    


