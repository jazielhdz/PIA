import re


class Vehiculo:
    def __init__(self, unidad, marca, modelo, km):
        if not re.match(r"^[A-Za-z0-9]{2}-[A-Za-z0-9]{3}$", unidad):
            raise ValueError("Código inválido. Formato: XX-123.")
        if not (2020 <= modelo <= 2024):
            raise ValueError("Modelo fuera del rango permitido (2020-2024).")
        if km < 0:
            raise ValueError("Kilómetros deben ser positivos.")
        self.unidad, self.marca, self.modelo, self.km = unidad, marca, modelo, km

    def modificar(self, marca, modelo, km):
        self.marca, self.modelo, self.km = marca, modelo, km

    def __str__(self):
        return f"{self.unidad} - {self.marca}, {self.modelo}, {self.km} km"


class GestionFlota:
    def __init__(self):
        self.unidades = []

    def agregar(self):
        try:
            unidad = input("Unidad (XX-123): ")
            marca = input("Marca: ")
            modelo = int(input("Modelo (2020-2024): "))
            km = int(input("Kilómetros: "))
            self.unidades.append(Vehiculo(unidad, marca, modelo, km))
            print("Unidad agregada.")
        except Exception as e:
            print(f"Error: {e}")

    def modificar(self):
        unidad = input("Unidad a modificar: ")
        for v in self.unidades:
            if v.unidad == unidad:
                try:
                    marca = input("Nueva marca: ")
                    modelo = int(input("Nuevo modelo (2020-2024): "))
                    km = int(input("Nuevos kilómetros: "))
                    v.modificar(marca, modelo, km)
                    print("Unidad modificada.")
                except Exception as e:
                    print(f"Error: {e}")
                return
        print("Unidad no encontrada.")

    def eliminar(self):
        unidad = input("Unidad a eliminar: ")
        self.unidades = [v for v in self.unidades if v.unidad != unidad]
        print("Unidad eliminada.")

    def listar(self):
        if not self.unidades:
            print("No hay unidades registradas.")
        else:
            print("\n".join(f"{i+1}. {v}" for i, v in enumerate(self.unidades)))

    def menu(self):
        opciones = {"1": self.agregar, "2": self.modificar, "3": self.eliminar, "4": self.listar}
        while (opcion := input("\n1. Agregar\n2. Modificar\n3. Eliminar\n4. Listar\n5. Salir\nOpción: ")) != "5":
            opciones.get(opcion, lambda: print("Opción inválida."))()


if __name__ == "__main__":
    GestionFlota().menu()
