
# Ingreso de datos por consola
salarioBase = float(input("Por faor ingrese el salario base mensual $: "))
cargo = input("Por favor ingrese el cargo del empleado: ")
desempeño = input("Por favor ingrese el nivel de desempeño: ")
def calcularBonificacion(salarioBase, cargo, desempeño):
    if cargo.lower() == "directivo":
        if desempeño.lower() == "alto":
            bonificacion = salarioBase * 0.20
        elif desempeño.lower() == "medio":
            bonificacion = salarioBase * 0.10
        else:
            bonificacion = 0
    elif cargo.lower() == "operativo":
        if desempeño.lower() == "alto":
            bonificacion = salarioBase * 0.15
        elif desempeño.lower() == "medio":
            bonificacion = salarioBase * 0.05
        else:
            bonificacion = 0
    else:
        bonificacion = 0  #cuando inngresan un cargo que no existe

    totalRecibir = salarioBase + bonificacion
    return bonificacion, totalRecibir

# Para que se cambie el cargo de empleado a primera mayuscula
def modificarCargo(cargo):
    return cargo.capitalize()



# Cálcular bonificacion
bonificacion, totalRecibir = calcularBonificacion(salarioBase, cargo, desempeño)

# imprimir
print("\n-----Resumen del Pago-----")
print(f"Cargo: {modificarCargo(cargo)}")
print(f"Nivel de Desempeño: {desempeño.capitalize()}")
print(f"Salario Base: ${salarioBase:.0f}")
print(f"Bonificación: ${bonificacion:.0f}")
print(f"Total a Recibir: ${totalRecibir:.0f}")
print("------------------------------------")
