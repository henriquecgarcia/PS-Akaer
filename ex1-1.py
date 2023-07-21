N = int( input() )
if N < 2 or N > 1000:
	print( "N fora do intervalo" )
	exit( 0 )

quebraCabeca = []
pecas = input().split( " " )
for i in range( N-1 ):
	peca = int( pecas[i] )
	quebraCabeca.append( peca )

for i in range( N-1 ):
	if i+1 not in quebraCabeca:
		print( i+1 )
		break