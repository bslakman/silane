species(
    label = '[SiH2][SiH]=[SiH2](28)',
    structure = SMILES('[SiH2][SiH]=[SiH2]'),
    E0 = (448.225,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([300,800,800,800,800,800,800,800,800,1600,1600,1600,1600,1600,1600,1600,1600],'cm^-1')),
        HinderedRotor(inertia=(0.156089,'amu*angstrom^2'), symmetry=1, barrier=(3.5888,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 1,
    molecularWeight = (89.2962,'amu'),
    collisionModel = TransportData(shapeIndex=2, epsilon=(1971.36,'J/mol'), sigma=(5.118e-10,'m'), dipoleMoment=(0,'C*m'), polarizability=(0,'angstroms^3'), rotrelaxcollnum=0, comment="""Epsilon & sigma estimated with fixed Lennard Jones Parameters. This is the fallback method! Try improving transport databases!"""),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[1.61942,0.0565326,-8.99443e-05,7.49028e-08,-2.44078e-11,53990.8,17.1505], Tmin=(100,'K'), Tmax=(841.026,'K')), NASAPolynomial(coeffs=[8.81602,0.0164019,-7.84147e-06,1.47571e-09,-1.0039e-13,52989,-15.0818], Tmin=(841.026,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(448.225,'kJ/mol'), comment="""Thermo group additivity estimation: group(Sis-H3Sid) + other(R) + group(Sid-HSis) + other(R) + group(Sid-H2) + other(R) + radical(SisJ_Si_H2)"""),
)

species(
    label = 'SiH3(3)',
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
    label = 'SiH2Si(12)',
    structure = SMILES('[Si]=[SiH2]'),
    E0 = (401.579,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([180,180,180,180,180,180],'cm^-1')),
    ],
    spinMultiplicity = 1,
    opticalIsomers = 1,
    molecularWeight = (58.1869,'amu'),
    collisionModel = TransportData(shapeIndex=2, epsilon=(920.412,'J/mol'), sigma=(4.443e-10,'m'), dipoleMoment=(0,'C*m'), polarizability=(0,'angstroms^3'), rotrelaxcollnum=0, comment="""Epsilon & sigma estimated with fixed Lennard Jones Parameters. This is the fallback method! Try improving transport databases!"""),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[2.89004,0.0261637,-3.5189e-05,2.79883e-08,-9.23237e-12,48337.1,17.7335], Tmin=(100,'K'), Tmax=(784.976,'K')), NASAPolynomial(coeffs=[5.47727,0.0118459,-5.66252e-06,1.07163e-09,-7.38009e-14,47965.9,6.10056], Tmin=(784.976,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(401.579,'kJ/mol'), comment="""Thermo group additivity estimation: group(Sid-H2) + other(R) + group(si) + other(R)"""),
)

species(
    label = 'SiH2SiH2(9)',
    structure = SMILES('[SiH2]=[SiH2]'),
    E0 = (255.415,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([180,180,180,634.668,1003.64,1003.85,1003.99,1004.34,1004.41,1485.48,3071.85,3071.88],'cm^-1')),
    ],
    spinMultiplicity = 1,
    opticalIsomers = 1,
    molecularWeight = (60.2028,'amu'),
    collisionModel = TransportData(shapeIndex=2, epsilon=(920.412,'J/mol'), sigma=(4.443e-10,'m'), dipoleMoment=(0,'C*m'), polarizability=(0,'angstroms^3'), rotrelaxcollnum=0, comment="""Epsilon & sigma estimated with fixed Lennard Jones Parameters. This is the fallback method! Try improving transport databases!"""),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[2.79402,0.0234376,-1.86129e-05,5.76209e-09,-9.95633e-14,30765.4,10.212], Tmin=(100,'K'), Tmax=(1032.63,'K')), NASAPolynomial(coeffs=[8.37804,0.00714282,-2.69331e-06,4.87897e-10,-3.40292e-14,29327.7,-18.2844], Tmin=(1032.63,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(255.415,'kJ/mol'), comment="""Thermo library: SiliconHydrideLibrary"""),
)

