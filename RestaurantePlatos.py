class RestaurantePlatos:
    def __init__(self, capacidad_limpios=20):
        self.limpios = []  # pila de platos limpios
        self.sucios = []   # pila de platos sucios
        self.capacidad_limpios = capacidad_limpios

    def recibir_plato_sucio(self, plato_id: str):
        self.sucios.append(plato_id)
        print(f"Plato sucio recibido: {plato_id}")

    def lavar_un_plato(self):
        if not self.sucios:
            print("No hay platos sucios para lavar.")
            return False

        if len(self.limpios) >= self.capacidad_limpios:
            print("La pila de platos limpios está llena.")
            return False

        plato = self.sucios.pop()      # LIFO
        self.limpios.append(plato)     # pasa a limpios
        print(f"Plato lavado y apilado limpio: {plato}")
        return True

    def servir_plato(self):
        if not self.limpios:
            print("No hay platos limpios para servir.")
            return None

        plato = self.limpios.pop()  # LIFO
        print(f"Plato servido: {plato}")
        return plato

    def estado(self):
        print("\n--- ESTADO ---")
        print("Limpios (abajo->arriba):", self.limpios)
        print("Sucios  (abajo->arriba):", self.sucios)
        print("-------------\n")


def menu():
    r = RestaurantePlatos(capacidad_limpios=5)

    while True:
        print("1) Recibir plato sucio")
        print("2) Lavar un plato")
        print("3) Servir un plato")
        print("4) Ver estado")
        print("5) Salir")
        op = input("Elige: ").strip()

        if op == "1":
            pid = input("ID del plato (ej: P1): ").strip()
            r.recibir_plato_sucio(pid)

        elif op == "2":
            r.lavar_un_plato()

        elif op == "3":
            r.servir_plato()

        elif op == "4":
            r.estado()

        elif op == "5":
            print("Bye")
            break

        else:
            print("Opción inválida.\n")


if __name__ == "__main__":
    menu()



