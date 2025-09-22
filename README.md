Questão: Explique o que ocorre quando um processo passa do estado Pronto para Executando.

Resposta:

Quando um processo passa do estado Pronto para Executando, significa que ele foi escolhido pelo sistema operacional para usar a CPU naquele momento. Essa escolha é feita pelo escalonador, que leva em conta fatores como prioridade e o algoritmo de escalonamento configurado.

Durante a simulação que realizei no SoSim, percebi que o processo de cor vermelha, que tinha prioridade 1, era o que mais alternava entre os estados Pronto e Executando. Isso mostra que ele estava sendo constantemente selecionado para usar o processador. Por outro lado, o processo amarelo, que também tinha prioridade 1, passava bastante tempo em I/O, ou seja, esperando por alguma operação de entrada ou saída, o que o colocava no estado de espera. Com isso, o processo vermelho acabava voltando a executar sempre que o amarelo saía para o I/O.

Já os processos de cor azul, verde e marrom, que tinham prioridade 0, ficaram o tempo todo no estado Pronto, mas nunca chegaram a ser executados. Isso provavelmente aconteceu porque o sistema estava usando uma política de escalonamento por prioridade, e os processos com prioridade mais baixa acabaram sendo ignorados enquanto havia outros mais prioritários disponíveis.

Ou seja, o processo só muda de Pronto para Executando quando é escolhido para usar a CPU, e isso depende principalmente da sua prioridade e do momento em que está disponível. No caso da simulação, ficou claro que os processos com prioridade mais alta dominaram a execução.

Questões:

Qual algoritmo apresentou menor tempo médio de espera?

Resposta: 
O menor tempo médio de espera foi no escalonamento circular, porque divide a CPU de forma justa entre os processos.

No Round Robin, como o quantum influencia no desempenho do sistema?

Resposta: 

Pequeno → muitas trocas de contexto, mais lento.
Grande → processos esperam mais, parece FIFO.
Ideal → equilíbrio entre justiça e eficiência.

Questões:

Explique o que é uma falta de página e como o sistema operacional a trata.

Resposta:
Uma falta de página acontece quando um processo tenta acessar uma página que não está na memória RAM.
O SO trata carregando essa página do disco (arquivo de paginação) para a RAM. Se não houver espaço, ele escolhe uma página para retirar (substituição de página).

Compare a execução de um processo com paginação e sem paginação. Quais vantagens você observou?

Resposta: 

Com paginação: permite executar processos maiores que a memória física, usa a memória de forma mais eficiente, mas pode gerar mais faltas de página (e ficar mais lento se exagerar). Já o sem paginação: O processo precisa caber inteiro na RAM. É mais rápido (sem custo de faltas de página), mas limita o tamanho do processo e pode desperdiçar memória.
A vantagem que eu observei é que com paginação dá pra rodar processos maiores e vários ao mesmo tempo, mesmo com RAM limitada, melhora o aproveitamento da memória evitando desperdício e facilita a multiprogramação rodando vários processos ao mesmo tempo.

