species(
    label = '[Si]=[SiH][Si]=[SiH2](55)',
    structure = SMILES('[Si]=[SiH][Si]=[SiH2]'),
    E0 = (776.475,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([180,180,180,180,180,180,180,180],'cm^-1')),
        HinderedRotor(inertia=(2.01713,'amu*angstrom^2'), symmetry=1, barrier=(46.3778,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 4,
    opticalIsomers = 1,
    molecularWeight = (113.35,'amu'),
    collisionModel = TransportData(shapeIndex=2, epsilon=(4418.31,'J/mol'), sigma=(4.687e-10,'m'), dipoleMoment=(0,'C*m'), polarizability=(0,'angstroms^3'), rotrelaxcollnum=0, comment="""Epsilon & sigma estimated with fixed Lennard Jones Parameters. This is the fallback method! Try improving transport databases!"""),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[0.879918,0.0861525,-0.000195818,1.91678e-07,-6.72047e-11,93484.3,-3.05493], Tmin=(100,'K'), Tmax=(904.898,'K')), NASAPolynomial(coeffs=[6.55899,0.0176187,-1.02218e-05,1.90485e-09,-1.22222e-13,94234.6,-20.0607], Tmin=(904.898,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(776.475,'kJ/mol'), comment="""Thermo group additivity estimation: group(Sis-Sis4) + other(R) + group(Sis-Sis4) + other(R) + group(Sid-H2) + other(R) + group(si) + other(R) + radical(SidsJ_Si) + radical(Si=SiJ2_triplet)"""),
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
    label = '[Si]=[SiH2](37)',
    structure = SMILES('[Si]=[SiH2]'),
    E0 = (622.157,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([180],'cm^-1')),
    ],
    spinMultiplicity = 3,
    opticalIsomers = 1,
    molecularWeight = (56.171,'amu'),
    collisionModel = TransportData(shapeIndex=1, epsilon=(920.412,'J/mol'), sigma=(4.443e-10,'m'), dipoleMoment=(0,'C*m'), polarizability=(0,'angstroms^3'), rotrelaxcollnum=0, comment="""Epsilon & sigma estimated with fixed Lennard Jones Parameters. This is the fallback method! Try improving transport databases!"""),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[2.6941,0.0225659,-4.77827e-05,4.82116e-08,-1.75935e-11,74852.6,20.6179], Tmin=(100,'K'), Tmax=(890.339,'K')), NASAPolynomial(coeffs=[3.03039,0.00905795,-4.81309e-06,9.02478e-10,-5.98212e-14,75268.2,21.7049], Tmin=(890.339,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(622.157,'kJ/mol'), comment="""Thermo group additivity estimation: group(Sid-H2) + other(R) + group(si) + other(R) + radical(Si=SiJ2_triplet)"""),
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
    label = '[Si]=[Si][Si]=[SiH2](73)',
    structure = SMILES('[Si]=[Si]=[Si][SiH2]'),
    E0 = (877.198,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([180,180,180,180,180,180],'cm^-1')),
    ],
    spinMultiplicity = 5,
    opticalIsomers = 1,
    molecularWeight = (112.342,'amu'),
    collisionModel = TransportData(shapeIndex=2, epsilon=(4418.31,'J/mol'), sigma=(4.687e-10,'m'), dipoleMoment=(0,'C*m'), polarizability=(0,'angstroms^3'), rotrelaxcollnum=0, comment="""Epsilon & sigma estimated with fixed Lennard Jones Parameters. This is the fallback method! Try improving transport databases!"""),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[1.52495,0.0701645,-0.000166529,1.65477e-07,-5.83649e-11,105577,-5.98791], Tmin=(100,'K'), Tmax=(907.979,'K')), NASAPolynomial(coeffs=[5.44982,0.0135788,-8.13167e-06,1.51347e-09,-9.61741e-14,106484,-15.6245], Tmin=(907.979,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(877.198,'kJ/mol'), comment="""Thermo group additivity estimation: group(Sis-Sis4) + other(R) + group(Sid-H2) + other(R) + group(Sis-Sis4) + other(R) + group(si) + other(R) + radical(SiJ_LP_Si) + radical(Si=SiJ2_triplet) + radical(SidsJ_Si)"""),
)