species(
    label = 'SiH(11)',
    structure = SMILES('[SiH]'),
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
    label = '[SiH2][Si]=[SiH2](49)',
    structure = SMILES('[SiH2][Si]=[SiH2]'),
    E0 = (576.791,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([300,800,800,800,800,800,800,1600,1600,1600,1600,1600,1600,1600],'cm^-1')),
        HinderedRotor(inertia=(0.156089,'amu*angstrom^2'), symmetry=1, barrier=(3.5888,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 3,
    opticalIsomers = 1,
    molecularWeight = (88.2883,'amu'),
    collisionModel = TransportData(shapeIndex=2, epsilon=(1971.36,'J/mol'), sigma=(5.118e-10,'m'), dipoleMoment=(0,'C*m'), polarizability=(0,'angstroms^3'), rotrelaxcollnum=0, comment="""Epsilon & sigma estimated with fixed Lennard Jones Parameters. This is the fallback method! Try improving transport databases!"""),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[1.70364,0.0587986,-0.000111967,1.04251e-07,-3.61955e-11,69446.8,18.8875], Tmin=(100,'K'), Tmax=(880.52,'K')), NASAPolynomial(coeffs=[6.6658,0.0172581,-8.83695e-06,1.66406e-09,-1.1123e-13,69309.4,-0.238563], Tmin=(880.52,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(576.791,'kJ/mol'), comment="""Thermo group additivity estimation: group(Sis-H3Sid) + other(R) + group(Sid-HSis) + other(R) + group(Sid-H2) + other(R) + radical(SidsJ_Si) + radical(SisJ_Si_H2)"""),
)

species(
    label = '[H](16)',
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
    label = '[SiH]=[SiH][SiH2](50)',
    structure = SMILES('[SiH]=[SiH][SiH2]'),
    E0 = (576.791,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([300,800,800,800,800,800,800,1600,1600,1600,1600,1600,1600,1600],'cm^-1')),
        HinderedRotor(inertia=(0.156089,'amu*angstrom^2'), symmetry=1, barrier=(3.5888,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 3,
    opticalIsomers = 1,
    molecularWeight = (88.2883,'amu'),
    collisionModel = TransportData(shapeIndex=2, epsilon=(1971.36,'J/mol'), sigma=(5.118e-10,'m'), dipoleMoment=(0,'C*m'), polarizability=(0,'angstroms^3'), rotrelaxcollnum=0, comment="""Epsilon & sigma estimated with fixed Lennard Jones Parameters. This is the fallback method! Try improving transport databases!"""),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[1.70364,0.0587986,-0.000111967,1.04251e-07,-3.61955e-11,69446.8,18.8875], Tmin=(100,'K'), Tmax=(880.52,'K')), NASAPolynomial(coeffs=[6.6658,0.0172581,-8.83695e-06,1.66406e-09,-1.1123e-13,69309.4,-0.238563], Tmin=(880.52,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(576.791,'kJ/mol'), comment="""Thermo group additivity estimation: group(Sis-H3Sid) + other(R) + group(Sid-HSis) + other(R) + group(Sid-H2) + other(R) + radical(SidsJ_Si) + radical(SisJ_Si_H2)"""),
)

species(
    label = '[SiH2][Si][SiH3](47)',
    structure = SMILES('[SiH2][Si][SiH3]'),
    E0 = (437.365,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([300,800,800,800,800,800,800,800,1600,1600,1600,1600,1600,1600,1600,1600],'cm^-1')),
        HinderedRotor(inertia=(0.156089,'amu*angstrom^2'), symmetry=1, barrier=(3.5888,'kJ/mol'), semiclassical=False),
        HinderedRotor(inertia=(0.156089,'amu*angstrom^2'), symmetry=1, barrier=(3.5888,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 1,
    molecularWeight = (89.2962,'amu'),
    collisionModel = TransportData(shapeIndex=2, epsilon=(1971.36,'J/mol'), sigma=(5.118e-10,'m'), dipoleMoment=(0,'C*m'), polarizability=(0,'angstroms^3'), rotrelaxcollnum=0, comment="""Epsilon & sigma estimated with fixed Lennard Jones Parameters. This is the fallback method! Try improving transport databases!"""),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[1.74579,0.0541236,-8.62e-05,7.35556e-08,-2.46358e-11,52679.7,17.0584], Tmin=(100,'K'), Tmax=(837.31,'K')), NASAPolynomial(coeffs=[7.79104,0.0180687,-8.75497e-06,1.65912e-09,-1.1341e-13,51918.9,-9.53103], Tmin=(837.31,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(437.365,'kJ/mol'), comment="""Thermo group additivity estimation: group(Sis-H3si) + other(R) + group(Sis-H3si) + other(R) + group(si) + other(R) + radical(SisJ_SiLP)"""),
)

species(
    label = '[SiH][SiH2][SiH2](46)',
    structure = SMILES('[SiH][SiH2][SiH2]'),
    E0 = (497.126,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([300,800,800,800,800,800,800,800,1600,1600,1600,1600,1600,1600,1600,1600],'cm^-1')),
        HinderedRotor(inertia=(0.156089,'amu*angstrom^2'), symmetry=1, barrier=(3.5888,'kJ/mol'), semiclassical=False),
        HinderedRotor(inertia=(0.156089,'amu*angstrom^2'), symmetry=1, barrier=(3.5888,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 1,
    molecularWeight = (89.2962,'amu'),
    collisionModel = TransportData(shapeIndex=2, epsilon=(1971.36,'J/mol'), sigma=(5.118e-10,'m'), dipoleMoment=(0,'C*m'), polarizability=(0,'angstroms^3'), rotrelaxcollnum=0, comment="""Epsilon & sigma estimated with fixed Lennard Jones Parameters. This is the fallback method! Try improving transport databases!"""),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[1.59877,0.0575709,-9.35945e-05,7.96188e-08,-2.64144e-11,59872.4,17.9387], Tmin=(100,'K'), Tmax=(843.082,'K')), NASAPolynomial(coeffs=[8.48182,0.017315,-8.45105e-06,1.60024e-09,-1.09094e-13,58981.9,-12.4915], Tmin=(843.082,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(497.126,'kJ/mol'), comment="""Thermo group additivity estimation: group(Sis-H2siSis) + other(R) + group(Sis-H3Sis) + other(R) + group(si) + other(R) + radical(SisJ_Si_H2)"""),
)

species(
    label = 'H2(7)',
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
    label = '[Si]=[SiH][SiH2](34)',
    structure = SMILES('[Si][SiH]=[SiH2]'),
    E0 = (515.444,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([395.857,396.125,396.413,396.566,396.998,397.038,398.075,399.413,1196.21,2038.81,2040.22,2040.5],'cm^-1')),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 1,
    molecularWeight = (87.2803,'amu'),
    collisionModel = TransportData(shapeIndex=2, epsilon=(1971.36,'J/mol'), sigma=(5.118e-10,'m'), dipoleMoment=(0,'C*m'), polarizability=(0,'angstroms^3'), rotrelaxcollnum=0, comment="""Epsilon & sigma estimated with fixed Lennard Jones Parameters. This is the fallback method! Try improving transport databases!"""),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[2.21476,0.0437124,-7.66819e-05,6.75013e-08,-2.26678e-11,62053.6,4.32151], Tmin=(100,'K'), Tmax=(866.262,'K')), NASAPolynomial(coeffs=[7.20753,0.0117349,-5.85909e-06,1.10564e-09,-7.45671e-14,61523.4,-17.1165], Tmin=(866.262,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(515.444,'kJ/mol'), comment="""Thermo group additivity estimation: group(Sis-Sis4) + other(R) + group(Sid-H2) + other(R) + group(si) + other(R) + radical(SiJ_LP_Si)"""),
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
    E0 = (583.131,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS2',
    E0 = (788.596,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS3',
    E0 = (788.596,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS4',
    E0 = (457.03,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS5',
    E0 = (531.017,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS6',
    E0 = (506.84,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS7',
    E0 = (623.223,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

reaction(
    label = 'reaction1',
    reactants = ['SiH3(3)', 'SiH2Si(12)'],
    products = ['[SiH2][SiH]=[SiH2](28)'],
    transitionState = 'TS1',
    kinetics = Arrhenius(A=(5.58e+14,'cm^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), Tmin=(295,'K'), Tmax=(595,'K'), comment="""Exact match found for rate rule (Si2S;Si_H)
Multiplied by reaction path degeneracy 3
Ea raised from -1.9 to 0 kJ/mol."""),
)

reaction(
    label = 'reaction2',
    reactants = ['[SiH2][Si]=[SiH2](49)', '[H](16)'],
    products = ['[SiH2][SiH]=[SiH2](28)'],
    transitionState = 'TS2',
    kinetics = Arrhenius(A=(7.20571e+06,'m^3/(mol*s)'), n=0.100587, Ea=(0,'kJ/mol'), T0=(1,'K'), comment="""Estimated using template (Y_rad;Y_rad) for rate rule (Si_rad;H_rad)
Ea raised from -0.8 to 0 kJ/mol."""),
)

reaction(
    label = 'reaction3',
    reactants = ['[SiH]=[SiH][SiH2](50)', '[H](16)'],
    products = ['[SiH2][SiH]=[SiH2](28)'],
    transitionState = 'TS3',
    kinetics = Arrhenius(A=(7.20571e+06,'m^3/(mol*s)'), n=0.100587, Ea=(0,'kJ/mol'), T0=(1,'K'), comment="""Estimated using template (Y_rad;Y_rad) for rate rule (Si_rad;H_rad)
Ea raised from -0.8 to 0 kJ/mol."""),
)

reaction(
    label = 'reaction4',
    reactants = ['[SiH2][Si][SiH3](47)'],
    products = ['[SiH2][SiH]=[SiH2](28)'],
    transitionState = 'TS4',
    kinetics = Arrhenius(A=(2.505e+12,'1/s'), n=0, Ea=(19.6648,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Exact match found for rate rule (SiSiSiH3)
Multiplied by reaction path degeneracy 3"""),
)

reaction(
    label = 'reaction5',
    reactants = ['[SiH][SiH2][SiH2](46)'],
    products = ['[SiH2][SiH]=[SiH2](28)'],
    transitionState = 'TS5',
    kinetics = Arrhenius(A=(2e+12,'1/s'), n=0, Ea=(33.8904,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Exact match found for rate rule (SiHSiH2)
Multiplied by reaction path degeneracy 2"""),
)

reaction(
    label = 'reaction6',
    reactants = ['H2(7)', '[Si]=[SiH][SiH2](34)'],
    products = ['[SiH2][SiH]=[SiH2](28)'],
    transitionState = 'TS6',
    kinetics = Arrhenius(A=(2.1e+06,'cm^3/(mol*s)'), n=1.97, Ea=(0,'kJ/mol'), T0=(1,'K'), Tmin=(400,'K'), Tmax=(2000,'K'), comment="""Exact match found for rate rule (Si2S;H_H)
Multiplied by reaction path degeneracy 2
Ea raised from -1.9 to 0 kJ/mol."""),
)

reaction(
    label = 'reaction7',
    reactants = ['SiH2SiH2(9)', 'SiH(11)'],
    products = ['[SiH2][SiH]=[SiH2](28)'],
    transitionState = 'TS7',
    kinetics = Arrhenius(A=(7.44e+14,'cm^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), Tmin=(295,'K'), Tmax=(595,'K'), comment="""Exact match found for rate rule (Si2S;Si_H)
Multiplied by reaction path degeneracy 4
Ea raised from -1.9 to 0 kJ/mol."""),
)

network(
    label = '24',
    isomers = [
        '[SiH2][SiH]=[SiH2](28)',
    ],
    reactants = [
        ('SiH3(3)', 'SiH2Si(12)'),
        ('SiH2SiH2(9)', 'SiH(11)'),
    ],
    bathGas = {
        'He': 0.25,
        'Ne': 0.25,
        'Ar': 0.25,
        'N2': 0.25,
    },
)

pressureDependence(
    label = '24',
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

