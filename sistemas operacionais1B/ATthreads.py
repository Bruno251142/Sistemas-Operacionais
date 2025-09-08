#importação de biblioteca
import threading # para Thread 
import time # para o tempo

#estrtura da thread 

def sequencia(nome, inicio, fim):
    for i in range(inicio, fim +1):
        print(f"{nome} -> {i}")
        #pausar entre as durações de contagem 
        time.sleep(1)

# criar thread 
thread1 = threading.Thread(target=sequencia, args=("thread1", 1, 10))
thread2 = threading.Thread(target=sequencia, args=("thread2", 50, 60))

# rodar 
thread1.start()
thread2.start()

#estado de espera
thread1.join()
thread2.join()