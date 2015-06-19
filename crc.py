
message = "01010111"


class CRC:
	_message;
	_tamanho;
	_polynomial;
	_resto_polinomial ;
	""" CONTRUTOR """
	def __init__(self,message):
    	self.message = message
		self.tamanho = len(message);
	"""FUNCOES GET """
	def get_message():
		return self._message;
	def get_tamanho():
		return self._tamanho;
	def get_message():
		return self._polynomial;
	def get_message():
		return self._resto_polinomial;
	"""Funcao que codifica a mensagem utilizando o algoritmo crc 8"""
	def codificar_crc(message)
		polynomial = message;
		n = 2;
		for i in xrange(1,tamanho-1):
			resto =  polynomial * x + message[i+n]
			pass

		pass
	""" FUNCAO QUE DECODIFICA E RETORNA CASO TENHA ERRO"""
	def decodificar_crc(message):
		

		pass


main();