#!/usr/bin/python3

import webapp

class holaApp(webapp.webApp):
    def parse(self, request):   
        return request.split()[1][1:]
        
    def process(self, parsedRequest):
        return("200 OK", "<html><body><h1>HOLA," + parsedRequest + "</h1></body></html>")

if __name__ == "__main__":
    testWebApp = holaApp("localhost", 4577)
