species(
    label = '[Si]=[SiH][SiH3](38)',
    structure = SMILES('[Si]=[SiH][SiH3]'),
    E0 = (511.726,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([300,800,800,800,800,800,800,1600,1600,1600,1600,1600,1600,1600],'cm^-1')),
        HinderedRotor(inertia=(0.156089,'amu*angstrom^2'), symmetry=1, barrier=(3.5888,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 3,
    opticalIsomers = 1,
    molecularWeight = (88.2883,'amu'),
    collisionModel = TransportData(shapeIndex=2, epsilon=(1971.36,'J/mol'), sigma=(5.118e-10,'m'), dipoleMoment=(0,'C*m'), polarizability=(0,'angstroms^3'), rotrelaxcollnum=0, comment="""Epsilon & sigma estimated with fixed Lennard Jones Parameters. This is the fallback method! Try improving transport databases!"""),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[2.05539,0.0471944,-7.77466e-05,6.78388e-08,-2.3051e-11,61612.2,15.759], Tmin=(100,'K'), Tmax=(841.916,'K')), NASAPolynomial(coeffs=[7.06786,0.0156374,-7.72899e-06,1.47293e-09,-1.00794e-13,61042.6,-5.93117], Tmin=(841.916,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(511.726,'kJ/mol'), comment="""Thermo group additivity estimation: group(Sis-H3Sid) + other(R) + group(Sid-HSis) + other(R) + group(Sid-H2) + other(R) + radical(Si=SiJ2_triplet)"""),
)

species(
    label = 'SiH4(1)',
    structure = SMILES('[SiH4]'),
    E0 = (12.704,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([410.267,1305.4,1305.48,1306.33,1306.38,1306.93,1309.23,2132.31,3568.96],'cm^-1')),
    ],
    spinMultiplicity = 1,
    opticalIsomers = 1,
    molecularWeight = (32.1173,'amu'),
    collisionModel = TransportData(shapeIndex=2, epsilon=(1235.53,'J/mol'), sigma=(3.758e-10,'m'), dipoleMoment=(0,'C*m'), polarizability=(0,'angstroms^3'), rotrelaxcollnum=0, comment="""Epsilon & sigma estimated with fixed Lennard Jones Parameters. This is the fallback method! Try improving transport databases!"""),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[3.89845,-0.00273683,3.35034e-05,-3.74635e-08,1.28903e-11,1535.98,2.01298], Tmin=(100,'K'), Tmax=(995.076,'K')), NASAPolynomial(coeffs=[4.37015,0.00859245,-3.51089e-06,6.91517e-10,-5.13524e-14,787.329,-3.55046], Tmin=(995.076,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(12.704,'kJ/mol'), comment="""Thermo library: SiliconHydrideLibrary"""),
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
    label = 'SiH2(2)',
    structure = SMILES('[SiH4]'),
    E0 = (253.111,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([1019.26,1858.84,2195.51],'cm^-1')),
    ],
    spinMultiplicity = 1,
    opticalIsomers = 1,
    molecularWeight = (30.1014,'amu'),
    collisionModel = TransportData(shapeIndex=2, epsilon=(1235.53,'J/mol'), sigma=(3.758e-10,'m'), dipoleMoment=(0,'C*m'), polarizability=(0,'angstroms^3'), rotrelaxcollnum=0, comment="""Epsilon & sigma estimated with fixed Lennard Jones Parameters. This is the fallback method! Try improving transport databases!"""),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[4.05121,-0.00189758,1.06519e-05,-9.83341e-09,2.89964e-12,30440.9,2.02993], Tmin=(100,'K'), Tmax=(1086.09,'K')), NASAPolynomial(coeffs=[3.2086,0.0041769,-1.84111e-06,3.53872e-10,-2.50882e-14,30448.7,5.35785], Tmin=(1086.09,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(253.111,'kJ/mol'), comment="""Thermo library: SiliconHydrideLibrary"""),
)

