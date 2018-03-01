#!/usr/bin/python3

import webapp
import calculadora
#... /1/suma/2 ...

class holaAppCalculadora(webapp.webApp):
    def parse(self, request):   
        numero1, operacion, numero2 = request.split()[1].split('/')[1:]  #['1', 'suma', '2']
        return (numero1, operacion, numero2)
        
    def process(self, parsedRequest):
        print(parsedRequest) #[ '1', 'suma', '2']
        numero1, operacion, numero2= parsedRequest
        solucion = calculadora.funciones[operacion](int(numero1), int(numero2))
        return("200 OK", "<html><body><h1> La solucion es: " + str(solucion) + "</h1></body></html>")   

if __name__ == "__main__":
    testWebAppcalculadora = holaAppCalculadora("localhost", 4587)
