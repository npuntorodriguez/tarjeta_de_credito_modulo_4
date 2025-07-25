from tarjeta_de_credito import TarjetaCredito

print("--- Iniciando el Programa de Gestión de Tarjetas ---")

print("\n--- Creando Tarjetas de Crédito ---")
TC1 = TarjetaCredito(10000, 0.05, 1000)
TC2 = TarjetaCredito(5000, 0.03, 500)
TC3 = TarjetaCredito(15000, 0.01, 2000)
TC_Nueva = TarjetaCredito(2000, 0.02, 0)

print("\n" + "="*40)
print("--- Operaciones con Tarjetas ---")
print("="*40 + "\n")

print("--- Operaciones TC1 ---")
TC1.compra(500).compra(200).pago(300).cobrar_interes().mostrar_info_tarjeta()

print("\n--- Operaciones TC2 ---")
TC2.compra(1000).compra(700).compra(300).pago(500).pago(200).cobrar_interes().mostrar_info_tarjeta()

print("\n--- Operaciones TC3 ---")
TC3.compra(3000).compra(4000).compra(5000).compra(6000).compra(100).mostrar_info_tarjeta()

TarjetaCredito.imprimir_todas_las_tarjetas()