import time

def fifo_page_replacement(pages, num_frames):
    frames = []  # Armazenar as páginas na memória
    page_faults = 0  # Contar o número de faltas de página
    acessos_memoria = {page: 0 for page in set(pages)}  # Para medir a utilização da memória

    start_time = time.time()  # Iniciar a medição do tempo de execução

    # Passo 2: Para cada referência de página na sequência
    for page in pages:
        # Passo 3: Verificar se a página já está em uma das molduras de página
        if page not in frames:
            # Se não estiver, ocorreu uma falta de página
            page_faults += 1
            # Passo 4: Verificar se há espaço vazio em uma das molduras de página
            if len(frames) < num_frames:
                # Se houver, adicione a página à moldura de página vazia
                frames.append(page)
            else:
                # Se não houver, remover a página mais antiga (FIFO)
                frames.pop(0)
                frames.append(page)
        
        # Atualizar contagem de acessos na memória
        if page in frames:
            acessos_memoria[page] += 1

    end_time = time.time()  # Finalizar a medição do tempo de execução

    # Calcular as métricas
    tempo_execucao = end_time - start_time
    taxa_faltas = page_faults / len(pages)

    # Definir tempos de acesso (em milissegundos)
    tempo_ram = 0.1  # Exemplo: 0.1 ms para acesso à RAM
    tempo_disco = 10  # Exemplo: 10 ms para acesso ao disco (em caso de falta de página)

    # Calcular o tempo médio de acesso
    taxa_acesso_ram = 1 - taxa_faltas
    tempo_medio_acesso = (taxa_acesso_ram * tempo_ram) + (taxa_faltas * tempo_disco)

    # Exibir as métricas
    print(f"\nMétricas do Algoritmo FIFO:")
    print(f"Total de Faltas de Página: {page_faults}")
    print(f"Taxa de Faltas de Página: {taxa_faltas:.2f}")
    print(f"Tempo Médio de Acesso: {tempo_medio_acesso:.2f} ms")
    print(f"Tempo de Execução do Algoritmo: {tempo_execucao:.6f} segundos")
    print(f"Utilização da Memória (acessos por página): {acessos_memoria}")

# Exemplo de uso
pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3]
num_frames = 3
fifo_page_replacement(pages, num_frames)
