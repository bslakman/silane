# Data sources
database(
    thermoLibraries = ['SiliconHydrideLibrary', 'primaryThermoLibrary'],
    reactionLibraries = [('Silicon', False), ('Silicon_Giunta_1990', False), ('DolletSi2H4', False)],
    #reactionLibraries = [('Silicon_Giunta_1990', False)],
    seedMechanisms = [],
    kineticsDepositories = ['training'],
    kineticsFamilies = ['R_Recombination', 'Silylene_Insertion', 'Silylene_to_Silene', 'H_Abstraction'],
    kineticsEstimator = 'rate rules',
)

# List of species

######
# species to explicitly allow the ring opening reaction
species(
    label='cSi3H6',
    reactive=True,
    structure=SMILES("[SiH2]1[SiH2][SiH2]1"),
)

species(
    label='SiHSiH2SiH3',
    reactive=True,
    structure=adjacencyList("""
1 Si u0 p1 c0 {2,S} {3,S}
2 H  u0 p0 c0 {1,S}
3 Si u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4 H  u0 p0 c0 {3,S}
5 H  u0 p0 c0 {3,S}
6 Si u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
7 H  u0 p0 c0 {6,S}
8 H  u0 p0 c0 {6,S}
9 H  u0 p0 c0 {6,S}"""),
)
#####

species(
    label='SiH4',
    reactive=True,
    structure=SMILES("[SiH4]")
)

species(
    label='Si2H6',
    reactive=True,
    structure=SMILES("[SiH3][SiH3]")
)

species(
    label='SiH3',
    reactive=True,
    structure=SMILES("[SiH3]")
)

species(
    label='Si2H5',
    reactive=True,
    structure=SMILES("[SiH3][SiH2]")
)

species(
    label='SiH2',
    reactive=True,
    structure=adjacencyList("""
1 Si u0 p1 c0 {2,S} {3,S}
2 H  u0 p0 c0 {1,S}
3 H  u0 p0 c0 {1,S}
""")
)

species(
    label='SiH3SiH',
    reactive=True,
    structure=adjacencyList("""
1 Si u0 p1 c0 {2,S} {3,S}
2 H  u0 p0 c0 {1,S}
3 Si u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4 H  u0 p0 c0 {3,S}
5 H  u0 p0 c0 {3,S}
6 H  u0 p0 c0 {3,S}
""")
)



species(
    label='Ar',
    reactive=False,
    structure=SMILES("[Ar]")
)

# Reaction system
simpleReactor(
    temperature=(613,'K'),
    pressure=(39000,'Pa'),
    initialMoleFractions={
        "SiH4": 0.00016,
	"Ar": 0.99984,
    },
    terminationConversion={
        'SiH4': 0.9,
    },
    terminationTime=(1e8, 's')
)

simpleReactor(
    temperature=(813,'K'),
    pressure=(39000,'Pa'),
    initialMoleFractions={
        "SiH4": 0.00016,
	"Ar": 0.99984,
    },
    terminationConversion={
        'SiH4': 0.99,
    },
    terminationTime=(1e7, 's')
)

simpleReactor(
    temperature=(863,'K'),
    pressure=(39000,'Pa'),
    initialMoleFractions={
        "SiH4": 0.00016,
	"Ar": 0.99984,
    },
    terminationConversion={
        'SiH4': 0.99,
    },
    terminationTime=(1e6, 's')
)

simpleReactor(
    temperature=(913,'K'),
    pressure=(39000,'Pa'),
    initialMoleFractions={
        "SiH4": 0.00016,
	"Ar": 0.99984,
    },
    terminationConversion={
        'SiH4': 0.999,
    },
    terminationTime=(1e6, 's')
)


simulator(
    atol=1e-24,
    rtol=1e-12,
)

model(
    toleranceKeepInEdge=0.0,
    toleranceMoveToCore=1e-2,
    toleranceInterruptSimulation=1e-2,
    maximumEdgeSpecies=100000
)

pressureDependence(
    method='modified strong collision',
    maximumGrainSize=(0.5,'kcal/mol'),
    minimumNumberOfGrains=250,
    temperatures=(300,2000,'K',8),
    pressures=(0.01,20,'bar',5),
    interpolation=('Chebyshev', 6, 4),
)

options(
    units='si',
    saveRestartPeriod=None,
    generateOutputHTML=True,
    generatePlots=False,
    saveEdgeSpecies=True,
)

generatedSpeciesConstraints(
    allowed = ['reaction libraries'],
    maximumSiliconAtoms=3
)


