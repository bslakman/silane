# Data sources
database(
    thermoLibraries = ['SiliconHydrideLibrary', 'primaryThermoLibrary'],
#    reactionLibraries = [('Silicon_Giunta_1990', False), ('DolletSi2H4', False)],
#    seedMechanisms = ['Silicon_Giunta_1990'],
    kineticsDepositories = ['training'],
    kineticsFamilies = ['H_Abstraction', 'Silylene_Insertion', 'Silylene_to_Silene', 'R_Recombination'],
    kineticsEstimator = 'rate rules',
)

# List of species
species(
    label='H2',
    reactive=True,
    structure=SMILES("[H][H]")
)

species(
    label='Si2H2_T',
    reactive=True,
    structure=adjacencyList("""
1 Si u2 p0 c0 {2,D}
2 Si u0 p0 c0 {1,D} {3,S} {4,S}
3 H u0 p0 c0 {2,S}
4 H u0 p0 c0 {2,S}
""")
)

species(
    label='H3SiSiH',
    reactive=True,
    structure=adjacencyList("""
1 Si u0 p1 c0 {2,S} {5,S}
2 Si u0 p0 c0 {1,S} {3,S} {4,S} {6,S}
3 H u0 p0 c0 {2,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
""")
)

species(
    label='Ar',
    reactive=False,
    structure=SMILES("[Ar]")
)

# Reaction system
simpleReactor(
    temperature=(873,'K'),
    pressure=(39000,'Pa'),
    initialMoleFractions={
        "H2": 0.49,
        "Si2H2_T": 0.49,
        "Ar": 0.02
    },
    terminationConversion={
        'Si2H2_T': 0.9,
    },
#    terminationTime=(1, 's')
)

## Reaction system
#simpleReactor(
#    temperature=(873,'K'),
#    pressure=(39000,'Pa'),
#    initialMoleFractions={
#        "SiH4": 0.0025,
#	"Ar": 0.9975,
#    },
#    terminationConversion={
#        'SiH4': 0.9,
#    },
##    terminationTime=(1, 's')
#)
#
## Reaction system
#simpleReactor(
#    temperature=(873,'K'),
#    pressure=(39000,'Pa'),
#    initialMoleFractions={
#        "SiH4": 0.05,
#	"Ar": 0.95,
#    },
#    terminationConversion={
#        'SiH4': 0.9,
#    },
# #   terminationTime=(1, 's')
#)
#
#simulator(
#    atol=1e-16,
#    rtol=1e-8,
#)
#
#model(
#    toleranceKeepInEdge=0.0,
#    toleranceMoveToCore=0.01,
#    toleranceInterruptSimulation=0.05,
#    maximumEdgeSpecies=100000
#)
#
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

#generatedSpeciesConstraints(
#    maximumSiliconAtoms=3
#)


