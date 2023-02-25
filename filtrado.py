import graphviz
class Filtrado:
    def __init__(self,lista_full):
        self.lista_full=lista_full

    def grupo_real_actores(self):
        lista_true=[]
        for ber in self.lista_full:
            if ber not in self.lista_true:
                lista_true.append(ber)
        return lista_true
