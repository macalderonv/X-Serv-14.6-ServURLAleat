#!/usr/bin/python3
#María de los Ángeles Calderón Velasco

import webapp
import random

class urls_aleatorias(webapp.webApp):
	"""docstring for urlsaleat"""

	def process (self, parsedRequest):
		numero_aleatorio = random.randrange(100000000)
		return ("200 OK", "<html><body><h1> Hola <a href=" + str(numero_aleatorio) + ">dame otra URL</a></h1></body></html>")

if __name__ == "__main__":
    testWebAppUrls = urls_aleatorias("localhost", 1234)
