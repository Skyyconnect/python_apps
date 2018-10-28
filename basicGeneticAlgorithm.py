from random import randint 
from time import sleep
from math import *



class Individual:
  def __init__(self, genLength):
    self.genLength = genLength
    self.genes = []
    self.fitness = 0
    self.isOffspring = False
    
    
  def birth(self):
    for i in range(self.genLength):
      self.genes.append(randint(0,1))
     
      
  def calculateFitness(self):
    self.fitness = 0
    for i in range(len(self.genes)):
      if self.genes[i] == 1:
        self.fitness +=1
        
        
class Population:
  def __init__(self, populationSize, geneLength):
    self.populationSize = populationSize
    self.individuals = []
    self.fittest = 0
    self.geneLength = geneLength
    self.topPair = [None,None]
    self.generation = 0
    self.totalOffspring = 0
    
  def createPopulations(self):
    for i in range(self.populationSize):
      child = Individual(self.geneLength)
      child.birth()
      child.calculateFitness()
      self.individuals.append(child)
   
    
  def getFittest(self):
    maxFit = 0
    maxFitIndex = 0
    for i in range(self.populationSize):
      if maxFit <= self.individuals[i].fitness:
        maxFit = self.individuals[i].fitness
        maxFitIndex = i
    self.fittest = self.individuals[maxFitIndex].fitness
    self.topPair[0] = self.individuals[maxFitIndex]
    return self.individuals[maxFitIndex]
  
  def getSecondFittest(self):
    maxFit1 = 0
    maxFit2 = 0
    for i in range(self.populationSize):
      if self.individuals[i].fitness > self.individuals[maxFit1].fitness:
        maxFit2 = maxFit1
        maxFit1 = i
      elif self.individuals[i].fitness > self.individuals[maxFit2].fitness:
        maxFit2 = i
    self.topPair[1] = self.individuals[maxFit2]
    return self.individuals[maxFit2]
    
  def leastFittest(self):
    minFit = 0
    minIndex = 0
    for i in range(self.populationSize):
      if minFit >= self.individuals[i].fitness:
        minFit = self.individuals[i].fitness
        minIndex = i
    return self.individuals[minIndex]
    
  def calculateFitness(self):
    for i in range(len(self.individuals)):
      self.individuals[i].calculateFitness()
    self.getFittest()
    
  
def selection(population):
  population.getFittest()
  population.getSecondFittest()
  return population.topPair
  
def crossOver(population):
  selected = selection(population)
  offspring = Individual(selected[0].genLength)
  crossOverPoint = randint(0, len(selected[0].genes)-1)
  for i in range(crossOverPoint):
    selected[0].genes[i],selected[1].genes[i] = selected[1].genes[i],selected[0].genes[i]
  offspring.genes = selected[randint(0,1)].genes
  offspring.isOffspring = True
  if offspring.fitness < offspring.genLength:
    mutation(offspring)
  offspring.calculateFitness()
  return offspring
  
def mutation(individual):
  for i in range(randint(1,2)):
    switchGene(individual.genes[randint(0, len(individual.genes)-1)])
  return individual
  
def reselect(mutatedIndividual, population):
  selected = selection(pop)
  for i in range(3):
    replace = randint(0, population.populationSize-1)
    if not population.individuals[replace].isOffspring:
      if i == 0:
        population.individuals[replace] = mutatedIndividual
      elif i == 1:
        population.individuals[replace] = selected[0]
      else:
        population.individuals[replace] = selected[1]
    return population
        
        
def switchGene(gene):
  if gene == 1:
    gene = 0
  else:
    gene = 1
  return gene
  
def totalFitness(pop):
  collective = 0
  for i in range(len(pop.individuals)):
    collective += pop.individuals[i].fitness
  return collective  
  
  
  
def goToNextGen(population):
  for i in range(population.populationSize):
    if population.individuals[i].isOffspring:
      population.individuals[i].isOffspring = False
  
  
perfect = 0  
pop = Population(100, 5)
pop.createPopulations()
maxOffSpring = 10

def life():
  perfect = 0
  offspring = crossOver(pop)
  pop.totalOffspring +=1
  reselect(offspring, pop)
  if pop.totalOffspring > maxOffSpring :
    pop.generation +=1
    print "Generation:  " + str(pop.generation)
    print "total fitness: " + str(totalFitness(pop))
    goToNextGen(pop)
    pop.totalOffspring = 0
    for each in pop.individuals:
      if each.fitness >= each.genLength:
        perfect +=1
  if totalFitness(pop) == (pop.populationSize*pop.geneLength):
      print "we are complete"
      return False
  else:
    return True
      
print (pop.populationSize*pop.geneLength)-1
while life():
  pass
      
     
      
    
    
    
  


  


      


   
   
  
    
    
    
    
    
  
    

    