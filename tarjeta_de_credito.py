class TarjetaCredito:
    _todas_las_tarjetas = []

    def __init__(self, limite_credito, intereses, saldo_pagar):
        if limite_credito <= 0:
            print("Error: El límite de crédito debe ser un número positivo.")
        if not (0 <= intereses < 1):
            print("Error: La tasa de interés debe ser un decimal entre 0 y 1.")
        if saldo_pagar < 0:
            print("Error: El saldo a pagar no puede ser negativo.")

        self.saldo_pagar = saldo_pagar
        self.limite_credito = limite_credito
        self.intereses = intereses

        TarjetaCredito._todas_las_tarjetas.append(self)
        print(f"Tarjeta creada. Límite: ${limite_credito:.2f}, Intereses: {intereses*100:.2f}%, Saldo inicial: ${saldo_pagar:.2f}")

    def compra(self, monto):
        if monto <= 0:
            print("Error en la compra: El monto debe ser un número positivo.")
            return self

        credito_disponible = self.limite_credito - self.saldo_pagar
        
        if monto > credito_disponible:
            print("Tarjeta Rechazada, has alcanzado tu límite de crédito")
        else:
            self.saldo_pagar += monto
            print(f"Compra de ${monto:.2f} realizada. Nuevo saldo: ${self.saldo_pagar:.2f}")
        return self

    def pago(self, monto):
        if monto <= 0:
            print("Error en el pago: El monto a pagar debe ser un número positivo.")
            return self
        
        if monto > self.saldo_pagar and self.saldo_pagar > 0:
            self.saldo_pagar = 0
        else:
            self.saldo_pagar -= monto
        
        print(f"Pago de ${monto:.2f} realizado. Nuevo saldo: ${self.saldo_pagar:.2f}")
        return self

    def mostrar_info_tarjeta(self):
        print(f"Saldo a Pagar: ${self.saldo_pagar:.2f}")
        return self

    def cobrar_interes(self):
        if self.saldo_pagar > 0:
            interes_cobrado = self.saldo_pagar * self.intereses
            self.saldo_pagar += interes_cobrado
            print(f"Intereses cobrados (${interes_cobrado:.2f}). Saldo actual con intereses: ${self.saldo_pagar:.2f}")
        else:
            print("No hay saldo a pagar, no se cobran intereses.")
        return self

    @classmethod
    def imprimir_todas_las_tarjetas(cls):
        print("\n--- Información de TODAS las Tarjetas Creadas ---")
        if not cls._todas_las_tarjetas:
            print("No se han creado tarjetas aún.")
            return
        
        for i, tarjeta in enumerate(cls._todas_las_tarjetas):
            print(f"\n--- Tarjeta #{i+1} ---")
            tarjeta.mostrar_info_tarjeta()
            print(f"   Límite de crédito: ${tarjeta.limite_credito:.2f}")
            print(f"   Intereses: {tarjeta.intereses*100:.2f}%")
            print(f"   Crédito disponible: ${tarjeta.limite_credito - tarjeta.saldo_pagar:.2f}")
            print("------------------------")