from random import choice
from collections import defaultdict

def main():
    tiempo = 0

    # Usamos defaultdict para que se cree automáticamente una instancia de Proximo cuando se acceda a una clave que no existe en el diccionario
    aQuienHayQueLlamar = defaultdict(Proximo)

    print("Sal de ahí chivita chivita, sal de ahí de ese lugar")
    tiempo += 1
    ahora = "la chiva"
    for i in range(N):
        proximo = aQuienHayQueLlamar[ahora]
        proximo.proximo_actual = choice(Animales.lista)
        proximo.agregar_proximo_actual_a_la_lista()
        aQuienHayQueLlamar[ahora] = proximo
        print(f"Hay que llamar a {proximo.proximo_actual} para que saque a {ahora}")
        tiempo += 1
        ahora = proximo.proximo_actual
        sacar = []
        cursor = "la chiva"

        # Bucle que busca al siguiente animal de la lista
        while cursor in aQuienHayQueLlamar and len(sacar) <= i:
            proximo = aQuienHayQueLlamar[cursor]
            sacar.insert(0, f"{proximo.llamar_al_proximo_de_la_lista()} no quiere sacar a {cursor}")
            cursor = proximo.proximo_actual

        # Imprimimos las líneas obtenidas en el bucle anterior
        for linea in sacar:
            print(linea)
            tiempo += 1

        # Reiniciamos el índice actual de cada instancia de Proximo a cero
        for p in aQuienHayQueLlamar.values():
            p.reiniciar_indice_actual_a_cero()

        print("La chiva no quiere salir de ahí. Sal de ahí chivita chivita, sal de ahí de ese lugar....\n")
        tiempo += 1

    print(f"--------------- TIEMPO DE EJECUCIÓN: {tiempo} milisegundos ---------------")

class Proximo:
    def __init__(self):
        self.lista_proximos = [] # lista de próximos que serán llamados para sacar al animal actual
        self.indice_actual = 0 # índice actual de la lista de próximos
        self.proximo_actual = None # próximo animal que será llamado

    def agregar_proximo_actual_a_la_lista(self):
        self.lista_proximos.append(self.proximo_actual) # agrega el próximo actual a la lista de próximos

    def llamar_al_proximo_de_la_lista(self):
        if self.indice_actual >= len(self.lista_proximos):
            self.indice_actual = 0  # si se llega al final de la lista, reinicia el índice al principio
        proximo = self.lista_proximos[self.indice_actual]
        self.indice_actual += 1 # incrementa el índice para el próximo llamado
        return proximo # devuelve el próximo animal que será llamado

    def reiniciar_indice_actual_a_cero(self):
        self.indice_actual = 0 # reinicia el índice actual a cero

class Animales:
    lista = ['el perro', 'el elefante', 'el mono', 'la jirafa', 'el tigre', 'el león', 'la vaca', 'el cerdo', 'la oveja', 'el conejo', 'el ratón', 'el hámster', 'el hamster', 'el pez', 'el pájaro', 'el pingüino', 'el camello', 'el canguro', 'el koala', 'la cabra', 'el zorro', 'el murciélago', 'el oso', 'la ballena', 'el delfín', 'la foca', 'el hipopótamo', 'el rinoceronte', 'el alce', 'el ciervo', 'el jaguar', 'la pantera', 'el guepardo', 'el castor', 'la ardilla', 'la marmota', 'el armadillo', 'el oso hormiguero', 'el topo', 'la morsa', 'la tortuga', 'el cocodrilo', 'la serpiente', 'el lagarto', 'la iguana', 'el sapo', 'la rana', 'el tucán', 'el loro', 'el buitre', 'el cuervo', 'el águila', 'el pavo', 'el pato', 'el cisne', 'el ganso', 'la mariposa', 'la abeja', 'el mosquito', 'la hormiga', 'el escarabajo', 'la araña', 'el grillo', 'el saltamontes', 'la cucaracha', 'la hormiga león', 'el escorpión', 'la pulga', 'el gusano', 'el caracol', 'la medusa', 'el calamar', 'la estrella de mar', 'el pulpo', 'el pez globo', 'el tiburón', 'la rana toro', 'el tritón', 'el tiburón martillo', 'el tiburón blanco', 'la foca', 'el cangrejo', 'la langosta', 'el esturión', 'la lucioperca', 'el pez espada', 'la merluza', 'el salmón', 'el atún', 'la caballa', 'la anguila', 'la cabra montés', 'los osos panda', 'el perico', 'el periquito', 'la paloma', 'el cóndor', 'el búfalo', 'el yak', 'el ren', 'el ciervo almizclero']

if __name__ == "__main__":
    N = 10
    main()

