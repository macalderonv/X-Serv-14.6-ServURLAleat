#!/usr/bin/python3
#María de los Ángeles Calderón Velasco

import webapp
import random


class urlsaleat(webapp.webApp):
	"""docstring for urlsaleat"""
	def process (self, parsedRequest):
		num_aleat = random.randrange(1000000)
		return ("200 OK", "<html><body><h1> Hola <a href=" + str(num_aleat) + ">dame otra URL</a></h1></body></html>")

if __name__ == "__main__":
    testWebApp = urlsaleat("localhost", 1234)
