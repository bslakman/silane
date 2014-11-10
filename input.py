# Data sources
database(
    thermoLibraries = ['SiliconHydrideLibrary', 'primaryThermoLibrary'],
    reactionLibraries = [('Silicon_Giunta_1990', False), ('DolletSi2H4', False)],
    seedMechanisms = [],
    kineticsDepositories = ['training'],
    kineticsFamilies = ['Silylene_Insertion', 'Silylene_to_Silene', 'H_Abstraction', 'H2_transfer'],
    kineticsEstimator = 'rate rules',
)

# List of species
species(
    label='SiH4',
    reactive=True,
    structure=adjacencyList("""
	1 Si u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
	2 H u0 p0 c0 {1,S}
	3 H u0 p0 c0 {1,S}
	4 H u0 p0 c0 {1,S}
	5 H u0 p0 c0 {1,S}
	""")
)

#species(
#    label='H2',
#    reactive=True,
#    structure=SMILES("[H][H]")
#)


species(
    label='SiH3',
    reactive=True,
    structure=adjacencyList("""
	1 Si u1 p0 c0 {2,S} {3,S} {4,S}
	2 H u0 p0 c0 {1,S}
	3 H u0 p0 c0 {1,S}
	4 H u0 p0 c0 {1,S}
	""")
)

species(
    label='Si2H2',
    reactive=True,
    structure=adjacencyList("""
	1 Si u0 p1 c0 {2,S} {3,S}      
	2 H u0 p0 c0 {1,S}
	3 Si u0 p1 c0 {1,S} {4,S}
	4 H u0 p0 c0 {3,S}
	""")
)

species(
    label='Si2H4',
    reactive=True,
    structure=adjacencyList("""
	1 Si u0 p0 c0 {2,D} {3,S} {4,S}
	2 Si u0 p0 c0 {1,D} {5,S} {6,S}
	3 H u0 p0 c0 {1,S}
	4 H u0 p0 c0 {1,S}
	5 H u0 p0 c0 {2,S}
	6 H u0 p0 c0 {2,S}
	""")
)

species(
    label='Si2H6',
    reactive=True,
    structure=adjacencyList("""
	1 Si u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
	2 Si u0 p0 c0 {1,S} {5,S} {6,S} {8,S}
	3 H u0 p0 c0 {1,S}
	4 H u0 p0 c0 {1,S}
	5 H u0 p0 c0 {2,S}
	6 H u0 p0 c0 {2,S}
	7 H u0 p0 c0 {1,S}
	8 H u0 p0 c0 {2,S}
	""")
)

species(
    label='He',
    reactive=False,
    structure=SMILES("[He]")
)

species(
    label='SiH3SiH',
    reactive=True,
    structure=adjacencyList("""
	1 Si u0 p1 c0 {2,S} {3,S}
	2 Si u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
	3 H u0 p0 c0 {1,S}
	4 H u0 p0 c0 {2,S}
	5 H u0 p0 c0 {2,S}
	6 H u0 p0 c0 {2,S}
	""")
)

species(
    label='Si3H8',
    reactive=True,
    structure=adjacencyList("""
	1 Si u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
	2 Si u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
	3 H u0 p0 c0 {1,S}
	4 H u0 p0 c0 {1,S}
	5 H u0 p0 c0 {1,S}
	6 Si u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
	7 H u0 p0 c0 {2,S}
	8 H u0 p0 c0 {2,S}
	9 H u0 p0 c0 {6,S}
	10 H u0 p0 c0 {6,S}
	11 H u0 p0 c0 {6,S}
	""")
)

species(
    label='Si',
    reactive=True,
    structure=adjacencyList("""
	1 Si u2 p1 c0
	""")
)

species(
    label='SiH',
    reactive=True,
    structure=adjacencyList("""
	1 Si u1 p1 c0 {2,S}
	2 H u0 p0 c0 {1,S}
	""")
)

species(
    label='SiH2Si',
    reactive=True,
    structure=adjacencyList("""
	1 Si u0 p0 c0 {2,D} {3,S} {4,S}
	2 Si u2 p0 c0 {1,D}
	3 H u0 p0 c0 {1,S}
	4 H u0 p0 c0 {1,S}
	""")
)

