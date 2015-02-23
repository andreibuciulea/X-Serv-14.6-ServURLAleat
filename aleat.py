#!/usr/bin/python

import webapp
import random
import socket
usuario = socket.gethostname()
class miweb(webapp.webApp):
	def process(self,parsedRequest):
		aleatorio = str(int(random.random()*1000000))
		return ("200 OK","<html><body><h1>"+ aleatorio +"</h1></body></html>")

if __name__ == "__main__":
	new_web = miweb(usuario,1235)
