import pandas as pd
import numpy as np

# Obtendo os dados
try:
    print('Obtendo os dados...')

    ENDERECO_DADOS = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'
    # Principais encodings (utf-8, iso-8859-1, latin1, cp1252)
    df_ocorrencias = pd.read_csv(ENDERECO_DADOS, sep = ';', encoding= 'iso-8859-1')
    # print(df_ocorrencias)
    # delimitando os dados
    df_roubo_veiculo = df_ocorrencias[['munic', 'roubo_veiculo']]
    # print(df_roubo_veiculo.head(30))
    # print(df_roubo_veiculo.tail(30))
    
    ### PREPARANDO OS DADOS
    #Totalizando os roubos por cidade (Var Qualitativa 'munic' e Variavel quantitativa 'roubo_veiculo')
    df_roubo_veiculo = df_roubo_veiculo.groupby('munic', as_index=False)['roubo_veiculo'].sum()
    # print(df_roubo_veiculo.head(50))
    # print(df_roubo_veiculo.tail(50))

    # Ordenandos os dados
    df_roubo_veiculo = df_roubo_veiculo.sort_values(by='roubo_veiculo', ascending=False)
    # print(df_roubo_veiculo.head(10))
    # print(df_roubo_veiculo.tail(10))




except Exception as e:
    print(f'Erro ao obter os dados - {e}')




try:
    print(f'\nObtendo informações a cerca dos roubos dos veículos...')
    array_roubo_veiculo = np.array(df_roubo_veiculo['roubo_veiculo'])

    media_roubo_veiculo = np.mean(array_roubo_veiculo)
    mediana_roubo_veiculo = np.median(array_roubo_veiculo)
    distancia = abs(                                                     # Verificar distância da média para a mediana
        (media_roubo_veiculo - mediana_roubo_veiculo) / mediana_roubo_veiculo * 100
        
        
        )                                                   

    print(f'\nMedidas de Tendência Central')
    print(f'Média: {media_roubo_veiculo:.2f}')
    print(f'Mediana: {mediana_roubo_veiculo}')
    print(f'Distância Média - Mediana: {distancia:.2f} %')                  # 
    

except Exception as e:
    print(f'Obtendo Medidas - {e}')


try:
    q1 = np.quantile(array_roubo_veiculo, .25)
    q2 = np.quantile(array_roubo_veiculo, .50)
    q3 = np.quantile(array_roubo_veiculo, .75)
    
    print('\nMedidas de Posição')
    print(f'Quartil 1: {q1}')
    print(f'Quartil 2: {q2}')
    print(f'Quartil 3: {q3}\n')



    # CIDADES COM MENOS ROUBOS DE VEÍCULOS
    df_roubo_veiculo_menores = df_roubo_veiculo[
        df_roubo_veiculo['roubo_veiculo'] < q1
     ]
    
    # CIDADES COM MAIS ROUBOS
    df_roubo_veiculo_maiores = df_roubo_veiculo[
        df_roubo_veiculo['roubo_veiculo'] > q3
     ]

    # Menores
    print(f'\n Muncípios com menos roubos')
    print(30*'=')
    print(df_roubo_veiculo_menores.sort_values(
        by='roubo_veiculo', ascending=True
         ))
    df_roubo_veiculo_menores.to_csv('menores_roubos.csv', index=False, sep=';', encoding='iso-8859-1')
    # Maiores
    print(f'\n Muncípios com mais roubos')
    print(30*'=')
    print(df_roubo_veiculo_maiores.sort_values(
        by='roubo_veiculo', ascending=False
    ))
     
    df_roubo_veiculo_maiores.to_csv('maiores_roubos.csv', index=False, sep=';', encoding='iso-8859-1')

except Exception as e:
    print(f'Erro ao analizar a distribuição {e}')