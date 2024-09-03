import time

def lru_page_replacement(pages, num_frames):
    frames = []  # Armazenar as páginas na memória
    page_faults = 0  # Contar o número de faltas de página
    acessos_memoria = {page: 0 for page in set(pages)}  # Para medir a utilização da memória

    start_time = time.time()  # Iniciar a medição do tempo de execução

    for i in range(len(pages)):
        current_page = pages[i]

        if current_page not in frames:
            page_faults += 1
            if len(frames) < num_frames:
                frames.append(current_page)
            else:
                # Encontrar a página menos recentemente usada (LRU)
                lru_page = frames[0]
                for f in frames:
                    # Comparar a última vez que cada página foi usada
                    last_used_index = pages[:i].index(f) if f in pages[:i] else -1
                    lru_index = pages[:i].index(lru_page) if lru_page in pages[:i] else -1
                    if last_used_index < lru_index:
                        lru_page = f
                frames.remove(lru_page)
                frames.append(current_page)
        else:
            frames.remove(current_page)
            frames.append(current_page)
        
        # Atualizar contagem de acessos na memória
        if current_page in frames:
            acessos_memoria[current_page] += 1

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
    print(f"\nMétricas do Algoritmo LRU:")
    print(f"Total de Faltas de Página: {page_faults}")
    print(f"Taxa de Faltas de Página: {taxa_faltas:.2f}")
    print(f"Tempo Médio de Acesso: {tempo_medio_acesso:.2f} ms")
    print(f"Tempo de Execução do Algoritmo: {tempo_execucao:.6f} segundos")
    print(f"Utilização da Memória (acessos por página): {acessos_memoria}")

# Exemplo de uso
pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3]
num_frames = 3
lru_page_replacement(pages, num_frames)
