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
    label = '[Si]=[Si][SiH2](69)',
    structure = SMILES('[Si]=[Si][SiH2]'),
    E0 = (796.832,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([180,180,180,180,180,1119.52,1119.55,1119.61],'cm^-1')),
        HinderedRotor(inertia=(0.18105,'amu*angstrom^2'), symmetry=1, barrier=(4.1627,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 5,
    opticalIsomers = 1,
    molecularWeight = (86.2724,'amu'),
    collisionModel = TransportData(shapeIndex=2, epsilon=(1971.36,'J/mol'), sigma=(5.118e-10,'m'), dipoleMoment=(0,'C*m'), polarizability=(0,'angstroms^3'), rotrelaxcollnum=0, comment="""Epsilon & sigma estimated with fixed Lennard Jones Parameters. This is the fallback method! Try improving transport databases!"""),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[2.19926,0.0501533,-0.000111773,1.11086e-07,-3.96258e-11,95891.6,18.1834], Tmin=(100,'K'), Tmax=(897.519,'K')), NASAPolynomial(coeffs=[4.52867,0.0137853,-7.56147e-06,1.41959e-09,-9.29452e-14,96520.1,13.0281], Tmin=(897.519,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(796.832,'kJ/mol'), comment="""Thermo group additivity estimation: group(Sis-H3Sid) + other(R) + group(Sid-HSis) + other(R) + group(Sid-H2) + other(R) + radical(SidsJ_Si) + radical(Si=SiJ2_triplet) + radical(SisJ_Si_H2)"""),
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
    label = '[Si]=[SiH][SiH2](70)',
    structure = SMILES('[Si]=[SiH][SiH2]'),
    E0 = (735.484,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([180,180,180,180,765.544,1704.08],'cm^-1')),
    ],
    spinMultiplicity = 4,
    opticalIsomers = 1,
    molecularWeight = (85.2644,'amu'),
    collisionModel = TransportData(shapeIndex=2, epsilon=(1971.36,'J/mol'), sigma=(5.118e-10,'m'), dipoleMoment=(0,'C*m'), polarizability=(0,'angstroms^3'), rotrelaxcollnum=0, comment="""Epsilon & sigma estimated with fixed Lennard Jones Parameters. This is the fallback method! Try improving transport databases!"""),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[2.70684,0.0351104,-7.66436e-05,7.45422e-08,-2.61853e-11,88498.6,3.63009], Tmin=(100,'K'), Tmax=(898.098,'K')), NASAPolynomial(coeffs=[5.08622,0.00823449,-4.56737e-06,8.57283e-10,-5.59561e-14,88727.7,-3.93842], Tmin=(898.098,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(735.484,'kJ/mol'), comment="""Thermo group additivity estimation: group(Sis-Sis4) + other(R) + group(Sid-H2) + other(R) + group(si) + other(R) + radical(SiJ_LP_Si) + radical(Si=SiJ2_triplet)"""),
)

species(
    label = 'SiH(10)',
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
    label = '[Si][SiH]=[SiH](71)',
    structure = SMILES('[Si][SiH]=[SiH]'),
    E0 = (1089.73,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([207.718,207.718,207.719,207.719,207.719,207.72,207.72,207.721,207.721],'cm^-1')),
    ],
    spinMultiplicity = 5,
    opticalIsomers = 1,
    molecularWeight = (86.2724,'amu'),
    collisionModel = TransportData(shapeIndex=2, epsilon=(1971.36,'J/mol'), sigma=(5.118e-10,'m'), dipoleMoment=(0,'C*m'), polarizability=(0,'angstroms^3'), rotrelaxcollnum=0, comment="""Epsilon & sigma estimated with fixed Lennard Jones Parameters. This is the fallback method! Try improving transport databases!"""),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[1.59565,0.0601428,-0.000119633,1.07716e-07,-3.60181e-11,131144,16.8277], Tmin=(100,'K'), Tmax=(884.417,'K')), NASAPolynomial(coeffs=[9.42641,0.00871003,-5.23701e-06,1.0093e-09,-6.7055e-14,130385,-16.4481], Tmin=(884.417,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(1089.73,'kJ/mol'), comment="""Thermo group additivity estimation: group(Sis-H3Sid) + other(R) + group(Sid-HSis) + other(R) + group(Sid-H2) + other(R) + radical(SidsJ_Si) + radical(CJ3)"""),
)

