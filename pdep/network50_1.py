species(
    label = '[SiH]=[SiH][Si]=[SiH2](56)',
    structure = SMILES('[SiH]=[SiH][Si]=[SiH2]'),
    E0 = (685.001,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([300,800,800,800,800,800,1600,1600,1600,1600,1600],'cm^-1')),
        HinderedRotor(inertia=(0.156089,'amu*angstrom^2'), symmetry=1, barrier=(3.5888,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 3,
    opticalIsomers = 1,
    molecularWeight = (114.358,'amu'),
    collisionModel = TransportData(shapeIndex=2, epsilon=(4418.31,'J/mol'), sigma=(4.687e-10,'m'), dipoleMoment=(0,'C*m'), polarizability=(0,'angstroms^3'), rotrelaxcollnum=0, comment="""Epsilon & sigma estimated with fixed Lennard Jones Parameters. This is the fallback method! Try improving transport databases!"""),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[0.484725,0.0968623,-0.000217288,2.13171e-07,-7.51105e-11,82494.8,-0.671425], Tmin=(100,'K'), Tmax=(901.022,'K')), NASAPolynomial(coeffs=[6.48407,0.0220565,-1.2557e-05,2.35312e-09,-1.52647e-13,83369.1,-18.1384], Tmin=(901.022,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(685.001,'kJ/mol'), comment="""Thermo group additivity estimation: group(Sis-Sis4) + other(R) + group(Sid-H2) + other(R) + group(Sis-Sis4) + other(R) + group(si) + other(R) + radical(SidsJ_Si) + radical(SidsJ_Si)"""),
)

species(
    label = '[SiH]=[SiH2](22)',
    structure = SMILES('[SiH]=[SiH2]'),
    E0 = (530.145,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([180,180,180],'cm^-1')),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 1,
    molecularWeight = (57.1789,'amu'),
    collisionModel = TransportData(shapeIndex=2, epsilon=(920.412,'J/mol'), sigma=(4.443e-10,'m'), dipoleMoment=(0,'C*m'), polarizability=(0,'angstroms^3'), rotrelaxcollnum=0, comment="""Epsilon & sigma estimated with fixed Lennard Jones Parameters. This is the fallback method! Try improving transport databases!"""),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[2.96237,0.0285803,-5.77864e-05,5.81405e-08,-2.13832e-11,63793.6,20.2056], Tmin=(100,'K'), Tmax=(880.968,'K')), NASAPolynomial(coeffs=[3.37234,0.0126212,-6.60971e-06,1.24828e-09,-8.36523e-14,64268.4,21.3845], Tmin=(880.968,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(530.145,'kJ/mol'), comment="""Thermo group additivity estimation: group(Sid-H2) + other(R) + group(si) + other(R) + radical(SidsJ_Si)"""),
)

species(
    label = '[H](13)',
    structure = SMILES('[H]'),
    E0 = (211.805,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
    molecularWeight = (1.00794,'amu'),
    collisionModel = TransportData(shapeIndex=0, epsilon=(1205.6,'J/mol'), sigma=(2.05,'angstroms'), dipoleMoment=(0,'C*m'), polarizability=(0,'angstroms^3'), rotrelaxcollnum=0.0, comment="""GRI-Mech"""),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[2.5,1.37382e-15,-2.66902e-18,1.75563e-21,-3.60841e-25,25474.2,-0.444973], Tmin=(100,'K'), Tmax=(2121.2,'K')), NASAPolynomial(coeffs=[2.5,3.04115e-14,-1.54211e-17,3.31771e-21,-2.56694e-25,25474.2,-0.444973], Tmin=(2121.2,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(211.805,'kJ/mol'), comment="""Thermo library: primaryThermoLibrary"""),
)

species(
    label = '[SiH]=[Si][Si]=[SiH2](89)',
    structure = SMILES('[SiH]#[Si][Si][SiH2]'),
    E0 = (705.841,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([180,180,180,180,180,180,180,180],'cm^-1')),
        HinderedRotor(inertia=(2.0773,'amu*angstrom^2'), symmetry=1, barrier=(47.7613,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 4,
    opticalIsomers = 1,
    molecularWeight = (113.35,'amu'),
    collisionModel = TransportData(shapeIndex=2, epsilon=(4418.31,'J/mol'), sigma=(4.687e-10,'m'), dipoleMoment=(0,'C*m'), polarizability=(0,'angstroms^3'), rotrelaxcollnum=0, comment="""Epsilon & sigma estimated with fixed Lennard Jones Parameters. This is the fallback method! Try improving transport databases!"""),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[1.41629,0.0664438,-0.000135126,1.24789e-07,-4.23462e-11,84977,-13.6407], Tmin=(100,'K'), Tmax=(898.499,'K')), NASAPolynomial(coeffs=[8.36375,0.0125916,-6.95392e-06,1.2935e-09,-8.39246e-14,84653.9,-41.2656], Tmin=(898.499,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(705.841,'kJ/mol'), comment="""Thermo group additivity estimation: group(Sis-H3si) + other(R) + group(Sis-Sis4) + other(R) + group(si) + other(R) + group(Sis-Sis4) + other(R) + radical(SiJ_LP_Si) + radical(SiSiSi_triplet)"""),
)

species(
    label = '[SiH][SiH2][SiH]=[SiH2](90)',
    structure = SMILES('[SiH][SiH2][SiH]=[SiH2]'),
    E0 = (887.812,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([200,800,900,1000,1100,1200,1300,1400,1500,1600],'cm^-1')),
        HinderedRotor(inertia=(0.156089,'amu*angstrom^2'), symmetry=1, barrier=(3.5888,'kJ/mol'), semiclassical=False),
        HinderedRotor(inertia=(0.156089,'amu*angstrom^2'), symmetry=1, barrier=(3.5888,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 3,
    opticalIsomers = 1,
    molecularWeight = (114.358,'amu'),
    collisionModel = TransportData(shapeIndex=2, epsilon=(4418.31,'J/mol'), sigma=(4.687e-10,'m'), dipoleMoment=(0,'C*m'), polarizability=(0,'angstroms^3'), rotrelaxcollnum=0, comment="""Epsilon & sigma estimated with fixed Lennard Jones Parameters. This is the fallback method! Try improving transport databases!"""),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[0.662915,0.0870549,-0.000176483,1.65877e-07,-5.72535e-11,106886,24.5132], Tmin=(100,'K'), Tmax=(895.68,'K')), NASAPolynomial(coeffs=[8.05694,0.0212491,-1.13722e-05,2.11617e-09,-1.38457e-13,106877,-3.00284], Tmin=(895.68,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(887.812,'kJ/mol'), comment="""Thermo group additivity estimation: group(Sis-H3si) + other(R) + group(Sis-Sis4) + other(R) + group(si) + other(R) + group(si) + other(R) + radical(SiSiH_triplet)"""),
)

species(
    label = '[SiH2]=[Si]=[SiH2](64)',
    structure = SMILES('[SiH2]=[Si]=[SiH2]'),
    E0 = (551.673,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([180,180,180,180],'cm^-1')),
    ],
    spinMultiplicity = 1,
    opticalIsomers = 1,
    molecularWeight = (84.2565,'amu'),
    collisionModel = TransportData(shapeIndex=1, epsilon=(1971.36,'J/mol'), sigma=(5.118e-10,'m'), dipoleMoment=(0,'C*m'), polarizability=(0,'angstroms^3'), rotrelaxcollnum=0, comment="""Epsilon & sigma estimated with fixed Lennard Jones Parameters. This is the fallback method! Try improving transport databases!"""),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[0.952794,0.0653744,-0.000126072,1.16714e-07,-4.01367e-11,66433.8,18.3711], Tmin=(100,'K'), Tmax=(892.396,'K')), NASAPolynomial(coeffs=[6.4937,0.018306,-9.58623e-06,1.77625e-09,-1.16739e-13,66330.1,-2.7698], Tmin=(892.396,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(551.673,'kJ/mol'), comment="""Thermo group additivity estimation: group(Sis-Sis4) + other(R) + group(si) + other(R) + group(si) + other(R)"""),
)

species(
    label = '[SiH2](68)',
    structure = SMILES('[SiH2]'),
    E0 = (345.086,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([916.932,1866.07,2487.05],'cm^-1')),
    ],
    spinMultiplicity = 3,
    opticalIsomers = 1,
    molecularWeight = (30.1014,'amu'),
    collisionModel = TransportData(shapeIndex=2, epsilon=(1235.53,'J/mol'), sigma=(3.758e-10,'m'), dipoleMoment=(0,'C*m'), polarizability=(0,'angstroms^3'), rotrelaxcollnum=0, comment="""Epsilon & sigma estimated with fixed Lennard Jones Parameters. This is the fallback method! Try improving transport databases!"""),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[4.01986,-0.0010006,8.10767e-06,-7.50465e-09,2.19219e-12,41504,2.96499], Tmin=(100,'K'), Tmax=(1093.22,'K')), NASAPolynomial(coeffs=[3.2975,0.00387404,-1.64273e-06,3.08554e-10,-2.15527e-14,41528.6,5.90443], Tmin=(1093.22,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(345.086,'kJ/mol'), comment="""Thermo library: SiliconHydrideLibrary"""),
)

species(
    label = 'Si(8)',
    structure = SMILES('[SiH2]'),
    E0 = (444.552,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
    molecularWeight = (28.0855,'amu'),
    collisionModel = TransportData(shapeIndex=2, epsilon=(1235.53,'J/mol'), sigma=(3.758e-10,'m'), dipoleMoment=(0,'C*m'), polarizability=(0,'angstroms^3'), rotrelaxcollnum=0, comment="""Epsilon & sigma estimated with fixed Lennard Jones Parameters. This is the fallback method! Try improving transport databases!"""),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[2.5,1.37382e-15,-2.66902e-18,1.75563e-21,-3.60841e-25,53467.3,4.92941], Tmin=(100,'K'), Tmax=(2121.2,'K')), NASAPolynomial(coeffs=[2.5,3.04115e-14,-1.54211e-17,3.31771e-21,-2.56694e-25,53467.3,4.92941], Tmin=(2121.2,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(444.552,'kJ/mol'), comment="""Thermo library: SiliconHydrideLibrary"""),
)

species(
    label = '[SiH2]=[Si]=[SiH2](91)',
    structure = SMILES('[SiH2]=[Si]=[SiH2]'),
    E0 = (414.727,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([180,180,180,180,180,180,180,180,180],'cm^-1')),
    ],
    spinMultiplicity = 1,
    opticalIsomers = 1,
    molecularWeight = (86.2724,'amu'),
    collisionModel = TransportData(shapeIndex=2, epsilon=(1971.36,'J/mol'), sigma=(5.118e-10,'m'), dipoleMoment=(0,'C*m'), polarizability=(0,'angstroms^3'), rotrelaxcollnum=0, comment="""Epsilon & sigma estimated with fixed Lennard Jones Parameters. This is the fallback method! Try improving transport databases!"""),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[1.57575,0.0595463,-0.000105232,9.24967e-08,-3.08812e-11,49961.5,6.54957], Tmin=(100,'K'), Tmax=(880.354,'K')), NASAPolynomial(coeffs=[8.20167,0.0159642,-8.0131e-06,1.48704e-09,-9.87737e-14,49317.1,-21.6064], Tmin=(880.354,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(414.727,'kJ/mol'), comment="""Thermo group additivity estimation: group(Sid-H2) + other(R) + group(Sis-Sis4) + other(R) + group(si) + other(R)"""),
)

species(
    label = 'He',
    structure = SMILES('[He]'),
    E0 = (-6.19738,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
    molecularWeight = (4.0026,'amu'),
    collisionModel = TransportData(shapeIndex=2, epsilon=(1235.53,'J/mol'), sigma=(3.758e-10,'m'), dipoleMoment=(0,'C*m'), polarizability=(0,'angstroms^3'), rotrelaxcollnum=0, comment="""Epsilon & sigma estimated with fixed Lennard Jones Parameters. This is the fallback method! Try improving transport databases!"""),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[2.5,0,0,0,0,-745.375,0.928724], Tmin=(200,'K'), Tmax=(1000,'K')), NASAPolynomial(coeffs=[2.5,0,0,0,0,-745.375,0.928724], Tmin=(1000,'K'), Tmax=(6000,'K'))], Tmin=(200,'K'), Tmax=(6000,'K'), E0=(-6.19738,'kJ/mol'), comment="""Thermo library: primaryThermoLibrary"""),
)

species(
    label = 'Ar',
    structure = SMILES('[Ar]'),
    E0 = (-6.19738,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
    molecularWeight = (39.348,'amu'),
    collisionModel = TransportData(shapeIndex=0, epsilon=(1134.93,'J/mol'), sigma=(3.33,'angstroms'), dipoleMoment=(0,'C*m'), polarizability=(0,'angstroms^3'), rotrelaxcollnum=0.0, comment="""GRI-Mech"""),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[2.5,0,0,0,0,-745.375,4.37967], Tmin=(200,'K'), Tmax=(1000,'K')), NASAPolynomial(coeffs=[2.5,0,0,0,0,-745.375,4.37967], Tmin=(1000,'K'), Tmax=(6000,'K'))], Tmin=(200,'K'), Tmax=(6000,'K'), E0=(-6.19738,'kJ/mol'), comment="""Thermo library: primaryThermoLibrary"""),
)

species(
    label = 'Ne',
    structure = SMILES('[Ne]'),
    E0 = (-6.19738,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
    molecularWeight = (20.1797,'amu'),
    collisionModel = TransportData(shapeIndex=2, epsilon=(1235.53,'J/mol'), sigma=(3.758e-10,'m'), dipoleMoment=(0,'C*m'), polarizability=(0,'angstroms^3'), rotrelaxcollnum=0, comment="""Epsilon & sigma estimated with fixed Lennard Jones Parameters. This is the fallback method! Try improving transport databases!"""),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[2.5,0,0,0,0,-745.375,3.35532], Tmin=(200,'K'), Tmax=(1000,'K')), NASAPolynomial(coeffs=[2.5,0,0,0,0,-745.375,3.35532], Tmin=(1000,'K'), Tmax=(6000,'K'))], Tmin=(200,'K'), Tmax=(6000,'K'), E0=(-6.19738,'kJ/mol'), comment="""Thermo library: primaryThermoLibrary"""),
)

