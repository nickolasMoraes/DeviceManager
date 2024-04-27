import time
import sys
 
# Simule um processo de longa duração
def processo_longo():
    for i in range(10):
        time.sleep(0.5)  # Simule o trabalho dormindo por 0.5 segundos
        # Atualize a barra de progresso
        sys.stdout.write(f'\r[{"=" * (i+1):<10}] {(i+1)*10}%')
        sys.stdout.flush()
    print('\nProcesso concluído.')
 
# Registre o tempo de início
tempo_inicial = time.time()
 
# Chame a função de processo longo
processo_longo()
 
# Calcule o tempo decorrido
tempo_decorrido = time.time() - tempo_inicial
 
# Imprima o tempo de execução
print(f"O processo levou {tempo_decorrido:.2f} segundos para ser executado.")