species(
    label = '[Si][SiH2][SiH3](72)',
    structure = SMILES('[Si][SiH2][SiH3]'),
    E0 = (1010.3,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([300,800,800,800,800,800,1600,1600,1600,1600,1600],'cm^-1')),
        HinderedRotor(inertia=(0.156089,'amu*angstrom^2'), symmetry=1, barrier=(3.5888,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 4,
    opticalIsomers = 1,
    molecularWeight = (87.2803,'amu'),
    collisionModel = TransportData(shapeIndex=2, epsilon=(1971.36,'J/mol'), sigma=(5.118e-10,'m'), dipoleMoment=(0,'C*m'), polarizability=(0,'angstroms^3'), rotrelaxcollnum=0, comment="""Epsilon & sigma estimated with fixed Lennard Jones Parameters. This is the fallback method! Try improving transport databases!"""),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[1.63824,0.0553401,-9.17519e-05,7.33933e-08,-2.27395e-11,121593,15.4319], Tmin=(100,'K'), Tmax=(798.462,'K')), NASAPolynomial(coeffs=[10.8491,0.00919269,-5.05027e-06,9.9563e-10,-6.93835e-14,120122,-26.931], Tmin=(798.462,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(1010.3,'kJ/mol'), comment="""Thermo group additivity estimation: group(Sis-H3si) + other(R) + group(Sis-H3si) + other(R) + group(si) + other(R) + radical(CJ3)"""),
)

species(
    label = '[SiH2]=[SiH2](15)',
    structure = SMILES('[SiH2]=[SiH2]'),
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
    label = '[SiH](63)',
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
    E0 = (803.709,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS2',
    E0 = (1008.64,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS3',
    E0 = (726.881,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS4',
    E0 = (843.257,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS5',
    E0 = (1301.53,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS6',
    E0 = (1029.96,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS7',
    E0 = (1083.75,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

reaction(
    label = 'reaction1',
    reactants = ['[Si]=[SiH2](37)', 'SiH3(9)'],
    products = ['[Si]=[SiH][SiH2](44)'],
    transitionState = 'TS1',
    kinetics = Arrhenius(A=(5.58e+14,'cm^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), Tmin=(295,'K'), Tmax=(595,'K'), comment="""Exact match found for rate rule (Si2S;Si_H)
Multiplied by reaction path degeneracy 3
Ea raised from -1.9 to 0 kJ/mol."""),
)

reaction(
    label = 'reaction2',
    reactants = ['[H](13)', '[Si]=[Si][SiH2](69)'],
    products = ['[Si]=[SiH][SiH2](44)'],
    transitionState = 'TS2',
    kinetics = Arrhenius(A=(7.20571e+06,'m^3/(mol*s)'), n=0.100587, Ea=(0,'kJ/mol'), T0=(1,'K'), comment="""Estimated using template (Y_rad;Y_rad) for rate rule (Si_rad;H_rad)
Ea raised from -0.8 to 0 kJ/mol."""),
)

reaction(
    label = 'reaction3',
    reactants = ['H2(3)', '[Si]=[SiH][SiH2](70)'],
    products = ['[Si]=[SiH][SiH2](44)'],
    transitionState = 'TS3',
    kinetics = Arrhenius(A=(2.1e+06,'cm^3/(mol*s)'), n=1.97, Ea=(0,'kJ/mol'), T0=(1,'K'), Tmin=(400,'K'), Tmax=(2000,'K'), comment="""Exact match found for rate rule (Si2S;H_H)
Multiplied by reaction path degeneracy 2
Ea raised from -1.9 to 0 kJ/mol."""),
)

reaction(
    label = 'reaction4',
    reactants = ['SiH(10)', 'SiH2Si(11)'],
    products = ['[Si]=[SiH][SiH2](44)'],
    transitionState = 'TS4',
    kinetics = Arrhenius(A=(3.72e+14,'cm^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), Tmin=(295,'K'), Tmax=(595,'K'), comment="""Exact match found for rate rule (Si2S;Si_H)
Multiplied by reaction path degeneracy 2
Ea raised from -1.9 to 0 kJ/mol."""),
)

reaction(
    label = 'reaction5',
    reactants = ['[H](13)', '[Si][SiH]=[SiH](71)'],
    products = ['[Si]=[SiH][SiH2](44)'],
    transitionState = 'TS5',
    kinetics = Arrhenius(A=(7.20571e+06,'m^3/(mol*s)'), n=0.100587, Ea=(0,'kJ/mol'), T0=(1,'K'), comment="""Estimated using template (Y_rad;Y_rad) for rate rule (Si_rad;H_rad)
Ea raised from -0.8 to 0 kJ/mol."""),
)

reaction(
    label = 'reaction6',
    reactants = ['[Si][SiH2][SiH3](72)'],
    products = ['[Si]=[SiH][SiH2](44)'],
    transitionState = 'TS6',
    kinetics = Arrhenius(A=(2.505e+12,'1/s'), n=0, Ea=(19.6648,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Exact match found for rate rule (SiSiSiH3)
Multiplied by reaction path degeneracy 3"""),
)

reaction(
    label = 'reaction7',
    reactants = ['[SiH2]=[SiH2](15)', '[SiH](63)'],
    products = ['[Si]=[SiH][SiH2](44)'],
    transitionState = 'TS7',
    kinetics = Arrhenius(A=(1.86e+14,'cm^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), Tmin=(295,'K'), Tmax=(595,'K'), comment="""Exact match found for rate rule (Si2S;Si_H)
Ea raised from -1.9 to 0 kJ/mol."""),
)

network(
    label = '56',
    isomers = [
        '[Si]=[SiH][SiH2](44)',
    ],
    reactants = [
        ('[Si]=[SiH2](37)', 'SiH3(9)'),
    ],
    bathGas = {
        'He': 0.25,
        'Ar': 0.25,
        'Ne': 0.25,
        'N2': 0.25,
    },
)

pressureDependence(
    label = '56',
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

