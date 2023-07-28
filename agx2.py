import random
import math
# função fitness que determina o resultado daquele gene
def fitness(x):
    x = int(x, base=2)
    return x**2

def torneio(populacao):
    x1 = random.choice(populacao)
    x2 = random.choice(populacao)
    if fitness(x1) > fitness(x2):
        return x1
    else:
        return x2

def crossover(pai1, pai2):
    separador = random.randint(1, len(pai1)-1)
    filho1 = pai1[:separador] + pai2[separador:]
    filho2 = pai2[:separador] + pai1[separador:]
    return filho1, filho2

def mutacao(individuo):
    new_individuo = ''
    for i in individuo:
        chance_mutacao = random.randint(1, 100)
        if chance_mutacao == 1:
            if i == '1':
                new_individuo += '0'
            else:
                new_individuo += '1'
        else:
            new_individuo += i
    return new_individuo

def nova_geracao(populacao):
    nova_geracao = []

    while len(nova_geracao) < len(populacao):
        pai1 = torneio(populacao)
        pai2 = torneio(populacao)

        if random.randint(1, 100) <= 80:
            filho1, filho2 = crossover(pai1, pai2)
        else:
            filho1, filho2 = pai1, pai2

        filho1 = mutacao(filho1)
        filho2 = mutacao(filho2)

        nova_geracao.append(filho1)
        nova_geracao.append(filho2)
    return nova_geracao

def criterio_de_parada(geracao, melhor_fitness):
    return geracao >= max_geracoes or melhor_fitness >= max_fitness

def algoritmo_genetico(populacao):
    geracao = 1
    melhor_fitness = max(fitness(individuo) for individuo in populacao)
    melhor_individuo = math.sqrt(melhor_fitness)
    
    while not criterio_de_parada(geracao, melhor_fitness):
        populacao = nova_geracao(populacao)

        novo_melhor_fitness = max(fitness(individuo) for individuo in populacao)
        novo_melhor_individuo = math.sqrt(novo_melhor_fitness)

        if novo_melhor_fitness > melhor_fitness:
            melhor_fitness = novo_melhor_fitness
            melhor_individuo = novo_melhor_individuo
        


    return melhor_individuo, melhor_fitness

if __name__ == '__main__':
    tamanho_cromossomo = 5
    tamanho_populacao = 50
    populacao = [''.join(random.choice('01') for i in range(tamanho_cromossomo)) for j in range(tamanho_populacao)]
    max_geracoes = 1000
    max_fitness = 31**2


    melhor_individuo, melhor_fitness = algoritmo_genetico(populacao)
    print('Melhor indivíduo encontrado:', melhor_individuo)
    print('Mair valor de x ao quadrado encontrado:', melhor_fitness)
