from cuentaBancaria import cuentaBancaria,Usuario

Ahorros = cuentaBancaria(1000, 1.2)
Corriente = cuentaBancaria(0, 1)

John=Usuario("John","john@smith.com",{"Ahorros":cuentaBancaria(0,1),"Corriente":cuentaBancaria(5000,6)})

John.hacer_deposito(9000,"Ahorros")
John.mostrarBalance("Ahorros")

John.cuentas["Ahorros"].generar_interes()
John.mostrarBalance("Ahorros")

John.hacer_retiro(1900,"Corriente")
John.cuentas["Corriente"].generar_interes()
John.mostrarBalance("Corriente")