species(
    label = 'SiH2Si(11)',
    structure = SMILES('[Si]=[SiH2]'),
    E0 = (475.448,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([180,496.087,738.472,740.252,1609.39,2850.44],'cm^-1')),
    ],
    spinMultiplicity = 3,
    opticalIsomers = 1,
    molecularWeight = (58.1869,'amu'),
    collisionModel = TransportData(shapeIndex=2, epsilon=(920.412,'J/mol'), sigma=(4.443e-10,'m'), dipoleMoment=(0,'C*m'), polarizability=(0,'angstroms^3'), rotrelaxcollnum=0, comment="""Epsilon & sigma estimated with fixed Lennard Jones Parameters. This is the fallback method! Try improving transport databases!"""),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[3.37727,0.013834,-1.5219e-05,8.6378e-09,-1.93333e-12,57205.5,9.87721], Tmin=(100,'K'), Tmax=(1088.12,'K')), NASAPolynomial(coeffs=[6.05418,0.00399341,-1.65332e-06,3.26322e-10,-2.37175e-14,56622.9,-3.26341], Tmin=(1088.12,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(475.448,'kJ/mol'), comment="""Thermo library: SiliconHydrideLibrary + radical(Si=SiJ2_triplet)"""),
)

species(
    label = '[Si]=[SiH](36)',
    structure = SMILES('[Si]=[SiH]'),
    E0 = (604.01,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([180,221.871,1858.4],'cm^-1')),
    ],
    spinMultiplicity = 4,
    opticalIsomers = 1,
    molecularWeight = (57.1789,'amu'),
    collisionModel = TransportData(shapeIndex=2, epsilon=(920.412,'J/mol'), sigma=(4.443e-10,'m'), dipoleMoment=(0,'C*m'), polarizability=(0,'angstroms^3'), rotrelaxcollnum=0, comment="""Epsilon & sigma estimated with fixed Lennard Jones Parameters. This is the fallback method! Try improving transport databases!"""),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[3.4267,0.0165706,-3.90977e-05,4.07442e-08,-1.50913e-11,72662.5,12.426], Tmin=(100,'K'), Tmax=(874.081,'K')), NASAPolynomial(coeffs=[3.91713,0.00483364,-2.66577e-06,5.3263e-10,-3.66184e-14,72939.4,12.2003], Tmin=(874.081,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(604.01,'kJ/mol'), comment="""Thermo library: SiliconHydrideLibrary + radical(SidsJ_Si) + radical(Si=SiJ2_triplet)"""),
)

species(
    label = 'SiH3(9)',
    structure = SMILES('[SiH3]'),
    E0 = (181.552,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([509.888,1381.04,1404.31,1421.15,1467.61,3293.64],'cm^-1')),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 1,
    molecularWeight = (31.1093,'amu'),
    collisionModel = TransportData(shapeIndex=2, epsilon=(1235.53,'J/mol'), sigma=(3.758e-10,'m'), dipoleMoment=(0,'C*m'), polarizability=(0,'angstroms^3'), rotrelaxcollnum=0, comment="""Epsilon & sigma estimated with fixed Lennard Jones Parameters. This is the fallback method! Try improving transport databases!"""),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[3.91655,-0.00100476,1.92801e-05,-2.15456e-08,7.35514e-12,21841.2,3.38325], Tmin=(100,'K'), Tmax=(1000.99,'K')), NASAPolynomial(coeffs=[4.09637,0.00586731,-2.39263e-06,4.64339e-10,-3.3986e-14,21424.9,0.61602], Tmin=(1000.99,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(181.552,'kJ/mol'), comment="""Thermo library: SiliconHydrideLibrary"""),
)

