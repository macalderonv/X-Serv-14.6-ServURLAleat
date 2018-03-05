#!/usr/bin/python3
#María de los Ángeles Calderón Velasco

import webapp
import random

class urls_aleatorias(webapp.webApp):
	"""docstring for urlsaleat"""

    def process(self, parsedRequest):
        numero = random.randint(1, 1000000)
        url = "http://localhost:1234/" + str(numero)
        return ("200 OK", "<html><body><h1> Hola <a href=" + url + ">dame otra URL</a></    h1></body></html>")

if __name__ == "__main__":
    testWebAppUrls = urls_aleatorias("localhost", 1234)
