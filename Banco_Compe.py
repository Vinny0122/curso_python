import pyodbc
import csv
import datetime
data_inicial = datetime.datetime(2023,1,2,0,0)
time_delta = datetime.timedelta(1)

data_final = datetime.datetime(2023,4,3,0,0)

#data_inicial = data_inicial+(time_delta*1)
#print(data_inicial.strftime('%Y%m%d'))
dados_conexao = (
    "Driver={SQL Server};"
    "Server=SP7012SR600\MSSQLSERVER01;"
    "Database=7012_2;"
)
conexao = pyodbc.connect(dados_conexao)
print('Conexão bem sucedida!')

cursor = conexao.cursor()
while data_inicial < data_final:
    data_inicial = data_inicial+(time_delta*1)
    dados = '\'' + data_inicial.strftime('%Y%m%d') + '\''
   
    comando = """USE [7012_2]
                DECLARE	@return_value int
                EXEC	@return_value = [des].[CMP_FraudeEvitada_INSERE]
                        @data_movimento = """ + dados + """
                SELECT	'Return Value' = @return_value
                """
    cursor.execute(comando)
    cursor.commit()
    print(f'Dia ' + data_inicial.strftime('%d/%m/%Y') + ' inserido com sucesso')
    data_inicial = data_inicial+(time_delta*1)

cursor.close
print('Conexão encerrada.')