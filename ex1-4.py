import pandas as pd
from datetime import datetime as dt

# Guardando o tempo de inicio do programa
programStart = dt.now()

licenses = pd.read_excel('Input_Teste_Python_Dados Exercicio 4 I.xlsx')
names = pd.read_excel('Input_Teste_Python_Dados Exercicio 4 II.xlsx')

output = licenses # Salvando em outra variavel para não perder os dados originais

for row in range(len(licenses['User Name'])):
	start = str(licenses['Start Time'][row])
	end = str(licenses['End Time'][row])

	startDate = start.split(" ")[0]
	startDate = startDate.split("/")[2] + "-" + startDate.split("/")[1] + "-" + startDate.split("/")[0] # Arrumando a data para ficar como o padrão do lista 2 (names)
	endDate = end.split(" ")[0]
	startTime = start.split(" ")[1]
	endTime = end.split(" ")[1]

	for row2 in range(len(names['Usuario'])):
		if names['Hora Inicio'][row2] == startTime:
			if names['Data Inicio'][row2] == startDate:
				output['User Name'][row] = names['Usuario'][row2]
				break

output.to_excel("Output_Teste_Python_exercicio 4.xlsx")
# Imprimindo o tempo de execução e salvando em um arquivo .txt o tempo de execução para facilitar a visualização futura
print("Tempo de execução: " + str(dt.now() - programStart))
with open("Output_Teste_Python_exercicio 4.txt", "w") as file:
	file.write("Tempo de execução: " + str(dt.now() - programStart))