# Data sources
database(
    thermoLibraries = ['SiliconHydrideLibrary', 'primaryThermoLibrary'],
    #reactionLibraries = [('Silicon_Giunta_1990', False), ('DolletSi2H4', False)],
    reactionLibraries = [('Silicon_Giunta_1990', False)],
    #seedMechanisms = [('Silicon_Giunta_1990')],
    seedMechanisms = [],
    kineticsDepositories = ['training'],
    kineticsFamilies = ['R_Recombination', 'Silylene_Insertion', 'Silylene_to_Silene', 'H_Abstraction'],
    kineticsEstimator = 'rate rules',
)

# List of species
species(
    label='SiH4',
    reactive=True,
    structure=SMILES("[SiH4]")
)

species(
    label='Ar',
    reactive=False,
    structure=SMILES("[Ar]")
)

#species(
#    label='SiH2',
#    reactive=True,
#    structure=adjacencyList("""
#1 Si u0 p1 c0 {2,S} {3,S}
#2 H u0 p0 c0 {1,S}
#3 H u0 p0 c0 {1,S}
#""")
#)

# Reaction systems
simpleReactor(
    temperature=(913,'K'),
    pressure=(39000,'Pa'),
    initialMoleFractions={
        "SiH4": 0.00016,  
	"Ar": 0.99984,  
    },
    terminationConversion={
        'SiH4': 0.9,
    },
    terminationTime=(1, 's'),
#    sensitivity=['SiH4', 'SiH2'],
#    sensitivityThreshold=0.001,
)

# Reaction systems
simpleReactor(
    temperature=(863,'K'),
    pressure=(39000,'Pa'),
    initialMoleFractions={
        "SiH4": 0.00016,  
	"Ar": 0.99984,  
    },
    terminationConversion={
        'SiH4': 0.9,
    },
    terminationTime=(1, 's'),
#    sensitivity=['SiH4', 'SiH2'],
#    sensitivityThreshold=0.001,
)

# Reaction systems
simpleReactor(
    temperature=(963,'K'),
    pressure=(39000,'Pa'),
    initialMoleFractions={
        "SiH4": 0.00016,  
	"Ar": 0.99984,  
    },
    terminationConversion={
        'SiH4': 0.9,
    },
    terminationTime=(1, 's'),
#    sensitivity=['SiH4', 'SiH2'],
#    sensitivityThreshold=0.001,
)

simpleReactor(
    temperature=(913,'K'),
    pressure=(19500,'Pa'),
    initialMoleFractions={
        "SiH4": 0.00016,  
	"Ar": 0.99984,  
    },
    terminationConversion={
        'SiH4': 0.9,
    },
    terminationTime=(1, 's'),
#    sensitivity=['SiH4', 'SiH2'],
#    sensitivityThreshold=0.001,
)

simpleReactor(
    temperature=(913,'K'),
    pressure=(78000,'Pa'),
    initialMoleFractions={
        "SiH4": 0.00016,  
	"Ar": 0.99984,  
    },
    terminationConversion={
        'SiH4': 0.9,
    },
    terminationTime=(1, 's'),
#    sensitivity=['SiH4', 'SiH2'],
#    sensitivityThreshold=0.001,
)

simpleReactor(
    temperature=(913,'K'),
    pressure=(39000,'Pa'),
    initialMoleFractions={
        "SiH4": 0.000032,  
	"Ar": 0.999968,  
    },
    terminationConversion={
        'SiH4': 0.9,
    },
    terminationTime=(1, 's'),
#    sensitivity=['SiH4', 'SiH2'],
#    sensitivityThreshold=0.001,
)

simpleReactor(
    temperature=(913,'K'),
    pressure=(39000,'Pa'),
    initialMoleFractions={
        "SiH4": 0.0008,  
	"Ar": 0.9992,  
    },
    terminationConversion={
        'SiH4': 0.9,
    },
    terminationTime=(1, 's'),
#    sensitivity=['SiH4', 'SiH2'],
#    sensitivityThreshold=0.001,
)

simulator(
    atol=1e-16,
    rtol=1e-8,
)

model(
    toleranceKeepInEdge=0.0,
    toleranceMoveToCore=1e-3,
    toleranceInterruptSimulation=5e-3,
    maximumEdgeSpecies=100000
)

#pressureDependence(
#    method='modified strong collision',
#    maximumGrainSize=(0.5,'kcal/mol'),
#    minimumNumberOfGrains=250,
#    temperatures=(300,2000,'K',8),
#    pressures=(0.01,20,'bar',5),
#    interpolation=('Chebyshev', 6, 4),
#)

options(
    units='si',
    saveRestartPeriod=None,
    generateOutputHTML=True,
    generatePlots=False,
    saveEdgeSpecies=True,
)

generatedSpeciesConstraints(
    maximumSiliconAtoms=6
)