species(
    label = '[Si]=[SiH][SiH2](44)',
    structure = SMILES('[Si]=[SiH][SiH2]'),
    E0 = (668.266,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([300,800,800,800,800,800,1600,1600,1600,1600,1600],'cm^-1')),
        HinderedRotor(inertia=(0.156089,'amu*angstrom^2'), symmetry=1, barrier=(3.5888,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 4,
    opticalIsomers = 1,
    molecularWeight = (87.2803,'amu'),
    collisionModel = TransportData(shapeIndex=2, epsilon=(1971.36,'J/mol'), sigma=(5.118e-10,'m'), dipoleMoment=(0,'C*m'), polarizability=(0,'angstroms^3'), rotrelaxcollnum=0, comment="""Epsilon & sigma estimated with fixed Lennard Jones Parameters. This is the fallback method! Try improving transport databases!"""),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[2.09753,0.0481031,-9.05406e-05,8.27988e-08,-2.8297e-11,80436.3,16.5087], Tmin=(100,'K'), Tmax=(884.288,'K')), NASAPolynomial(coeffs=[6.75226,0.0128005,-6.49018e-06,1.21305e-09,-8.05773e-14,80170.2,-2.22561], Tmin=(884.288,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(668.266,'kJ/mol'), comment="""Thermo group additivity estimation: group(Sis-H3Sid) + other(R) + group(Sid-HSis) + other(R) + group(Sid-H2) + other(R) + radical(SisJ_Si_H2) + radical(Si=SiJ2_triplet)"""),
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
    label = '[Si]=[Si][SiH3](45)',
    structure = SMILES('[Si]=[Si][SiH3]'),
    E0 = (640.292,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([300,800,800,800,800,800,1600,1600,1600,1600,1600],'cm^-1')),
        HinderedRotor(inertia=(0.156089,'amu*angstrom^2'), symmetry=1, barrier=(3.5888,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 4,
    opticalIsomers = 1,
    molecularWeight = (87.2803,'amu'),
    collisionModel = TransportData(shapeIndex=2, epsilon=(1971.36,'J/mol'), sigma=(5.118e-10,'m'), dipoleMoment=(0,'C*m'), polarizability=(0,'angstroms^3'), rotrelaxcollnum=0, comment="""Epsilon & sigma estimated with fixed Lennard Jones Parameters. This is the fallback method! Try improving transport databases!"""),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[2.14441,0.0493979,-9.95224e-05,9.68182e-08,-3.46563e-11,77068,17.4791], Tmin=(100,'K'), Tmax=(878.896,'K')), NASAPolynomial(coeffs=[4.90877,0.0165096,-8.73408e-06,1.66361e-09,-1.11833e-13,77366.4,8.9615], Tmin=(878.896,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(640.292,'kJ/mol'), comment="""Thermo group additivity estimation: group(Sis-H3Sid) + other(R) + group(Sid-HSis) + other(R) + group(Sid-H2) + other(R) + radical(SidsJ_Si) + radical(Si=SiJ2_triplet)"""),
)

species(
    label = 'H2(3)',
    structure = SMILES('[H][H]'),
    E0 = (-8.60349,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([3765.59],'cm^-1')),
    ],
    spinMultiplicity = 1,
    opticalIsomers = 1,
    molecularWeight = (2.01588,'amu'),
    collisionModel = TransportData(shapeIndex=1, epsilon=(315.951,'J/mol'), sigma=(2.92,'angstroms'), dipoleMoment=(0,'C*m'), polarizability=(0.79,'angstroms^3'), rotrelaxcollnum=280.0, comment="""GRI-Mech"""),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[3.43536,0.000212709,-2.78622e-07,3.40265e-10,-7.76026e-14,-1031.36,-3.90842], Tmin=(100,'K'), Tmax=(1959.08,'K')), NASAPolynomial(coeffs=[2.78815,0.000587663,1.59e-07,-5.52718e-11,4.34296e-15,-596.134,0.112835], Tmin=(1959.08,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(-8.60349,'kJ/mol'), comment="""Thermo library: primaryThermoLibrary"""),
)

species(
    label = '[Si]=[SiH][SiH3](46)',
    structure = SMILES('[Si]=[SiH][SiH3]'),
    E0 = (634.761,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([359.492,360.571,361.001,362.681,362.945,363.744,364.526,364.804],'cm^-1')),
        HinderedRotor(inertia=(0.00130739,'amu*angstrom^2'), symmetry=1, barrier=(0.119627,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 3,
    opticalIsomers = 1,
    molecularWeight = (86.2724,'amu'),
    collisionModel = TransportData(shapeIndex=2, epsilon=(1971.36,'J/mol'), sigma=(5.118e-10,'m'), dipoleMoment=(0,'C*m'), polarizability=(0,'angstroms^3'), rotrelaxcollnum=0, comment="""Epsilon & sigma estimated with fixed Lennard Jones Parameters. This is the fallback method! Try improving transport databases!"""),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[2.06271,0.0510878,-0.000105898,1.00702e-07,-3.50108e-11,76405.9,6.55983], Tmin=(100,'K'), Tmax=(893.97,'K')), NASAPolynomial(coeffs=[6.18943,0.0122847,-6.66346e-06,1.25009e-09,-8.21217e-14,76480.7,-8.3412], Tmin=(893.97,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(634.761,'kJ/mol'), comment="""Thermo group additivity estimation: group(Sis-Sis4) + other(R) + group(Sid-H2) + other(R) + group(si) + other(R) + radical(Si=SiJ2_triplet)"""),
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
    E0 = (634.861,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS2',
    E0 = (785.562,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS3',
    E0 = (880.07,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS4',
    E0 = (852.097,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS5',
    E0 = (629.505,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS6',
    E0 = (728.558,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

reaction(
    label = 'reaction1',
    reactants = ['SiH4(1)', '[Si]=[SiH2](37)'],
    products = ['[Si]=[SiH][SiH3](38)'],
    transitionState = 'TS1',
    kinetics = Arrhenius(A=(7.44e+14,'cm^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), Tmin=(295,'K'), Tmax=(595,'K'), comment="""Estimated using template (Si2S;Si_H) for rate rule (Si2S;SiH4)
Multiplied by reaction path degeneracy 4
Ea raised from -1.9 to 0 kJ/mol."""),
)

reaction(
    label = 'reaction2',
    reactants = ['[Si]=[SiH](36)', 'SiH3(9)'],
    products = ['[Si]=[SiH][SiH3](38)'],
    transitionState = 'TS2',
    kinetics = Arrhenius(A=(7.20571e+06,'m^3/(mol*s)'), n=0.100587, Ea=(0,'kJ/mol'), T0=(1,'K'), comment="""Estimated using template (Y_rad;Y_rad) for rate rule (Si_rad;Si_silyl)
Ea raised from -0.8 to 0 kJ/mol."""),
)

reaction(
    label = 'reaction3',
    reactants = ['[Si]=[SiH][SiH2](44)', '[H](13)'],
    products = ['[Si]=[SiH][SiH3](38)'],
    transitionState = 'TS3',
    kinetics = Arrhenius(A=(7.20571e+06,'m^3/(mol*s)'), n=0.100587, Ea=(0,'kJ/mol'), T0=(1,'K'), comment="""Estimated using template (Y_rad;Y_rad) for rate rule (Si_rad;H_rad)
Ea raised from -0.8 to 0 kJ/mol."""),
)

reaction(
    label = 'reaction4',
    reactants = ['[Si]=[Si][SiH3](45)', '[H](13)'],
    products = ['[Si]=[SiH][SiH3](38)'],
    transitionState = 'TS4',
    kinetics = Arrhenius(A=(7.20571e+06,'m^3/(mol*s)'), n=0.100587, Ea=(0,'kJ/mol'), T0=(1,'K'), comment="""Estimated using template (Y_rad;Y_rad) for rate rule (H_rad;Si_rad)
Ea raised from -0.8 to 0 kJ/mol."""),
)

reaction(
    label = 'reaction5',
    reactants = ['H2(3)', '[Si]=[SiH][SiH3](46)'],
    products = ['[Si]=[SiH][SiH3](38)'],
    transitionState = 'TS5',
    kinetics = Arrhenius(A=(7.6e+12,'cm^3/(mol*s)'), n=0, Ea=(3.3472,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Exact match found for rate rule (Si-Si-H;H_H)
Multiplied by reaction path degeneracy 2"""),
)

reaction(
    label = 'reaction6',
    reactants = ['SiH2(2)', 'SiH2Si(11)'],
    products = ['[Si]=[SiH][SiH3](38)'],
    transitionState = 'TS6',
    kinetics = Arrhenius(A=(462582,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), comment="""Estimated using an average for rate rule (SiH2;Si_H)
Multiplied by reaction path degeneracy 2
Ea raised from -39.3 to 0 kJ/mol."""),
)

network(
    label = '32',
    isomers = [
        '[Si]=[SiH][SiH3](38)',
    ],
    reactants = [
        ('SiH4(1)', '[Si]=[SiH2](37)'),
        ('SiH2(2)', 'SiH2Si(11)'),
    ],
    bathGas = {
        'He': 0.25,
        'Ar': 0.25,
        'Ne': 0.25,
        'N2': 0.25,
    },
)

pressureDependence(
    label = '32',
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