species(
    label = '[Si][SiH2][SiH]=[SiH2](74)',
    structure = SMILES('[Si][SiH2][SiH]=[SiH2]'),
    E0 = (1257.6,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([180,180,180,180,180,180,180,180],'cm^-1')),
        HinderedRotor(inertia=(1.96959,'amu*angstrom^2'), symmetry=1, barrier=(45.2847,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 4,
    opticalIsomers = 1,
    molecularWeight = (113.35,'amu'),
    collisionModel = TransportData(shapeIndex=2, epsilon=(4418.31,'J/mol'), sigma=(4.687e-10,'m'), dipoleMoment=(0,'C*m'), polarizability=(0,'angstroms^3'), rotrelaxcollnum=0, comment="""Epsilon & sigma estimated with fixed Lennard Jones Parameters. This is the fallback method! Try improving transport databases!"""),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[0.330779,0.0922319,-0.000183327,1.65336e-07,-5.52428e-11,151376,22.0967], Tmin=(100,'K'), Tmax=(893.103,'K')), NASAPolynomial(coeffs=[11.7278,0.0146699,-8.52208e-06,1.60546e-09,-1.04961e-13,150397,-25.6784], Tmin=(893.103,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(1257.6,'kJ/mol'), comment="""Thermo group additivity estimation: group(Sis-H3si) + other(R) + group(Sis-Sis4) + other(R) + group(si) + other(R) + group(si) + other(R) + radical(CJ3)"""),
)

species(
    label = '[SiH](72)',
    structure = SMILES('[SiH]'),
    E0 = (682.172,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([180],'cm^-1')),
    ],
    spinMultiplicity = 4,
    opticalIsomers = 1,
    molecularWeight = (29.0934,'amu'),
    collisionModel = TransportData(shapeIndex=1, epsilon=(1235.53,'J/mol'), sigma=(3.758e-10,'m'), dipoleMoment=(0,'C*m'), polarizability=(0,'angstroms^3'), rotrelaxcollnum=0, comment="""Epsilon & sigma estimated with fixed Lennard Jones Parameters. This is the fallback method! Try improving transport databases!"""),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[3.85231,-0.000582041,1.30242e-05,-1.84877e-08,7.317e-12,82055.1,2.00317], Tmin=(100,'K'), Tmax=(978.651,'K')), NASAPolynomial(coeffs=[6.79259,-0.0027429,1.22841e-06,-1.60731e-10,6.29138e-15,81007.5,-14.5301], Tmin=(978.651,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(682.172,'kJ/mol'), comment="""Thermo library: SiliconHydrideLibrary + radical(CJ3)"""),
)

species(
    label = '[SiH2]=[Si]=[SiH2](75)',
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
    E0 = (1152.3,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS2',
    E0 = (1089,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS3',
    E0 = (1262.91,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS4',
    E0 = (1233.84,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

reaction(
    label = 'reaction1',
    reactants = ['[SiH]=[SiH2](22)', '[Si]=[SiH2](37)'],
    products = ['[Si]=[SiH][Si]=[SiH2](55)'],
    transitionState = 'TS1',
    kinetics = Arrhenius(A=(1.86e+14,'cm^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), Tmin=(295,'K'), Tmax=(595,'K'), comment="""Exact match found for rate rule (Si2S;Si_H)
Ea raised from -1.9 to 0 kJ/mol."""),
)

reaction(
    label = 'reaction2',
    reactants = ['[H](13)', '[Si]=[Si][Si]=[SiH2](73)'],
    products = ['[Si]=[SiH][Si]=[SiH2](55)'],
    transitionState = 'TS2',
    kinetics = Arrhenius(A=(7.20571e+06,'m^3/(mol*s)'), n=0.100587, Ea=(0,'kJ/mol'), T0=(1,'K'), comment="""Estimated using template (Y_rad;Y_rad) for rate rule (Si_rad;H_rad)
Ea raised from -0.8 to 0 kJ/mol."""),
)

reaction(
    label = 'reaction3',
    reactants = ['[Si][SiH2][SiH]=[SiH2](74)'],
    products = ['[Si]=[SiH][Si]=[SiH2](55)'],
    transitionState = 'TS3',
    kinetics = Arrhenius(A=(7.9e+12,'cm^3/(mol*s)'), n=0, Ea=(5.3095,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1600,'K'), comment="""Estimated using template (SiRSiH) for rate rule (SiSiSiH)"""),
)

reaction(
    label = 'reaction4',
    reactants = ['[SiH](72)', '[SiH2]=[Si]=[SiH2](75)'],
    products = ['[Si]=[SiH][Si]=[SiH2](55)'],
    transitionState = 'TS4',
    kinetics = Arrhenius(A=(3.72e+14,'cm^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), Tmin=(295,'K'), Tmax=(595,'K'), comment="""Exact match found for rate rule (Si2S;Si_H)
Multiplied by reaction path degeneracy 2
Ea raised from -1.9 to 0 kJ/mol."""),
)

network(
    label = '48',
    isomers = [
        '[Si]=[SiH][Si]=[SiH2](55)',
    ],
    reactants = [
        ('[SiH]=[SiH2](22)', '[Si]=[SiH2](37)'),
    ],
    bathGas = {
        'He': 0.25,
        'Ar': 0.25,
        'Ne': 0.25,
        'N2': 0.25,
    },
)

pressureDependence(
    label = '48',
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