species(
    label='H2Si',
    reactive=True,
    structure=adjacencyList("""
	1 Si u2 p0 c0 {2,S} {3,S}
	2 H u0 p0 c0 {1,S}
	3 H u0 p0 c0 {1,S}
	""")
)

species(
    label='H6Si3',
    reactive=True,
    structure=adjacencyList("""
	1 Si u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
	2 Si u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
	3 Si u0 p1 c0 {1,S} {2,S}
	4 H u0 p0 c0 {1,S}
	5 H u0 p0 c0 {1,S}
	6 H u0 p0 c0 {1,S}
	7 H u0 p0 c0 {2,S}
	8 H u0 p0 c0 {2,S}
	9 H u0 p0 c0 {2,S}
	""")
)

species(
    label='H3Si2',
    reactive=True,
    structure=adjacencyList("""
	1 Si u0 p0 c0 {2,D} {3,S} {4,S}
	2 Si u1 p0 c0 {1,D} {5,S}      
	3 H u0 p0 c0 {1,S}
	4 H u0 p0 c0 {1,S}
	5 H u0 p0 c0 {2,S}
	""")
)

species(
    label='H2Si2',
    reactive=True,
    structure=adjacencyList("""
	1 Si u0 p0 c0 {2,D} {3,S} {4,S}
	2 Si u0 p1 c0 {1,D}            
	3 H u0 p0 c0 {1,S}
	4 H u0 p0 c0 {1,S}
	""")
)

species(
    label='H5Si2',
    reactive=True,
    structure=adjacencyList("""
	1 Si u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
	2 Si u1 p0 c0 {1,S} {6,S} {7,S}
	3 H u0 p0 c0 {1,S}
	4 H u0 p0 c0 {1,S}
	5 H u0 p0 c0 {1,S}
	6 H u0 p0 c0 {2,S}
	7 H u0 p0 c0 {2,S}
	""")
)

species(
    label='H8Si4',
    reactive=True,
    structure=adjacencyList("""
	1 Si u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
	2 Si u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
	3 Si u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
	4 Si u0 p1 c0 {2,S} {12,S}
	5 H u0 p0 c0 {1,S}
	6 H u0 p0 c0 {1,S}
	7 H u0 p0 c0 {2,S}
	8 H u0 p0 c0 {2,S}
	9 H u0 p0 c0 {3,S}
	10 H u0 p0 c0 {3,S}
	11 H u0 p0 c0 {3,S}
	12 H u0 p0 c0 {4,S}
	""")
)

species(
    label='H',
    reactive=True,
    structure=adjacencyList("""
	1 H u1 p0 c0
	""")
)

# Reaction systems
simpleReactor(
    temperature=(550, 'K'),
    pressure=(5,'torr'),
    initialMoleFractions={
        "SiH4": 0.01,
#	"H2": 0.9,
	"SiH3": 0.0,
	"Si2H2": 0.0,
	"Si2H4": 0.0,
	"Si2H6": 0.0,
	"He": 0.99,
	"SiH3SiH": 0.0,
	"Si3H8": 0.0,
	"Si": 0.0,
	"SiH2Si": 0.0,
	"H2Si": 0.0,
	"H6Si3": 0.0,
	"H3Si2": 0.0,
	"H2Si2": 0.0,
	"H5Si2": 0.0,
	"H8Si4": 0.0,
	"H": 0.0,
	"SiH": 0.0,
    },
    terminationConversion={
        'SiH4': 0.9,
    },
    terminationTime=(1e6, 's'),
)

simulator(
    atol=1e-16,
    rtol=1e-8,
)

model(
    toleranceKeepInEdge=0.0,
    toleranceMoveToCore=0.001,
    toleranceInterruptSimulation=0.1,
    maximumEdgeSpecies=100000
)

options(
    units='si',
    saveRestartPeriod=None,
    drawMolecules=False,
    generatePlots=False,
    saveEdgeSpecies=True,
    saveConcentrationProfiles=True,
)
