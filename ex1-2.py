while True:
	try:
		N = int( input() )
		if N < 2 or N > 10000:
			raise Exception( "N fora do intervalo" )
		if N%2 != 0:
			raise Exception( "N deve ser par" )

		botasEntreges = [ "" for i in range( 31 ) ] # base de números de 30 a 60 (tamanhos de botas)
		botasCorretas = 0 # Número de pares de botas corretas entregues

		for i in range( N ):
			linha = input().split( " " ) # Formato: <tamanho> <pe>

			if len( linha ) != 2:
				raise Exception( "Formato da linha invalido" )

			tam = int( linha[0] ) # Tamanho da bota de 30 a 60
			pe = linha[1] # Pe da bota: "E" ou "D"

			if tam < 30 or tam > 60:
				raise Exception( "Tamanho da bota fora do intervalo" )
			if pe != "E" and pe != "D":
				raise Exception( "Pe da bota invalido" )
			tam -= 30 # Normalizando o tamanho da bota para o indice do vetor
			if botasEntreges[tam] == "": # Se não houver bota do tamanho "tam" entregue
				botasEntreges[tam] = pe
			elif botasEntreges[tam] != pe: # Se o pé da bota entregue for diferente do atual, ele incrementa o número de botas corretas e rezeta o vetor
				botasEntreges[tam] = ""
				botasCorretas += 1

		print( botasCorretas )
	except Exception as err:
		print( err )
		break