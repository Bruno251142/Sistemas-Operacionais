# importando as bibliotecas que a gente vai precisar
import threading  # essa aqui é pra criar e trabalhar com threads (processos que rodam em paralelo)
import time       # essa aqui é só pra gente conseguir colocar pausas no código (tipo um "espera aí")

# função que cada thread vai executar
def sequencia(nome, inicio, fim):  # recebe o nome da thread, o número inicial e o final da contagem
    for i in range(inicio, fim + 1):  # faz um loop que conta do número inicial até o final
        print(f"{nome} -> {i}")       # mostra na tela o nome da thread e o número atual
        time.sleep(2)                 # dá uma pausa de 2 segundo antes de ir pro próximo número

# criando as threads (como se fossem “tarefas paralelas”)
thread1 = threading.Thread(target=sequencia, args=("thread1", 1, 10))   # primeira thread, vai contar de 1 até 10
thread2 = threading.Thread(target=sequencia, args=("thread2", 50, 60))  # segunda thread, vai contar de 50 até 60

# iniciando as threads (colocando elas pra rodar ao mesmo tempo)
thread1.start()  # liga a primeira thread
thread2.start()  # liga a segunda thread

# esperando as threads terminarem antes de encerrar o programa
thread1.join()  # o programa principal espera a primeira terminar
thread2.join()  # e também espera a segunda terminar
