species(
    label = '[SiH2]=[SiH][SiH3](25)',
    structure = SMILES('[SiH2]=[SiH][SiH3]'),
    E0 = (291.686,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([300,800,800,800,800,800,800,800,800,800,1600,1600,1600,1600,1600,1600,1600,1600,1600,1600],'cm^-1')),
        HinderedRotor(inertia=(0.156089,'amu*angstrom^2'), symmetry=1, barrier=(3.5888,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 1,
    opticalIsomers = 1,
    molecularWeight = (90.3041,'amu'),
    collisionModel = TransportData(shapeIndex=2, epsilon=(1971.36,'J/mol'), sigma=(5.118e-10,'m'), dipoleMoment=(0,'C*m'), polarizability=(0,'angstroms^3'), rotrelaxcollnum=0, comment="""Epsilon & sigma estimated with fixed Lennard Jones Parameters. This is the fallback method! Try improving transport databases!"""),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[1.68958,0.054172,-7.14271e-05,5.1493e-08,-1.50454e-11,35161.9,16.0061], Tmin=(100,'K'), Tmax=(832.607,'K')), NASAPolynomial(coeffs=[8.85939,0.0197272,-9.37277e-06,1.8066e-09,-1.26618e-13,33968,-17.2707], Tmin=(832.607,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(291.686,'kJ/mol'), comment="""Thermo group additivity estimation: group(Sis-H3Sid) + other(R) + group(Sid-HSis) + other(R) + group(Sid-H2) + other(R)"""),
)

species(
    label = '[SiH3][Si][SiH3](32)',
    structure = SMILES('[SiH3][Si][SiH3]'),
    E0 = (340.821,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([300,800,800,800,800,800,800,800,800,800,1600,1600,1600,1600,1600,1600,1600,1600,1600],'cm^-1')),
        HinderedRotor(inertia=(0.156089,'amu*angstrom^2'), symmetry=1, barrier=(3.5888,'kJ/mol'), semiclassical=False),
        HinderedRotor(inertia=(0.156089,'amu*angstrom^2'), symmetry=1, barrier=(3.5888,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 1,
    opticalIsomers = 1,
    molecularWeight = (90.3041,'amu'),
    collisionModel = TransportData(shapeIndex=2, epsilon=(1971.36,'J/mol'), sigma=(5.118e-10,'m'), dipoleMoment=(0,'C*m'), polarizability=(0,'angstroms^3'), rotrelaxcollnum=0, comment="""Epsilon & sigma estimated with fixed Lennard Jones Parameters. This is the fallback method! Try improving transport databases!"""),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[1.81137,0.0516991,-6.58165e-05,4.68753e-08,-1.37233e-11,41066.9,15.6718], Tmin=(100,'K'), Tmax=(826.341,'K')), NASAPolynomial(coeffs=[8.14386,0.0210445,-1.01686e-05,1.97815e-09,-1.39523e-13,40020.4,-13.6706], Tmin=(826.341,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(340.821,'kJ/mol'), comment="""Thermo group additivity estimation: group(Sis-H3si) + other(R) + group(Sis-H3si) + other(R) + group(si) + other(R)"""),
)

species(
    label = '[SiH][SiH2][SiH3](23)',
    structure = SMILES('[SiH][SiH2][SiH3]'),
    E0 = (340.587,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([300,800,800,800,800,800,800,800,800,800,1600,1600,1600,1600,1600,1600,1600,1600,1600],'cm^-1')),
        HinderedRotor(inertia=(0.156089,'amu*angstrom^2'), symmetry=1, barrier=(3.5888,'kJ/mol'), semiclassical=False),
        HinderedRotor(inertia=(0.156089,'amu*angstrom^2'), symmetry=1, barrier=(3.5888,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 1,
    opticalIsomers = 1,
    molecularWeight = (90.3041,'amu'),
    collisionModel = TransportData(shapeIndex=2, epsilon=(1971.36,'J/mol'), sigma=(5.118e-10,'m'), dipoleMoment=(0,'C*m'), polarizability=(0,'angstroms^3'), rotrelaxcollnum=0, comment="""Epsilon & sigma estimated with fixed Lennard Jones Parameters. This is the fallback method! Try improving transport databases!"""),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[1.64952,0.0554549,-7.60163e-05,5.75743e-08,-1.77158e-11,41044.3,16.8628], Tmin=(100,'K'), Tmax=(791.3,'K')), NASAPolynomial(coeffs=[8.54271,0.0206104,-9.96515e-06,1.92708e-09,-1.34988e-13,39953.4,-14.7793], Tmin=(791.3,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(340.587,'kJ/mol'), comment="""Thermo group additivity estimation: group(Sis-H2siSis) + other(R) + group(Sis-H3Sis) + other(R) + group(si) + other(R)"""),
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
    label = '[Si]=[SiH][SiH3](29)',
    structure = SMILES('[Si]=[SiH][SiH3]'),
    E0 = (428.094,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([300,800,800,800,800,800,800,1600,1600,1600,1600,1600,1600,1600],'cm^-1')),
        HinderedRotor(inertia=(0.156089,'amu*angstrom^2'), symmetry=1, barrier=(3.5888,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 1,
    opticalIsomers = 1,
    molecularWeight = (88.2883,'amu'),
    collisionModel = TransportData(shapeIndex=2, epsilon=(1971.36,'J/mol'), sigma=(5.118e-10,'m'), dipoleMoment=(0,'C*m'), polarizability=(0,'angstroms^3'), rotrelaxcollnum=0, comment="""Epsilon & sigma estimated with fixed Lennard Jones Parameters. This is the fallback method! Try improving transport databases!"""),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[1.62003,0.0567256,-8.63902e-05,7.2386e-08,-2.41937e-11,51569.3,25.4188], Tmin=(100,'K'), Tmax=(819.632,'K')), NASAPolynomial(coeffs=[7.84115,0.0207062,-1.01152e-05,1.92252e-09,-1.31999e-13,50739.5,-2.19756], Tmin=(819.632,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(428.094,'kJ/mol'), comment="""Thermo group additivity estimation: group(Sis-H3Sid) + other(R) + group(Sid-HSis) + other(R) + group(si) + other(R)"""),
)

species(
    label = 'SiH2(5)',
    structure = SMILES('[SiH2]'),
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
    label = 'Si2H5(4)',
    structure = SMILES('[SiH2][SiH3]'),
    E0 = (207.489,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([300,800,800,800,800,800,800,1600,1600,1600,1600,1600,1600,1600],'cm^-1')),
        HinderedRotor(inertia=(0.156089,'amu*angstrom^2'), symmetry=1, barrier=(3.5888,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 1,
    molecularWeight = (61.2107,'amu'),
    collisionModel = TransportData(shapeIndex=2, epsilon=(920.412,'J/mol'), sigma=(4.443e-10,'m'), dipoleMoment=(0,'C*m'), polarizability=(0,'angstroms^3'), rotrelaxcollnum=0, comment="""Epsilon & sigma estimated with fixed Lennard Jones Parameters. This is the fallback method! Try improving transport databases!"""),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[2.58316,0.0277325,-2.2448e-05,9.20907e-09,-1.50792e-12,25009,12.3685], Tmin=(100,'K'), Tmax=(1456.77,'K')), NASAPolynomial(coeffs=[9.15912,0.00967627,-3.85587e-06,7.0071e-10,-4.77821e-14,23093.1,-21.8307], Tmin=(1456.77,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(207.489,'kJ/mol'), comment="""Thermo library: SiliconHydrideLibrary + radical(SisJ_Si_H2)"""),
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
    label = 'SiH3SiH(6)',
    structure = SMILES('[SiH][SiH3]'),
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
    label = '[SiH]=[SiH2](24)',
    structure = SMILES('[SiH]=[SiH2]'),
    E0 = (383.981,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([436.739,436.878,436.911,436.975,437.062,900.642,2142.02,2142.1,2142.17],'cm^-1')),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 1,
    molecularWeight = (59.1948,'amu'),
    collisionModel = TransportData(shapeIndex=2, epsilon=(920.412,'J/mol'), sigma=(4.443e-10,'m'), dipoleMoment=(0,'C*m'), polarizability=(0,'angstroms^3'), rotrelaxcollnum=0, comment="""Epsilon & sigma estimated with fixed Lennard Jones Parameters. This is the fallback method! Try improving transport databases!"""),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[2.95596,0.0247776,-3.73963e-05,3.10077e-08,-1.02309e-11,46218.1,12.3641], Tmin=(100,'K'), Tmax=(822.252,'K')), NASAPolynomial(coeffs=[5.80551,0.00872293,-4.10881e-06,7.75912e-10,-5.31657e-14,45823.6,-0.374989], Tmin=(822.252,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(383.981,'kJ/mol'), comment="""Thermo library: SiliconHydrideLibrary"""),
)

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
    label = '[SiH2]=[Si][SiH3](30)',
    structure = SMILES('[SiH2]=[Si][SiH3]'),
    E0 = (420.252,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([300,800,800,800,800,800,800,800,800,1600,1600,1600,1600,1600,1600,1600,1600],'cm^-1')),
        HinderedRotor(inertia=(0.156089,'amu*angstrom^2'), symmetry=1, barrier=(3.5888,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 1,
    molecularWeight = (89.2962,'amu'),
    collisionModel = TransportData(shapeIndex=2, epsilon=(1971.36,'J/mol'), sigma=(5.118e-10,'m'), dipoleMoment=(0,'C*m'), polarizability=(0,'angstroms^3'), rotrelaxcollnum=0, comment="""Epsilon & sigma estimated with fixed Lennard Jones Parameters. This is the fallback method! Try improving transport databases!"""),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[1.65846,0.0579283,-9.93206e-05,8.95008e-08,-3.10471e-11,50622.8,18.1485], Tmin=(100,'K'), Tmax=(850.995,'K')), NASAPolynomial(coeffs=[6.99026,0.0200793,-1.00664e-05,1.92166e-09,-1.31256e-13,50178.3,-3.9935], Tmin=(850.995,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(420.252,'kJ/mol'), comment="""Thermo group additivity estimation: group(Sis-H3Sid) + other(R) + group(Sid-HSis) + other(R) + group(Sid-H2) + other(R) + radical(SidsJ_Si)"""),
)

species(
    label = '[SiH]=[SiH][SiH3](31)',
    structure = SMILES('[SiH]=[SiH][SiH3]'),
    E0 = (420.252,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([300,800,800,800,800,800,800,800,800,1600,1600,1600,1600,1600,1600,1600,1600],'cm^-1')),
        HinderedRotor(inertia=(0.156089,'amu*angstrom^2'), symmetry=1, barrier=(3.5888,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 1,
    molecularWeight = (89.2962,'amu'),
    collisionModel = TransportData(shapeIndex=2, epsilon=(1971.36,'J/mol'), sigma=(5.118e-10,'m'), dipoleMoment=(0,'C*m'), polarizability=(0,'angstroms^3'), rotrelaxcollnum=0, comment="""Epsilon & sigma estimated with fixed Lennard Jones Parameters. This is the fallback method! Try improving transport databases!"""),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[1.65846,0.0579283,-9.93206e-05,8.95008e-08,-3.10471e-11,50622.8,18.1485], Tmin=(100,'K'), Tmax=(850.995,'K')), NASAPolynomial(coeffs=[6.99026,0.0200793,-1.00664e-05,1.92166e-09,-1.31256e-13,50178.3,-3.9935], Tmin=(850.995,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(420.252,'kJ/mol'), comment="""Thermo group additivity estimation: group(Sis-H3Sid) + other(R) + group(Sid-HSis) + other(R) + group(Sid-H2) + other(R) + radical(SidsJ_Si)"""),
)

species(
    label = '[SiH][SiH]=[SiH2](33)',
    structure = SMILES('[SiH][SiH]=[SiH2]'),
    E0 = (414.721,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([300,800,800,800,800,800,800,1600,1600,1600,1600,1600,1600,1600],'cm^-1')),
        HinderedRotor(inertia=(0.156089,'amu*angstrom^2'), symmetry=1, barrier=(3.5888,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 1,
    opticalIsomers = 1,
    molecularWeight = (88.2883,'amu'),
    collisionModel = TransportData(shapeIndex=2, epsilon=(1971.36,'J/mol'), sigma=(5.118e-10,'m'), dipoleMoment=(0,'C*m'), polarizability=(0,'angstroms^3'), rotrelaxcollnum=0, comment="""Epsilon & sigma estimated with fixed Lennard Jones Parameters. This is the fallback method! Try improving transport databases!"""),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[1.57145,0.0596799,-0.000105899,9.3612e-08,-3.1472e-11,49960.8,7.24834], Tmin=(100,'K'), Tmax=(870.08,'K')), NASAPolynomial(coeffs=[8.30738,0.0157909,-7.9586e-06,1.49926e-09,-1.00801e-13,49277.8,-21.5004], Tmin=(870.08,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(414.721,'kJ/mol'), comment="""Thermo group additivity estimation: group(Sis-Sis4) + other(R) + group(Sid-H2) + other(R) + group(si) + other(R)"""),
)

species(
    label = '[Si][SiH3](19)',
    structure = SMILES('[Si][SiH3]'),
    E0 = (388.911,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([180,566.863,1060.78,1061.04,1061.79,1062.11,2193.61,4000,4000],'cm^-1')),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 1,
    molecularWeight = (59.1948,'amu'),
    collisionModel = TransportData(shapeIndex=2, epsilon=(920.412,'J/mol'), sigma=(4.443e-10,'m'), dipoleMoment=(0,'C*m'), polarizability=(0,'angstroms^3'), rotrelaxcollnum=0, comment="""Epsilon & sigma estimated with fixed Lennard Jones Parameters. This is the fallback method! Try improving transport databases!"""),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[3.46986,0.00884507,2.93107e-06,-8.83578e-09,3.56123e-12,46796.7,9.83644], Tmin=(100,'K'), Tmax=(1057.05,'K')), NASAPolynomial(coeffs=[5.91224,0.00616349,-2.57354e-06,5.07492e-10,-3.71892e-14,45913.8,-3.8159], Tmin=(1057.05,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(388.911,'kJ/mol'), comment="""Thermo library: SiliconHydrideLibrary + radical(SiJ_LP_Si)"""),
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
    label = '[SiH][Si][SiH3](36)',
    structure = SMILES('[SiH][Si][SiH3]'),
    E0 = (574.973,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([180,1063.08,1063.08,1063.08,1063.08,1063.08,1063.08,1063.08,1063.08,1063.08,1063.08,1063.08,2259.89],'cm^-1')),
        HinderedRotor(inertia=(0.0522239,'amu*angstrom^2'), symmetry=1, barrier=(1.20073,'kJ/mol'), semiclassical=False),
        HinderedRotor(inertia=(0.0522239,'amu*angstrom^2'), symmetry=1, barrier=(1.20073,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 1,
    opticalIsomers = 1,
    molecularWeight = (88.2883,'amu'),
    collisionModel = TransportData(shapeIndex=2, epsilon=(1971.36,'J/mol'), sigma=(5.118e-10,'m'), dipoleMoment=(0,'C*m'), polarizability=(0,'angstroms^3'), rotrelaxcollnum=0, comment="""Epsilon & sigma estimated with fixed Lennard Jones Parameters. This is the fallback method! Try improving transport databases!"""),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[1.68615,0.0569073,-9.39953e-05,8.40243e-08,-2.92526e-11,69230.9,34.6784], Tmin=(100,'K'), Tmax=(843.571,'K')), NASAPolynomial(coeffs=[6.65294,0.0217691,-1.09108e-05,2.08069e-09,-1.42357e-13,68805.2,14.005], Tmin=(843.571,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(574.973,'kJ/mol'), comment="""Thermo group additivity estimation: group(Sis-H3si) + other(R) + group(si) + other(R) + group(si) + other(R)"""),
)

species(
    label = '[SiH][SiH2](18)',
    structure = SMILES('[SiH][SiH2]'),
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
    label = '[SiH][SiH][SiH3](54)',
    structure = SMILES('[SiH][SiH][SiH3]'),
    E0 = (437.131,'kJ/mol'),
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
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[1.62357,0.0573692,-9.43928e-05,8.12798e-08,-2.71641e-11,52655.4,17.0113], Tmin=(100,'K'), Tmax=(851.88,'K')), NASAPolynomial(coeffs=[8.12399,0.0177522,-8.62162e-06,1.62501e-09,-1.10307e-13,51877.8,-11.3705], Tmin=(851.88,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(437.131,'kJ/mol'), comment="""Thermo group additivity estimation: group(Sis-H2siSis) + other(R) + group(Sis-H3Sis) + other(R) + group(si) + other(R) + radical(SisJ_SiLP)"""),
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
    label = '[Si][SiH2][SiH3](48)',
    structure = SMILES('[Si][SiH2][SiH3]'),
    E0 = (441.31,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([300,800,800,800,800,800,800,800,800,1600,1600,1600,1600,1600,1600,1600,1600],'cm^-1')),
        HinderedRotor(inertia=(0.156089,'amu*angstrom^2'), symmetry=1, barrier=(3.5888,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 1,
    molecularWeight = (89.2962,'amu'),
    collisionModel = TransportData(shapeIndex=2, epsilon=(1971.36,'J/mol'), sigma=(5.118e-10,'m'), dipoleMoment=(0,'C*m'), polarizability=(0,'angstroms^3'), rotrelaxcollnum=0, comment="""Epsilon & sigma estimated with fixed Lennard Jones Parameters. This is the fallback method! Try improving transport databases!"""),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[2.34289,0.038879,-4.45676e-05,2.8364e-08,-7.46509e-12,53135,13.7575], Tmin=(100,'K'), Tmax=(911.785,'K')), NASAPolynomial(coeffs=[7.42688,0.0165753,-7.87476e-06,1.53506e-09,-1.0885e-13,52207.9,-10.3002], Tmin=(911.785,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(441.31,'kJ/mol'), comment="""Thermo group additivity estimation: group(Sis-H2siSis) + other(R) + group(Sis-H3Sis) + other(R) + group(si) + other(R) + radical(SiJ_LP_Si)"""),
)

species(
    label = '[SiH][SiH2][SiH](55)',
    structure = SMILES('[SiH][SiH2][SiH]'),
    E0 = (574.973,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([180,1063.08,1063.08,1063.08,1063.08,1063.08,1063.08,1063.08,1063.08,1063.08,1063.08,1063.08,2259.89],'cm^-1')),
        HinderedRotor(inertia=(0.0522239,'amu*angstrom^2'), symmetry=1, barrier=(1.20073,'kJ/mol'), semiclassical=False),
        HinderedRotor(inertia=(0.0522239,'amu*angstrom^2'), symmetry=1, barrier=(1.20073,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 1,
    opticalIsomers = 1,
    molecularWeight = (88.2883,'amu'),
    collisionModel = TransportData(shapeIndex=2, epsilon=(1971.36,'J/mol'), sigma=(5.118e-10,'m'), dipoleMoment=(0,'C*m'), polarizability=(0,'angstroms^3'), rotrelaxcollnum=0, comment="""Epsilon & sigma estimated with fixed Lennard Jones Parameters. This is the fallback method! Try improving transport databases!"""),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[1.68615,0.0569073,-9.39953e-05,8.40243e-08,-2.92526e-11,69230.9,35.0838], Tmin=(100,'K'), Tmax=(843.571,'K')), NASAPolynomial(coeffs=[6.65294,0.0217691,-1.09108e-05,2.08069e-09,-1.42357e-13,68805.2,14.4104], Tmin=(843.571,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(574.973,'kJ/mol'), comment="""Thermo group additivity estimation: group(Sis-H3si) + other(R) + group(si) + other(R) + group(si) + other(R)"""),
)

species(
    label = 'Si2H2(15)',
    structure = SMILES('[SiH][SiH]'),
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
    E0 = (414.283,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS2',
    E0 = (565.533,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS3',
    E0 = (660.03,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS4',
    E0 = (632.057,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS5',
    E0 = (632.057,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS6',
    E0 = (360.486,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS7',
    E0 = (374.477,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS8',
    E0 = (409.464,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS9',
    E0 = (419.49,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS10',
    E0 = (508.525,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS11',
    E0 = (570.463,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS12',
    E0 = (649.17,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS13',
    E0 = (569.717,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS14',
    E0 = (566.283,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS15',
    E0 = (575.298,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS16',
    E0 = (648.935,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS17',
    E0 = (708.931,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS18',
    E0 = (653.115,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS19',
    E0 = (566.37,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS20',
    E0 = (569.717,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS21',
    E0 = (454.322,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS22',
    E0 = (541.301,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

reaction(
    label = 'reaction1',
    reactants = ['SiH4(1)', 'SiH2Si(12)'],
    products = ['[SiH2]=[SiH][SiH3](25)'],
    transitionState = 'TS1',
    kinetics = Arrhenius(A=(7.44e+14,'cm^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), Tmin=(295,'K'), Tmax=(595,'K'), comment="""Estimated using template (Si2S;Si_H) for rate rule (Si2S;SiH4)
Multiplied by reaction path degeneracy 4
Ea raised from -1.9 to 0 kJ/mol."""),
)

reaction(
    label = 'reaction2',
    reactants = ['SiH3(3)', '[SiH]=[SiH2](24)'],
    products = ['[SiH2]=[SiH][SiH3](25)'],
    transitionState = 'TS2',
    kinetics = Arrhenius(A=(7.20571e+06,'m^3/(mol*s)'), n=0.100587, Ea=(0,'kJ/mol'), T0=(1,'K'), comment="""Estimated using template (Y_rad;Y_rad) for rate rule (Si_rad;Si_silyl)
Ea raised from -0.8 to 0 kJ/mol."""),
)

reaction(
    label = 'reaction3',
    reactants = ['[SiH2][SiH]=[SiH2](28)', '[H](16)'],
    products = ['[SiH2]=[SiH][SiH3](25)'],
    transitionState = 'TS3',
    kinetics = Arrhenius(A=(7.20571e+06,'m^3/(mol*s)'), n=0.100587, Ea=(0,'kJ/mol'), T0=(1,'K'), comment="""Estimated using template (Y_rad;Y_rad) for rate rule (Si_rad;H_rad)
Ea raised from -0.8 to 0 kJ/mol."""),
)

reaction(
    label = 'reaction4',
    reactants = ['[H](16)', '[SiH2]=[Si][SiH3](30)'],
    products = ['[SiH2]=[SiH][SiH3](25)'],
    transitionState = 'TS4',
    kinetics = Arrhenius(A=(7.20571e+06,'m^3/(mol*s)'), n=0.100587, Ea=(0,'kJ/mol'), T0=(1,'K'), comment="""Estimated using template (Y_rad;Y_rad) for rate rule (Si_rad;H_rad)
Ea raised from -0.8 to 0 kJ/mol."""),
)

reaction(
    label = 'reaction5',
    reactants = ['[H](16)', '[SiH]=[SiH][SiH3](31)'],
    products = ['[SiH2]=[SiH][SiH3](25)'],
    transitionState = 'TS5',
    kinetics = Arrhenius(A=(7.20571e+06,'m^3/(mol*s)'), n=0.100587, Ea=(0,'kJ/mol'), T0=(1,'K'), comment="""Estimated using template (Y_rad;Y_rad) for rate rule (Si_rad;H_rad)
Ea raised from -0.8 to 0 kJ/mol."""),
)

reaction(
    label = 'reaction6',
    reactants = ['[SiH3][Si][SiH3](32)'],
    products = ['[SiH2]=[SiH][SiH3](25)'],
    transitionState = 'TS6',
    kinetics = Arrhenius(A=(5.01e+12,'1/s'), n=0, Ea=(4.7,'kcal/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Matched reaction 4 H3SiSiSiH3 <=> SiH3Si2H4 in Silylene_to_Silene/training"""),
)

reaction(
    label = 'reaction7',
    reactants = ['[SiH][SiH2][SiH3](23)'],
    products = ['[SiH2]=[SiH][SiH3](25)'],
    transitionState = 'TS7',
    kinetics = Arrhenius(A=(2e+12,'1/s'), n=0, Ea=(8.1,'kcal/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Matched reaction 2 Si2H5SiH <=> SiH3Si2H4 in Silylene_to_Silene/training"""),
)

reaction(
    label = 'reaction8',
    reactants = ['H2(7)', '[SiH][SiH]=[SiH2](33)'],
    products = ['[SiH2]=[SiH][SiH3](25)'],
    transitionState = 'TS8',
    kinetics = Arrhenius(A=(7.6e+12,'cm^3/(mol*s)'), n=0, Ea=(3.3472,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Exact match found for rate rule (Si-Si-H;H_H)
Multiplied by reaction path degeneracy 2"""),
)

reaction(
    label = 'reaction9',
    reactants = ['H2(7)', '[Si]=[SiH][SiH3](29)'],
    products = ['[SiH2]=[SiH][SiH3](25)'],
    transitionState = 'TS9',
    kinetics = Arrhenius(A=(2.1e+06,'cm^3/(mol*s)'), n=1.97, Ea=(0,'kJ/mol'), T0=(1,'K'), Tmin=(400,'K'), Tmax=(2000,'K'), comment="""Exact match found for rate rule (Si2S;H_H)
Multiplied by reaction path degeneracy 2
Ea raised from -1.9 to 0 kJ/mol."""),
)

reaction(
    label = 'reaction10',
    reactants = ['SiH2(5)', 'SiH2SiH2(9)'],
    products = ['[SiH2]=[SiH][SiH3](25)'],
    transitionState = 'TS10',
    kinetics = Arrhenius(A=(925165,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), comment="""Estimated using an average for rate rule (SiH2;Si_H)
Multiplied by reaction path degeneracy 4
Ea raised from -39.3 to 0 kJ/mol."""),
)

reaction(
    label = 'reaction11',
    reactants = ['SiH3(3)', '[Si][SiH3](19)'],
    products = ['[SiH3][Si][SiH3](32)'],
    transitionState = 'TS11',
    kinetics = Arrhenius(A=(7.20571e+06,'m^3/(mol*s)'), n=0.100587, Ea=(0,'kJ/mol'), T0=(1,'K'), comment="""Estimated using template (Y_rad;Y_rad) for rate rule (Si_rad;Si_silyl)
Ea raised from -0.8 to 0 kJ/mol."""),
)

reaction(
    label = 'reaction12',
    reactants = ['[SiH2][Si][SiH3](47)', '[H](16)'],
    products = ['[SiH3][Si][SiH3](32)'],
    transitionState = 'TS12',
    kinetics = Arrhenius(A=(7.20571e+06,'m^3/(mol*s)'), n=0.100587, Ea=(0,'kJ/mol'), T0=(1,'K'), comment="""Estimated using template (Y_rad;Y_rad) for rate rule (Si_rad;H_rad)
Ea raised from -0.8 to 0 kJ/mol."""),
)

reaction(
    label = 'reaction13',
    reactants = ['H2(7)', '[SiH][Si][SiH3](36)'],
    products = ['[SiH3][Si][SiH3](32)'],
    transitionState = 'TS13',
    kinetics = Arrhenius(A=(7.6e+12,'cm^3/(mol*s)'), n=0, Ea=(3.3472,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Exact match found for rate rule (Si-Si-H;H_H)
Multiplied by reaction path degeneracy 2"""),
)

reaction(
    label = 'reaction14',
    reactants = ['SiH3(3)', '[SiH][SiH2](18)'],
    products = ['[SiH][SiH2][SiH3](23)'],
    transitionState = 'TS14',
    kinetics = Arrhenius(A=(7.20571e+06,'m^3/(mol*s)'), n=0.100587, Ea=(0,'kJ/mol'), T0=(1,'K'), comment="""Estimated using template (Y_rad;Y_rad) for rate rule (Si_rad;Si_silyl)
Ea raised from -0.8 to 0 kJ/mol."""),
)

reaction(
    label = 'reaction15',
    reactants = ['Si2H5(4)', 'SiH(11)'],
    products = ['[SiH][SiH2][SiH3](23)'],
    transitionState = 'TS15',
    kinetics = Arrhenius(A=(7.20571e+06,'m^3/(mol*s)'), n=0.100587, Ea=(0,'kJ/mol'), T0=(1,'K'), comment="""Estimated using template (Y_rad;Y_rad) for rate rule (Si_rad;Si_rad)
Ea raised from -0.8 to 0 kJ/mol."""),
)

reaction(
    label = 'reaction16',
    reactants = ['[SiH][SiH][SiH3](54)', '[H](16)'],
    products = ['[SiH][SiH2][SiH3](23)'],
    transitionState = 'TS16',
    kinetics = Arrhenius(A=(7.20571e+06,'m^3/(mol*s)'), n=0.100587, Ea=(0,'kJ/mol'), T0=(1,'K'), comment="""Estimated using template (Y_rad;Y_rad) for rate rule (Si_rad;H_rad)
Ea raised from -0.8 to 0 kJ/mol."""),
)

reaction(
    label = 'reaction17',
    reactants = ['[H](16)', '[SiH][SiH2][SiH2](46)'],
    products = ['[SiH][SiH2][SiH3](23)'],
    transitionState = 'TS17',
    kinetics = Arrhenius(A=(7.20571e+06,'m^3/(mol*s)'), n=0.100587, Ea=(0,'kJ/mol'), T0=(1,'K'), comment="""Estimated using template (Y_rad;Y_rad) for rate rule (Si_rad;H_rad)
Ea raised from -0.8 to 0 kJ/mol."""),
)

reaction(
    label = 'reaction18',
    reactants = ['[Si][SiH2][SiH3](48)', '[H](16)'],
    products = ['[SiH][SiH2][SiH3](23)'],
    transitionState = 'TS18',
    kinetics = Arrhenius(A=(7.20571e+06,'m^3/(mol*s)'), n=0.100587, Ea=(0,'kJ/mol'), T0=(1,'K'), comment="""Estimated using template (Y_rad;Y_rad) for rate rule (H_rad;Si_rad)
Ea raised from -0.8 to 0 kJ/mol."""),
)

reaction(
    label = 'reaction19',
    reactants = ['H2(7)', '[SiH][Si][SiH3](36)'],
    products = ['[SiH][SiH2][SiH3](23)'],
    transitionState = 'TS19',
    kinetics = Arrhenius(A=(2.4e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Exact match found for rate rule (Si-Si-Si;H_H)
Multiplied by reaction path degeneracy 2
Ea raised from -2.1 to 0 kJ/mol."""),
)

reaction(
    label = 'reaction20',
    reactants = ['[SiH][SiH2][SiH](55)', 'H2(7)'],
    products = ['[SiH][SiH2][SiH3](23)'],
    transitionState = 'TS20',
    kinetics = Arrhenius(A=(1.52e+13,'cm^3/(mol*s)'), n=0, Ea=(3.3472,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Exact match found for rate rule (Si-Si-H;H_H)
Multiplied by reaction path degeneracy 4"""),
)

reaction(
    label = 'reaction21',
    reactants = ['SiH4(1)', 'Si2H2(15)'],
    products = ['[SiH][SiH2][SiH3](23)'],
    transitionState = 'TS21',
    kinetics = Arrhenius(A=(4.8e+10,'cm^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Exact match found for rate rule (Si-Si-H;SiH4)
Multiplied by reaction path degeneracy 8
Ea raised from -38.1 to 0 kJ/mol."""),
)

reaction(
    label = 'reaction22',
    reactants = ['SiH2(5)', 'SiH3SiH(6)'],
    products = ['[SiH][SiH2][SiH3](23)'],
    transitionState = 'TS22',
    kinetics = Arrhenius(A=(9.3e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), Tmin=(295,'K'), Tmax=(595,'K'), comment="""Exact match found for rate rule (SiH2;SiH3_Si)
Multiplied by reaction path degeneracy 3
Ea raised from -1.9 to 0 kJ/mol."""),
)

network(
    label = '23',
    isomers = [
        '[SiH2]=[SiH][SiH3](25)',
        '[SiH3][Si][SiH3](32)',
        '[SiH][SiH2][SiH3](23)',
    ],
    reactants = [
        ('SiH4(1)', 'SiH2Si(12)'),
        ('H2(7)', '[Si]=[SiH][SiH3](29)'),
        ('SiH2(5)', 'SiH2SiH2(9)'),
        ('Si2H5(4)', 'SiH(11)'),
        ('SiH2(5)', 'SiH3SiH(6)'),
    ],
    bathGas = {
        'He': 0.25,
        'Ne': 0.25,
        'Ar': 0.25,
        'N2': 0.25,
    },
)

pressureDependence(
    label = '23',
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

