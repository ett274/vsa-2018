# proj10_extension
#
# Name:
# Date:


import random

from proj10 import *


#
# PROBLEM 1
#
class ResistantVirus(SimpleVirus):
    """
    Representation of a virus which can have drug resistance.
    """

    def __init__(self, maxBirthProb, clearProb, resistances, mutProb):

        """

        Initialize a ResistantVirus instance, saves all parameters as attributes
        of the instance.

        maxBirthProb: Maximum reproduction probability (a float between 0-1)        
        clearProb: Maximum clearance probability (a float between 0-1).

        resistances: A dictionary of drug names (strings) mapping to the state
        of this virus particle's resistance (either True or False) to each drug.
        e.g. {'drug_a':False, 'drug_b',False}, means that this virus
        particle is resistant to neither drug_a nor drug_b.

        mutProb: Mutation probability for this virus particle (a float). This is
        the probability of the offspring acquiring or losing resistance to a drug.        

        """
        super(ResistantVirus, self).__init__(maxBirthProb, clearProb)
        self.maxBirthProb = maxBirthProb
        self.clearProb = clearProb
        self.resistances = resistances
        self.mutProb = mutProb

    def doesClear(self):
        """ Stochastically determines whether this virus particle is cleared from the
        patient's body at a time step.
        returns: True with probability self.clearProb and otherwise returns
        False.
        """
        if random.random() <= self.clearProb:
            return True
        else:
            return False

    def isResistantTo(self, drug):

        """
        Get the state of this virus particle's resistance to a drug. This method
        is called by getResistPop() in Patient to determine how many virus
        particles have resistance to a drug.    

        drug: The drug (a string)
        returns: True if this virus instance is resistant to the drug, False
        otherwise.
        """
        if self.resistances[drug] is True:
            return True
        else:
            return False

        # TODO

    def reproducf(self, popDensity, activeDrugs):

        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the Patient class.

        If the virus particle is not resistant to any drug in activeDrugs,
        then it does not reproduce. Otherwise, the virus particle reproduces
        with probability:       
        
        self.maxBirthProb * (1 - popDensity).                       
        
        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring ResistantVirus (which has the same
        maxBirthProb and clearProb values as its parent). 

        For each drug resistance trait of the virus (i.e. each key of
        self.resistances), the offspring has probability 1-mutProb of
        inheriting that resistance trait from the parent, and probability
        mutProb of switching that resistance trait in the offspring.        

        For example, if a virus particle is resistant to drug_a but not
        drug_b, and `self.mutProb` is 0.1, then there is a 10% chance that
        that the offspring will lose resistance to drug_a and a 90% 
        chance that the offspring will be resistant to drug_a.
        There is also a 10% chance that the offspring will gain resistance to
        drug_b and a 90% chance that the offspring will not be resistant to
        drug_b.

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population        

        activeDrugs: a list of the drug names acting on this virus particle
        (a list of strings). 
        
        returns: a new instance of the ResistantVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.         
        """
        if len(activeDrugs) > 0:
            for drig in activeDrugs:
                if self.isResistantTo(drig) is False:
                    raise NoChildException
        if random.random() <= self.maxBirthProb * (1 - popDensity):
            child_resistance = self.resistances
            for drug in self.resistances:
                if self.isResistantTo(drug) is True:
                    if random.random() <= (1 - self.mutProb):
                        child_resistance[drug] = True
                    else:
                        child_resistance[drug] = False
                else:
                    if random.random() <= (1 - self.mutProb):
                        child_resistance[drug] = False
                    else:
                        child_resistance[drug] = True
            return ResistantVirus(self.maxBirthProb, self.clearProb, child_resistance, self.mutProb)
        else:
            raise NoChildException


class Patient(SimplePatient):
    """
    Representation of a patient. The patient is able to take drugs and his/her
    virus population can acquire resistance to the drugs he/she takes.
    """

    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes. Also initializes the list of drugs being administered
        (which should initially include no drugs).               

        viruses: the list representing the virus population (a list of
        SimpleVirus instances)
        
        maxPop: the  maximum virus population for this patient (an integer)
        """

        super(Patient, self).__init__(viruses, maxPop)
        self.viruses = viruses
        self.maxPop = maxPop
        self.drugs = []

    def addPrescription(self, newDrug):

        """
        Administer a drug to this patient. After a prescription is added, the 
        drug acts on the virus population for all subsequent time steps. If the
        newDrug is already prescribed to this patient, the method has no effect.

        newDrug: The name of the drug to administer to the patient (a string).

        postcondition: list of drugs being administered to a patient is updated
        """
        # TODO
        # should not allow one drug being added to the list multiple times
        if newDrug not in self.drugs:
            self.drugs.append(newDrug)

    def getPrescriptions(self):

        """
        Returns the drugs that are being administered to this patient.
        returns: The list of drug names (strings) being administered to this
        patient.
        """
        return self.drugs

    def getResistPop(self, drugResist):
        """
        Get the population of virus particles resistant to the drugs listed in 
        drugResist.        

        drugResist: Which drug resistances to include in the population (a list
        of strings - e.g. ['drug_a'] or ['drug_a', 'drug_b'])

        returns: the population of viruses (an integer) with resistances to all
        drugs in the drugResist list.
        """
        resistant_viruses = []
        for drug in drugResist:
            for virus in self.viruses:
                if virus.isResistantTo(drug) is True and virus not in resistant_viruses:
                    resistant_viruses.append(virus)
        return len(resistant_viruses)

        # TODO

    def update(self):

        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute these actions in order:
        
        - Determine whether each virus particle survives and update the list of 
          virus particles accordingly          
        - The current population density is calculated. This population density
          value is used until the next call to update().
        - Determine whether each virus particle should reproduce and add
          offspring virus particles to the list of viruses in this patient. 
          The listof drugs being administered should be accounted for in the
          determination of whether each virus particle reproduces. 

        returns: the total virus population at the end of the update (an
        integer)
        """
        # TODO
        for virus in self.viruses:
            if virus.doesClear() is True:
                self.viruses.remove(virus)
        popDens = float(self.getTotalPop()) / float(self.maxPop)
        for virus in self.viruses:
            try:
                self.viruses.append(virus.reproducf(popDens, self.getPrescriptions()))
            except NoChildException:
                pass

        return len(self.viruses)


#
# PROBLEM 2
#

def simulationWithDrug(number_of_viruses):
    """

    Runs simulations and plots graphs for problem 4.
    Instantiates a patient, runs a simulation for 150 timesteps, adds
    drug_a, and runs the simulation for an additional 150 timesteps.
    total virus population vs. time and drug_a-resistant virus population
    vs. time are plotted
    """
    # TODO
    some_viruses = []
    for x in range(number_of_viruses + 1):
        some_viruses.append(ResistantVirus(0.1, 0.05, {"drug_a": False}, 0.005))
    patient = Patient(some_viruses, 1000)
    for m in range(151):
        print str(m) + " " + str(patient.update()) + " " + str(patient.getResistPop(['drug_a']))
    patient.addPrescription("drug_a")
    for m in range(151, 301):
        print str(m) + " " + str(patient.update()) + " " + str(patient.getResistPop(['drug_a']))


#
# PROBLEM 3
#        

def simulationDelayedTreatment(trials):
    """
    Runs simulations and make histograms for problem 5.
    Runs multiple simulations to show the relationship between delayed treatment
    and patient outcome.
    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).    
    """
    timestamps = [300, 150, 75, 0]

    for timestamp in timestamps:
        for x in range(trials + 1):
            virus_list = []
            for m in range(101):
                virus_list.append(ResistantVirus(0.1,0.05, {"doge": False}, 0.005))
            person = Patient(virus_list, 1000)
            if timestamp != 0:
                for time in range(timestamp + 1):
                    person.update()
            person.addPrescription("doge")
            for tim in range(150):
                person.update()
            print person.update()
        print "----------"


#
# PROBLEM 4
#

def simulationTwoDrugsDelayedTreatment(trials):
    """
    Runs simulations and make histograms for problem 6.
    Runs multiple simulations to show the relationship between administration
    of multiple drugs and patient outcome.
   
    Histograms of final total virus populations are displayed for lag times of
    150, 75, 0 timesteps between adding drugs (followed by an additional 150
    timesteps of simulation).
    """
    timestamps = [300, 150, 75, 0]
    for timestamp in timestamps:
        for x in range(trials + 1):
            virus_list = []
            for m in range(101):
                virus_list.append(ResistantVirus(0.1,0.05, {"drug_a": False, "drug_b": False}, 0.005))
            person = Patient(virus_list, 1000)
            for t in range(151):
                person.update()
            person.addPrescription("drug_a")
            if timestamp != 0:
                for t in range(timestamp + 1):
                    person.update()
            person.addPrescription("drug_b")
            for t in range(150):
                person.update()
            print person.update()
        print "----------"



#
# PROBLEM 5
#    

def simulationTwoDrugsVirusPopulations(trials):
    """

    Run simulations and plot graphs examining the relationship between
    administration of multiple drugs and patient outcome.
    Plots of total and drug-resistant viruses vs. time are made for a
    simulation with a 300 time step delay between administering the 2 drugs and
    a simulations for which drugs are administered simultaneously.        

    """
    for x in range(trials + 1):
        virus_list = []
        for m in range(101):
            virus_list.append(ResistantVirus(0.1, 0.05, {"drug_a": False, "drug_b": False}, 0.005))
        person = Patient(virus_list, 1000)
        for t in range(151):
            person.update()
        person.addPrescription("drug_a")
        for t in range(301):
            person.update()
        person.addPrescription("drug_b")
        for t in range(150):
            person.update()
        print person.update()
    print "--------"
    for x in range(trials + 1):
        virus_list = []
        for m in range(101):
            virus_list.append(ResistantVirus(0.1, 0.05, {"drug_a": False, "drug_b": False}, 0.005))
        person = Patient(virus_list, 1000)
        for t in range(151):
            person.update()
        person.addPrescription("drug_a")
        person.addPrescription("drug_b")
        for t in range(150):
            person.update()
        print person.update()


simulationWithDrug(100)