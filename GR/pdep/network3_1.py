species(
    label = 'H3SiSiH(3)',
    structure = SMILES('[SiH3][SiH3]'),
    E0 = (288.191,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([300,800,800,800,800,800,1600,1600,1600,1600,1600],'cm^-1')),
        HinderedRotor(inertia=(0.156089,'amu*angstrom^2'), symmetry=1, barrier=(3.5888,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 1,
    opticalIsomers = 1,
    molecularWeight = (60.2028,'amu'),
    collisionModel = TransportData(shapeIndex=2, epsilon=(920.412,'J/mol'), sigma=(4.443e-10,'m'), dipoleMoment=(0,'C*m'), polarizability=(0,'angstroms^3'), rotrelaxcollnum=0, comment="""Epsilon & sigma estimated with fixed Lennard Jones Parameters. This is the fallback method! Try improving transport databases!"""),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[2.96585,0.0231422,-2.03763e-05,9.47522e-09,-1.83128e-12,34698.2,12.2671], Tmin=(100,'K'), Tmax=(1208.2,'K')), NASAPolynomial(coeffs=[6.72586,0.0106939,-4.92167e-06,9.47639e-10,-6.67695e-14,33789.6,-6.58397], Tmin=(1208.2,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(288.191,'kJ/mol'), comment="""Thermo library: SiliconHydrideLibrary"""),
)

species(
    label = '[SiH3](7)',
    structure = SMILES('[SiH3]'),
    E0 = (367.809,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([1747],'cm^-1')),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 1,
    molecularWeight = (29.0934,'amu'),
    collisionModel = TransportData(shapeIndex=1, epsilon=(1235.53,'J/mol'), sigma=(3.758e-10,'m'), dipoleMoment=(0,'C*m'), polarizability=(0,'angstroms^3'), rotrelaxcollnum=0, comment="""Epsilon & sigma estimated with fixed Lennard Jones Parameters. This is the fallback method! Try improving transport databases!"""),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[3.51239,0.000844124,-3.14556e-06,5.5264e-09,-2.63903e-12,44235.7,3.65288], Tmin=(100,'K'), Tmax=(878.727,'K')), NASAPolynomial(coeffs=[2.39072,0.00289534,-1.43263e-06,2.70837e-10,-1.83107e-14,44550.7,9.59034], Tmin=(878.727,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(367.809,'kJ/mol'), comment="""Thermo library: SiliconHydrideLibrary"""),
)

species(
    label = '[SiH3](8)',
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
    label = '[H](4)',
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
    label = '[SiH2][SiH3](9)',
    structure = SMILES('[SiH2][SiH3]'),
    E0 = (384.731,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([180,180,451.913,738.446,738.466,738.494,1634.44,2708.46],'cm^-1')),
        HinderedRotor(inertia=(0.00941647,'amu*angstrom^2'), symmetry=1, barrier=(49.0164,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 1,
    molecularWeight = (59.1948,'amu'),
    collisionModel = TransportData(shapeIndex=2, epsilon=(920.412,'J/mol'), sigma=(4.443e-10,'m'), dipoleMoment=(0,'C*m'), polarizability=(0,'angstroms^3'), rotrelaxcollnum=0, comment="""Epsilon & sigma estimated with fixed Lennard Jones Parameters. This is the fallback method! Try improving transport databases!"""),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[2.95711,0.0248006,-3.75655e-05,3.13473e-08,-1.04364e-11,46308.2,12.7611], Tmin=(100,'K'), Tmax=(802.147,'K')), NASAPolynomial(coeffs=[5.83596,0.00867529,-4.10251e-06,7.85923e-10,-5.44628e-14,45903.3,-0.138194], Tmin=(802.147,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(384.731,'kJ/mol'), comment="""Thermo library: SiliconHydrideLibrary + radical(SisJ_SiLP)"""),
)

species(
    label = '[SiH2]=[SiH2](11)',
    structure = SMILES('[SiH2]=[SiH2]'),
    E0 = (255.415,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
    molecularWeight = (60.2028,'amu'),
    collisionModel = TransportData(shapeIndex=2, epsilon=(920.412,'J/mol'), sigma=(4.443e-10,'m'), dipoleMoment=(0,'C*m'), polarizability=(0,'angstroms^3'), rotrelaxcollnum=0, comment="""Epsilon & sigma estimated with fixed Lennard Jones Parameters. This is the fallback method! Try improving transport databases!"""),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[2.79402,0.0234376,-1.86129e-05,5.76209e-09,-9.95633e-14,30765.4,10.212], Tmin=(100,'K'), Tmax=(1032.63,'K')), NASAPolynomial(coeffs=[8.37804,0.00714282,-2.69331e-06,4.87897e-10,-3.40292e-14,29327.7,-18.2844], Tmin=(1032.63,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(255.415,'kJ/mol'), comment="""Thermo library: SiliconHydrideLibrary"""),
)

species(
    label = 'H2(1)',
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
    label = '[SiH3][SiH3](12)',
    structure = SMILES('[SiH3][SiH3]'),
    E0 = (441.618,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([424.64,424.663,424.93,425.521,3300.2],'cm^-1')),
        HinderedRotor(inertia=(0.0255584,'amu*angstrom^2'), symmetry=1, barrier=(59.1505,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 1,
    opticalIsomers = 1,
    molecularWeight = (58.1869,'amu'),
    collisionModel = TransportData(shapeIndex=2, epsilon=(920.412,'J/mol'), sigma=(4.443e-10,'m'), dipoleMoment=(0,'C*m'), polarizability=(0,'angstroms^3'), rotrelaxcollnum=0, comment="""Epsilon & sigma estimated with fixed Lennard Jones Parameters. This is the fallback method! Try improving transport databases!"""),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[3.14502,0.0208298,-3.62767e-05,3.11975e-08,-1.00977e-11,53143.3,9.04269], Tmin=(100,'K'), Tmax=(910.256,'K')), NASAPolynomial(coeffs=[5.63589,0.00502331,-2.21943e-06,3.87734e-10,-2.46164e-14,52891.2,-1.63395], Tmin=(910.256,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(441.618,'kJ/mol'), comment="""Thermo library: SiliconHydrideLibrary"""),
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

transitionState(
    label = 'TS1',
    E0 = (549.361,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS2',
    E0 = (596.536,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS3',
    E0 = (310.406,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS4',
    E0 = (436.362,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

reaction(
    label = 'reaction1',
    reactants = ['[SiH3](7)', '[SiH3](8)'],
    products = ['H3SiSiH(3)'],
    transitionState = 'TS1',
    kinetics = Arrhenius(A=(7.20571e+06,'m^3/(mol*s)'), n=0.100587, Ea=(0,'kJ/mol'), T0=(1,'K'), comment="""Estimated using template (Y_rad;Y_rad) for rate rule (Si_rad;Si_silyl)
Ea raised from -0.8 to 0 kJ/mol."""),
)

reaction(
    label = 'reaction2',
    reactants = ['[H](4)', '[SiH2][SiH3](9)'],
    products = ['H3SiSiH(3)'],
    transitionState = 'TS2',
    kinetics = Arrhenius(A=(7.20571e+06,'m^3/(mol*s)'), n=0.100587, Ea=(0,'kJ/mol'), T0=(1,'K'), comment="""Estimated using template (Y_rad;Y_rad) for rate rule (Si_rad;H_rad)
Ea raised from -0.8 to 0 kJ/mol."""),
)

reaction(
    label = 'reaction3',
    reactants = ['H3SiSiH(3)'],
    products = ['[SiH2]=[SiH2](11)'],
    transitionState = 'TS3',
    kinetics = Arrhenius(A=(7.9e+12,'1/s'), n=0, Ea=(5.3095,'kcal/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1600,'K'), comment="""Matched reaction 1 H3SiSiH <=> Si2H4 in Silylene_to_Silene/training"""),
)

reaction(
    label = 'reaction4',
    reactants = ['H2(1)', '[SiH3][SiH3](12)'],
    products = ['H3SiSiH(3)'],
    transitionState = 'TS4',
    kinetics = Arrhenius(A=(1.52e+13,'cm^3/(mol*s)'), n=0, Ea=(3.3472,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Exact match found for rate rule (Si-Si-H;H_H)
Multiplied by reaction path degeneracy 4"""),
)

network(
    label = '3',
    isomers = [
        'H3SiSiH(3)',
    ],
    reactants = [
    ],
    bathGas = {
        'Ne': 0.25,
        'N2': 0.25,
        'He': 0.25,
        'Ar': 0.25,
    },
)

pressureDependence(
    label = '3',
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

