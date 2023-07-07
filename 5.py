class Empleado:
    def __init__(self, rol, nombre, cedula, balance=0):
        self.rol = rol
        self.nombre = nombre
        self.cedula = cedula
        self.balance = balance

    def retirar_dinero(self, cantidad):
        if cantidad <= self.balance:
            self.balance -= cantidad
            print(f"Se han retirado {cantidad} pesos de la cuenta de {self.nombre}")
        else:
            print(f"No se pudo retirar {cantidad} pesos de la cuenta de {self.nombre}, saldo insuficiente")

    def pagar_salario(self, cantidad):
        self.balance += cantidad
        print(f"Se ha pagado un salario de {cantidad} pesos a {self.nombre}")


class Nomina:
    def __init__(self, presupuesto):
        self.presupuesto = presupuesto
        self.empleados = []

    def ae(self, empleado):
        self.empleados.append(empleado)

    def me(self):
        print("Lista de empleados:")
        for empleado in self.empleados:
            print(f"{empleado.nombre}, Rol: {empleado.rol}, Cedula: {empleado.cedula}, Balance: {empleado.balance}")

    def pn(self):
        total_a_pagar = 0
        for empleado in self.empleados:
            if empleado.rol == "Programador Junior":
                salario = 30000
            elif empleado.rol == "Programador Senior":
                salario = 50000
            elif empleado.rol == "Manager":
                salario = 70000
            else:
                salario = 0

            total_a_pagar += salario
            empleado.pagar_salario(salario)

        if total_a_pagar > self.presupuesto:
            print("No hay suficiente presupuesto para pagar la nómina")
        else:
            self.presupuesto -= total_a_pagar

    def ap(self, cantidad):
        self.presupuesto += cantidad

nomina = Nomina(presupuesto=100000)

while True:
    opcion = int(input("1. Agregar empleado\n2. Mostrar empleados\n3. Pagar nómina\n4. Agregar presupuesto\n5. Salir\n>>>"))

    if opcion == "1":
        rol = input("Ingrese el rol del empleado: ")
        nombre = input("Ingrese el nombre del empleado: ")
        cedula = input("Ingrese la cédula del empleado: ")
        empleado = Empleado(rol, nombre, cedula)
        nomina.ae(empleado)
    elif opcion == "2":
        nomina.me()
    elif opcion == "3":
        nomina.pn()
    elif opcion == "4":
        cantidad = int(input("Ingrese la cantidad a agregar al presupuesto: "))
        nomina.ap(cantidad)
    elif opcion == "5":
        break
    else:
        print("Opción inválida")