species(
    label = 'N2',
    structure = SMILES('N#N'),
    E0 = (-8.64289,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
    molecularWeight = (28.0135,'amu'),
    collisionModel = TransportData(shapeIndex=1, epsilon=(810.913,'J/mol'), sigma=(3.621,'angstroms'), dipoleMoment=(0,'C*m'), polarizability=(1.76,'angstroms^3'), rotrelaxcollnum=4.0, comment="""GRI-Mech"""),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[3.53101,-0.000123661,-5.02999e-07,2.43531e-09,-1.40881e-12,-1046.98,2.96747], Tmin=(200,'K'), Tmax=(1000,'K')), NASAPolynomial(coeffs=[2.95258,0.0013969,-4.92632e-07,7.8601e-11,-4.60755e-15,-923.949,5.87189], Tmin=(1000,'K'), Tmax=(6000,'K'))], Tmin=(200,'K'), Tmax=(6000,'K'), E0=(-8.64289,'kJ/mol'), comment="""Thermo library: primaryThermoLibrary"""),
)

transitionState(
    label = 'TS1',
    E0 = (1060.29,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS2',
    E0 = (917.646,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS3',
    E0 = (893.121,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS4',
    E0 = (896.759,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS5',
    E0 = (859.279,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

reaction(
    label = 'reaction1',
    reactants = ['[SiH]=[SiH2](22)', '[SiH]=[SiH2](22)'],
    products = ['[SiH]=[SiH][Si]=[SiH2](56)'],
    transitionState = 'TS1',
    kinetics = Arrhenius(A=(1.86e+14,'cm^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), Tmin=(295,'K'), Tmax=(595,'K'), comment="""Exact match found for rate rule (Si2S;Si_H)
Ea raised from -1.9 to 0 kJ/mol."""),
)

reaction(
    label = 'reaction2',
    reactants = ['[H](13)', '[SiH]=[Si][Si]=[SiH2](89)'],
    products = ['[SiH]=[SiH][Si]=[SiH2](56)'],
    transitionState = 'TS2',
    kinetics = Arrhenius(A=(7.20571e+06,'m^3/(mol*s)'), n=0.100587, Ea=(0,'kJ/mol'), T0=(1,'K'), comment="""Estimated using template (Y_rad;Y_rad) for rate rule (Si_rad;H_rad)
Ea raised from -0.8 to 0 kJ/mol."""),
)

reaction(
    label = 'reaction3',
    reactants = ['[SiH][SiH2][SiH]=[SiH2](90)'],
    products = ['[SiH]=[SiH][Si]=[SiH2](56)'],
    transitionState = 'TS3',
    kinetics = Arrhenius(A=(7.9e+12,'cm^3/(mol*s)'), n=0, Ea=(5.3095,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1600,'K'), comment="""Estimated using template (SiRSiH) for rate rule (SiSiSiH)"""),
)

reaction(
    label = 'reaction4',
    reactants = ['[SiH2]=[Si]=[SiH2](64)', '[SiH2](68)'],
    products = ['[SiH]=[SiH][Si]=[SiH2](56)'],
    transitionState = 'TS4',
    kinetics = Arrhenius(A=(7.44e+14,'cm^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), Tmin=(295,'K'), Tmax=(595,'K'), comment="""Exact match found for rate rule (Si2S;Si_H)
Multiplied by reaction path degeneracy 4
Ea raised from -1.9 to 0 kJ/mol."""),
)

reaction(
    label = 'reaction5',
    reactants = ['Si(8)', '[SiH2]=[Si]=[SiH2](91)'],
    products = ['[SiH]=[SiH][Si]=[SiH2](56)'],
    transitionState = 'TS5',
    kinetics = Arrhenius(A=(3.72e+14,'cm^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), Tmin=(295,'K'), Tmax=(595,'K'), comment="""Exact match found for rate rule (Si2S;Si_H)
Multiplied by reaction path degeneracy 2
Ea raised from -1.9 to 0 kJ/mol."""),
)

network(
    label = '50',
    isomers = [
        '[SiH]=[SiH][Si]=[SiH2](56)',
    ],
    reactants = [
        ('[SiH]=[SiH2](22)', '[SiH]=[SiH2](22)'),
    ],
    bathGas = {
        'He': 0.25,
        'Ar': 0.25,
        'Ne': 0.25,
        'N2': 0.25,
    },
)

pressureDependence(
    label = '50',
    Tmin = (300,'K'),
    Tmax = (2000,'K'),
    Tcount = 8,
    Tlist = ([302.47,323.145,369.86,455.987,609.649,885.262,1353.64,1896.74],'K'),
    Pmin = (0.01,'bar'),
    Pmax = (20,'bar'),
    Pcount = 5,
    Plist = ([0.0120443,0.0479034,0.447214,4.17507,16.6054],'bar'),
    maximumGrainSize = (0.5,'kcal/mol'),
    minimumGrainCount = 250,
    method = 'modified strong collision',
    interpolationModel = ('Chebyshev', 6, 4),
    activeKRotor = True,
    activeJRotor = True,
    rmgmode = True,
)

