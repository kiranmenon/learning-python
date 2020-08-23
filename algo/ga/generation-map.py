import random

POPULATION_SIZE = 100

GENES  = "abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ"

TARGET_GENOME = "I LOVE INDIA"

def mutated_genes():
    global GENES
    return random.choice(GENES)

def create_genome():
    global GENES
    return [mutated_genes() for _ in range(len(TARGET_GENOME))]

class Individual(object):

    def __init__(self, genome):
        self.genome = genome
        self.fitness = self.calc_fitness()

    def mate(self, partner):
        child_genome = []

        for gene_parent1, gene_parent2 in zip(self.genome, partner.genome):
            prob = random.random()

            if prob < 0.45 :
                child_genome.append(gene_parent1)
            elif prob < 0.90 :
                child_genome.append(gene_parent2)
            else:
                child_genome.append(mutated_genes())

        return Individual(child_genome)

    def calc_fitness(self):
        fitness = 0
        global TARGET_GENOME

        for gene_self, gene_target in zip(self.genome, TARGET_GENOME):
            if gene_self != gene_target:
                fitness += 1

        return fitness


def main():
    global POPULATION_SIZE
    space = []
    #create population
    for _ in range(POPULATION_SIZE):
        genome = create_genome()
        individual = Individual(genome)
        space.append(individual)

    found = False
    generation = 1

    while not found:
        
        population = sorted(space, key = lambda individual:
                individual.fitness)

        if population[0].fitness <= 0 :
            found = True
            break

        new_generation = []
        s = int(0.1 * POPULATION_SIZE)
        new_generation.extend(population[:s])

        s = int(0.9 * POPULATION_SIZE)
        for _ in range(s):
            parent1 = random.choice(population[:50])
            parent2 = random.choice(population[:50])
            offspring = parent1.mate(parent2)
            new_generation.append(offspring)

        space = new_generation

        print("Generation: {} \t Genome: {} \t fitness: {}\n".format(generation, "".join(population[0].genome),population[0].fitness))
        generation += 1

    print("Generation: {} \t Genome: {} \t fitness: {}\n".format(generation, "".join(population[0].genome),population[0].fitness))

if __name__=='__main__':
    main()



      
