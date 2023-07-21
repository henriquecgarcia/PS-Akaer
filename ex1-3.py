import pandas as pd
import numpy as np
from datetime import datetime as dt

# Guardando o tempo de inicio do programa
programStart = dt.now()

dados = pd.read_excel( "Input_Teste_Python_exercicio 3.xlsx" )

dados['Day'] = np.nan
dados['Tempo de Uso'] = np.nan

for row in range(len(dados['Email'])):
	start = str(dados['Start Time'][row])
	end = str(dados['End Time'][row])
	
	
	dateStart = start.split(" ")[0]
	dateEnd = end.split(" ")[0]

	timeStart = start.split(" ")[1]
	timeEnd = end.split(" ")[1]
	startHour = int(timeStart.split(":")[0])
	endHour = int(timeEnd.split(":")[0])
	startMin = int(timeStart.split(":")[1])
	endMin = int(timeEnd.split(":")[1])

	tempoDecorrido = (endHour - startHour) * 60 + (endMin - startMin)

	hour = str( int( (tempoDecorrido-tempoDecorrido%60)/60 ) )
	
	dados['Day'][row] = dateStart
	dados['Tempo de Uso'][row] = hour + ":" + str(tempoDecorrido % 60) + ":00" 

dados = dados.drop(columns=['Start Time', 'End Time'])

dados.to_excel("Output_Teste_Python_exercicio 3.xlsx")
# print(dados.head())
# Imprimindo o tempo de execução e salvando em um arquivo .txt o tempo de execução para facilitar a visualização futura
print("Tempo de execução: " + str(dt.now() - programStart))
with open("Output_Teste_Python_exercicio 3.txt", "w") as file:
	file.write("Tempo de execução: " + str(dt.now() - programStart))