class CuentaBancaria:

    def __init__(self, balance, interes):
        self.balance = balance
        self.interes = interes/100

    def deposito(self, cantidad):
        self.balance += cantidad
        return self

    def retiro(self, cantidad):
        if(cantidad>self.balance):
            print("Fondos insuficientes")
            if(self.balance<5):
                self.balance=0
            else:
                self.balance -=5
            return self
        self.balance -= cantidad
        return self

    def mostrar(self):
        print("Balance: "+str(self.balance))
        return self

    def generarInteres(self):
        if(self.balance>0):
            self.balance += (self.balance*self.interes)
        return self


ahorros = CuentaBancaria(100, 2)
corriente= CuentaBancaria(200,5)
ahorros.mostrar().deposito(120).mostrar().deposito(60).mostrar().deposito(60).mostrar().retiro(240).mostrar().generarInteres().mostrar()
corriente.mostrar().deposito(100).mostrar().deposito(50).mostrar().retiro(50).mostrar().retiro(50).mostrar().retiro(50).mostrar().retiro(50).mostrar().generarInteres().mostrar()