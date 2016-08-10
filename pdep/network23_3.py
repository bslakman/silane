species(
    label = '[SiH2]=[SiH][SiH3](25)',
    structure = SMILES('[SiH2]=[SiH][SiH3]'),
    E0 = (283.336,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([300,800,800,800,800,800,800,800,800,800,1600,1600,1600,1600,1600,1600,1600,1600,1600,1600],'cm^-1')),
        HinderedRotor(inertia=(0.156089,'amu*angstrom^2'), symmetry=1, barrier=(3.5888,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 1,
    opticalIsomers = 1,
    molecularWeight = (90.3041,'amu'),
    collisionModel = TransportData(shapeIndex=2, epsilon=(1971.36,'J/mol'), sigma=(5.118e-10,'m'), dipoleMoment=(0,'C*m'), polarizability=(0,'angstroms^3'), rotrelaxcollnum=0, comment="""Epsilon & sigma estimated with fixed Lennard Jones Parameters. This is the fallback method! Try improving transport databases!"""),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[1.64567,0.0553112,-7.62364e-05,5.79951e-08,-1.78603e-11,34158.9,16.8031], Tmin=(100,'K'), Tmax=(791.879,'K')), NASAPolynomial(coeffs=[8.6208,0.0200803,-9.50549e-06,1.81951e-09,-1.26617e-13,33054.2,-15.2207], Tmin=(791.879,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(283.336,'kJ/mol'), comment="""Thermo group additivity estimation: group(Sis-H3Si) + other(R) + group(Sid-Sid-H-Si) + other(R) + group(Sid-Sid-H2) + other(R)"""),
)

species(
    label = '[SiH3][Si][SiH3](32)',
    structure = SMILES('[SiH3][Si][SiH3]'),
    E0 = (318.795,'kJ/mol'),
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
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[1.78087,0.0523466,-6.87024e-05,5.07815e-08,-1.53917e-11,38418.9,16.0112], Tmin=(100,'K'), Tmax=(800.364,'K')), NASAPolynomial(coeffs=[8.03961,0.0210656,-1.00741e-05,1.9444e-09,-1.3628e-13,37417.1,-12.7895], Tmin=(800.364,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(318.795,'kJ/mol'), comment="""Thermo group additivity estimation: group(Sis-H3Si) + other(R) + group(Sis-H3Si) + other(R) + group(si-Sis2) + other(R)"""),
)

species(
    label = '[SiH][SiH2][SiH3](23)',
    structure = SMILES('[SiH][SiH2][SiH3]'),
    E0 = (328.595,'kJ/mol'),
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
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[1.68957,0.0544172,-7.34003e-05,5.50023e-08,-1.67789e-11,39600.7,18.006], Tmin=(100,'K'), Tmax=(797.535,'K')), NASAPolynomial(coeffs=[8.42195,0.0206487,-9.88388e-06,1.90434e-09,-1.33185e-13,38526.9,-12.9503], Tmin=(797.535,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(328.595,'kJ/mol'), comment="""Thermo group additivity estimation: group(Sis-H2Si2) + other(R) + group(Sis-H3Si) + other(R) + group(si-Sis-H) + other(R)"""),
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
    E0 = (357.089,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([422.724,422.725,422.726,422.726,422.726,422.726],'cm^-1')),
    ],
    spinMultiplicity = 1,
    opticalIsomers = 1,
    molecularWeight = (58.1869,'amu'),
    collisionModel = TransportData(shapeIndex=2, epsilon=(920.412,'J/mol'), sigma=(4.443e-10,'m'), dipoleMoment=(0,'C*m'), polarizability=(0,'angstroms^3'), rotrelaxcollnum=0, comment="""Epsilon & sigma estimated with fixed Lennard Jones Parameters. This is the fallback method! Try improving transport databases!"""),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[3.11978,0.0202227,-2.29972e-05,1.45572e-08,-3.80123e-12,42978.8,8.5677], Tmin=(100,'K'), Tmax=(921.484,'K')), NASAPolynomial(coeffs=[5.82377,0.0084851,-3.89039e-06,7.33872e-10,-5.09079e-14,42480.5,-4.25636], Tmin=(921.484,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(357.089,'kJ/mol'), comment="""Thermo group additivity estimation: group(Sid-Sid-H2) + other(R) + group(si-Sid-H) + other(R)"""),
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
    label = '[SiH2][SiH]=[SiH2](28)',
    structure = SMILES('[SiH2][SiH]=[SiH2]'),
    E0 = (439.875,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([300,800,800,800,800,800,800,800,800,1600,1600,1600,1600,1600,1600,1600,1600],'cm^-1')),
        HinderedRotor(inertia=(0.156089,'amu*angstrom^2'), symmetry=1, barrier=(3.5888,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 1,
    molecularWeight = (89.2962,'amu'),
    collisionModel = TransportData(shapeIndex=2, epsilon=(1971.36,'J/mol'), sigma=(5.118e-10,'m'), dipoleMoment=(0,'C*m'), polarizability=(0,'angstroms^3'), rotrelaxcollnum=0, comment="""Epsilon & sigma estimated with fixed Lennard Jones Parameters. This is the fallback method! Try improving transport databases!"""),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[1.61145,0.05721,-9.29404e-05,7.87221e-08,-2.59046e-11,52986.3,17.821], Tmin=(100,'K'), Tmax=(854.581,'K')), NASAPolynomial(coeffs=[8.51791,0.0168611,-8.03739e-06,1.5039e-09,-1.01678e-13,52098.8,-12.6994], Tmin=(854.581,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(439.875,'kJ/mol'), comment="""Thermo group additivity estimation: group(Sis-H3Si) + other(R) + group(Sid-Sid-H-Si) + other(R) + group(Sid-Sid-H2) + other(R) + radical(SisJ_Si_H2)"""),
)

species(
    label = '[SiH2]=[Si][SiH3](30)',
    structure = SMILES('[SiH2]=[Si][SiH3]'),
    E0 = (411.902,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([300,800,800,800,800,800,800,800,800,1600,1600,1600,1600,1600,1600,1600,1600],'cm^-1')),
        HinderedRotor(inertia=(0.156089,'amu*angstrom^2'), symmetry=1, barrier=(3.5888,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 1,
    molecularWeight = (89.2962,'amu'),
    collisionModel = TransportData(shapeIndex=2, epsilon=(1971.36,'J/mol'), sigma=(5.118e-10,'m'), dipoleMoment=(0,'C*m'), polarizability=(0,'angstroms^3'), rotrelaxcollnum=0, comment="""Epsilon & sigma estimated with fixed Lennard Jones Parameters. This is the fallback method! Try improving transport databases!"""),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[1.65398,0.0585611,-0.000102144,9.30713e-08,-3.24259e-11,49618.2,18.8067], Tmin=(100,'K'), Tmax=(858.509,'K')), NASAPolynomial(coeffs=[6.68251,0.0205556,-1.02725e-05,1.95233e-09,-1.32754e-13,49291.9,-1.55743], Tmin=(858.509,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(411.902,'kJ/mol'), comment="""Thermo group additivity estimation: group(Sis-H3Si) + other(R) + group(Sid-Sid-H-Si) + other(R) + group(Sid-Sid-H2) + other(R) + radical(SidsJ_Si)"""),
)

species(
    label = '[SiH]=[SiH][SiH3](31)',
    structure = SMILES('[SiH]=[SiH][SiH3]'),
    E0 = (411.902,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([300,800,800,800,800,800,800,800,800,1600,1600,1600,1600,1600,1600,1600,1600],'cm^-1')),
        HinderedRotor(inertia=(0.156089,'amu*angstrom^2'), symmetry=1, barrier=(3.5888,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 1,
    molecularWeight = (89.2962,'amu'),
    collisionModel = TransportData(shapeIndex=2, epsilon=(1971.36,'J/mol'), sigma=(5.118e-10,'m'), dipoleMoment=(0,'C*m'), polarizability=(0,'angstroms^3'), rotrelaxcollnum=0, comment="""Epsilon & sigma estimated with fixed Lennard Jones Parameters. This is the fallback method! Try improving transport databases!"""),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[1.65398,0.0585611,-0.000102144,9.30713e-08,-3.24259e-11,49618.2,18.8067], Tmin=(100,'K'), Tmax=(858.509,'K')), NASAPolynomial(coeffs=[6.68251,0.0205556,-1.02725e-05,1.95233e-09,-1.32754e-13,49291.9,-1.55743], Tmin=(858.509,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(411.902,'kJ/mol'), comment="""Thermo group additivity estimation: group(Sis-H3Si) + other(R) + group(Sid-Sid-H-Si) + other(R) + group(Sid-Sid-H2) + other(R) + radical(SidsJ_Si)"""),
)

species(
    label = '[SiH][SiH]=[SiH2](33)',
    structure = SMILES('[SiH][SiH]=[SiH2]'),
    E0 = (491.995,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([300,800,800,800,800,800,800,1600,1600,1600,1600,1600,1600,1600],'cm^-1')),
        HinderedRotor(inertia=(0.156089,'amu*angstrom^2'), symmetry=1, barrier=(3.5888,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 1,
    opticalIsomers = 1,
    molecularWeight = (88.2883,'amu'),
    collisionModel = TransportData(shapeIndex=2, epsilon=(1971.36,'J/mol'), sigma=(5.118e-10,'m'), dipoleMoment=(0,'C*m'), polarizability=(0,'angstroms^3'), rotrelaxcollnum=0, comment="""Epsilon & sigma estimated with fixed Lennard Jones Parameters. This is the fallback method! Try improving transport databases!"""),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[1.81675,0.0529664,-8.71958e-05,7.56786e-08,-2.54749e-11,59247.2,25.7311], Tmin=(100,'K'), Tmax=(855.5,'K')), NASAPolynomial(coeffs=[7.44449,0.0173482,-8.42931e-06,1.58439e-09,-1.0731e-13,58624.8,1.44893], Tmin=(855.5,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(491.995,'kJ/mol'), comment="""Thermo group additivity estimation: group(Sid-Sid-H2) + other(R) + group(Sid-Sid-H2) + other(R) + group(si-Sid-H) + other(R)"""),
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
    E0 = (670.032,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([300,800,800,800,800,800,800,1600,1600,1600,1600,1600,1600,1600],'cm^-1')),
        HinderedRotor(inertia=(0.156089,'amu*angstrom^2'), symmetry=1, barrier=(3.5888,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 1,
    opticalIsomers = 1,
    molecularWeight = (88.2883,'amu'),
    collisionModel = TransportData(shapeIndex=2, epsilon=(1971.36,'J/mol'), sigma=(5.118e-10,'m'), dipoleMoment=(0,'C*m'), polarizability=(0,'angstroms^3'), rotrelaxcollnum=0, comment="""Epsilon & sigma estimated with fixed Lennard Jones Parameters. This is the fallback method! Try improving transport databases!"""),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[1.14459,0.0701591,-0.000122,1.07823e-07,-3.64259e-11,80682,31.4606], Tmin=(100,'K'), Tmax=(868.307,'K')), NASAPolynomial(coeffs=[8.55796,0.0207852,-1.04091e-05,1.95481e-09,-1.31466e-13,79968.5,0.0467376], Tmin=(868.307,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(670.032,'kJ/mol'), comment="""Thermo group additivity estimation: group(Sis-H3Si) + other(R) + group(Sid-sid-H-Si) + other(R) + group(si-Sid-H) + other(R)"""),
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
    label = '[SiH2][Si][SiH3](35)',
    structure = SMILES('[SiH2][Si][SiH3]'),
    E0 = (415.339,'kJ/mol'),
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
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[1.74464,0.0543943,-8.76091e-05,7.52807e-08,-2.52341e-11,50030.4,17.2945], Tmin=(100,'K'), Tmax=(849.541,'K')), NASAPolynomial(coeffs=[7.63956,0.0181739,-8.71045e-06,1.63745e-09,-1.11186e-13,49334.2,-8.38613], Tmin=(849.541,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(415.339,'kJ/mol'), comment="""Thermo group additivity estimation: group(Sis-H3Si) + other(R) + group(Sis-H3Si) + other(R) + group(si-Sis2) + other(R) + radical(SisJ_SiLP)"""),
)

species(
    label = '[SiH][Si][SiH3](36)',
    structure = SMILES('[SiH][Si][SiH3]'),
    E0 = (492.073,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([300,800,800,800,800,800,800,1600,1600,1600,1600,1600,1600],'cm^-1')),
        HinderedRotor(inertia=(0.156089,'amu*angstrom^2'), symmetry=1, barrier=(3.5888,'kJ/mol'), semiclassical=False),
        HinderedRotor(inertia=(0.156089,'amu*angstrom^2'), symmetry=1, barrier=(3.5888,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 1,
    opticalIsomers = 1,
    molecularWeight = (88.2883,'amu'),
    collisionModel = TransportData(shapeIndex=2, epsilon=(1971.36,'J/mol'), sigma=(5.118e-10,'m'), dipoleMoment=(0,'C*m'), polarizability=(0,'angstroms^3'), rotrelaxcollnum=0, comment="""Epsilon & sigma estimated with fixed Lennard Jones Parameters. This is the fallback method! Try improving transport databases!"""),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[2.06018,0.0466724,-7.53321e-05,6.46185e-08,-2.17084e-11,59248.7,17.9213], Tmin=(100,'K'), Tmax=(836.449,'K')), NASAPolynomial(coeffs=[7.30802,0.0152034,-7.46976e-06,1.42172e-09,-9.73533e-14,58593.8,-5.12653], Tmin=(836.449,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(492.073,'kJ/mol'), comment="""Thermo group additivity estimation: group(Sis-H3Si) + other(R) + group(si-Sis-si) + other(R) + group(si-Sis-H) + other(R)"""),
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
    label = '[SiH][SiH][SiH3](43)',
    structure = SMILES('[SiH][SiH][SiH3]'),
    E0 = (425.138,'kJ/mol'),
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
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[1.66273,0.0563423,-9.18178e-05,7.87681e-08,-2.62581e-11,51211.8,18.1577], Tmin=(100,'K'), Tmax=(853.86,'K')), NASAPolynomial(coeffs=[8.00073,0.0177952,-8.54325e-06,1.603e-09,-1.08567e-13,50452.3,-9.52769], Tmin=(853.86,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(425.138,'kJ/mol'), comment="""Thermo group additivity estimation: group(Sis-H2Si2) + other(R) + group(Sis-H3Si) + other(R) + group(si-Sis-H) + other(R) + radical(SisJ_SiLP)"""),
)

species(
    label = '[SiH][SiH2][SiH2](44)',
    structure = SMILES('[SiH][SiH2][SiH2]'),
    E0 = (485.134,'kJ/mol'),
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
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[1.63783,0.0565453,-9.10234e-05,7.71114e-08,-2.55096e-11,58428.8,19.0854], Tmin=(100,'K'), Tmax=(844.963,'K')), NASAPolynomial(coeffs=[8.35925,0.0173568,-8.37196e-06,1.57805e-09,-1.07339e-13,57556,-10.6525], Tmin=(844.963,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(485.134,'kJ/mol'), comment="""Thermo group additivity estimation: group(Sis-H2Si2) + other(R) + group(Sis-H3Si) + other(R) + group(si-Sis-H) + other(R) + radical(SisJ_Si_H2)"""),
)

species(
    label = '[Si][SiH2][SiH3](45)',
    structure = SMILES('[Si][SiH2][SiH3]'),
    E0 = (429.318,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([300,800,800,800,800,800,800,800,800,1600,1600,1600,1600,1600,1600,1600,1600],'cm^-1')),
        HinderedRotor(inertia=(0.156089,'amu*angstrom^2'), symmetry=1, barrier=(3.5888,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 1,
    molecularWeight = (89.2962,'amu'),
    collisionModel = TransportData(shapeIndex=2, epsilon=(1971.36,'J/mol'), sigma=(5.118e-10,'m'), dipoleMoment=(0,'C*m'), polarizability=(0,'angstroms^3'), rotrelaxcollnum=0, comment="""Epsilon & sigma estimated with fixed Lennard Jones Parameters. This is the fallback method! Try improving transport databases!"""),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[2.37736,0.0379186,-4.22783e-05,2.6302e-08,-6.78758e-12,51691.6,14.92], Tmin=(100,'K'), Tmax=(927.841,'K')), NASAPolynomial(coeffs=[7.3289,0.016572,-7.76833e-06,1.50616e-09,-1.06523e-13,50772.7,-8.5975], Tmin=(927.841,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(429.318,'kJ/mol'), comment="""Thermo group additivity estimation: group(Sis-H2Si2) + other(R) + group(Sis-H3Si) + other(R) + group(si-Sis-H) + other(R) + radical(SiJ_LP_Si)"""),
)

species(
    label = '[SiH][SiH2][SiH](46)',
    structure = SMILES('[SiH][SiH2][SiH]'),
    E0 = (552.384,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([300,800,800,800,800,800,800,1600,1600,1600,1600,1600,1600],'cm^-1')),
        HinderedRotor(inertia=(0.156089,'amu*angstrom^2'), symmetry=1, barrier=(3.5888,'kJ/mol'), semiclassical=False),
        HinderedRotor(inertia=(0.156089,'amu*angstrom^2'), symmetry=1, barrier=(3.5888,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 1,
    opticalIsomers = 1,
    molecularWeight = (88.2883,'amu'),
    collisionModel = TransportData(shapeIndex=2, epsilon=(1971.36,'J/mol'), sigma=(5.118e-10,'m'), dipoleMoment=(0,'C*m'), polarizability=(0,'angstroms^3'), rotrelaxcollnum=0, comment="""Epsilon & sigma estimated with fixed Lennard Jones Parameters. This is the fallback method! Try improving transport databases!"""),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[1.84753,0.0530771,-9.31168e-05,8.30218e-08,-2.82744e-11,66508.5,17.958], Tmin=(100,'K'), Tmax=(862.466,'K')), NASAPolynomial(coeffs=[7.38019,0.0157584,-7.93481e-06,1.50415e-09,-1.01858e-13,65987.7,-5.40145], Tmin=(862.466,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(552.384,'kJ/mol'), comment="""Thermo group additivity estimation: group(Sis-H2Si2) + other(R) + group(si-Sis-H) + other(R) + group(si-Sis-H) + other(R)"""),
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
    collisionModel = TransportData(shapeIndex=0, epsilon=(1235.53,'J/mol'), sigma=(3.758e-10,'m'), dipoleMoment=(0,'C*m'), polarizability=(0,'angstroms^3'), rotrelaxcollnum=0, comment="""Epsilon & sigma estimated with fixed Lennard Jones Parameters. This is the fallback method! Try improving transport databases!"""),
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
    collisionModel = TransportData(shapeIndex=0, epsilon=(1235.53,'J/mol'), sigma=(3.758e-10,'m'), dipoleMoment=(0,'C*m'), polarizability=(0,'angstroms^3'), rotrelaxcollnum=0, comment="""Epsilon & sigma estimated with fixed Lennard Jones Parameters. This is the fallback method! Try improving transport databases!"""),
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
    E0 = (369.793,'kJ/mol'),
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
    E0 = (651.68,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS4',
    E0 = (623.707,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS5',
    E0 = (623.707,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS6',
    E0 = (338.46,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS7',
    E0 = (362.485,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS8',
    E0 = (486.739,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS9',
    E0 = (661.428,'kJ/mol'),
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
    E0 = (627.144,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS13',
    E0 = (486.817,'kJ/mol'),
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
    E0 = (636.943,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS17',
    E0 = (696.939,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS18',
    E0 = (641.123,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS19',
    E0 = (483.47,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS20',
    E0 = (547.128,'kJ/mol'),
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
    reactants = ['[H](16)', '[SiH2][SiH]=[SiH2](28)'],
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
    reactants = ['[SiH][SiH]=[SiH2](33)', 'H2(7)'],
    products = ['[SiH2]=[SiH][SiH3](25)'],
    transitionState = 'TS8',
    kinetics = Arrhenius(A=(7.6e+12,'cm^3/(mol*s)'), n=0, Ea=(3.3472,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Exact match found for rate rule (Si-Si-H;H_H)
Multiplied by reaction path degeneracy 2"""),
)

reaction(
    label = 'reaction9',
    reactants = ['[Si]=[SiH][SiH3](29)', 'H2(7)'],
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
    reactants = ['[H](16)', '[SiH2][Si][SiH3](35)'],
    products = ['[SiH3][Si][SiH3](32)'],
    transitionState = 'TS12',
    kinetics = Arrhenius(A=(7.20571e+06,'m^3/(mol*s)'), n=0.100587, Ea=(0,'kJ/mol'), T0=(1,'K'), comment="""Estimated using template (Y_rad;Y_rad) for rate rule (Si_rad;H_rad)
Ea raised from -0.8 to 0 kJ/mol."""),
)

reaction(
    label = 'reaction13',
    reactants = ['[SiH][Si][SiH3](36)', 'H2(7)'],
    products = ['[SiH3][Si][SiH3](32)'],
    transitionState = 'TS13',
    kinetics = Arrhenius(A=(7.6e+12,'cm^3/(mol*s)'), n=0, Ea=(3.3472,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Exact match found for rate rule (Si-Si-H;H_H)
Multiplied by reaction path degeneracy 2"""),
)

reaction(
    label = 'reaction2',
    reactants = ['SiH3(3)', '[SiH][SiH2](18)'],
    products = ['[SiH][SiH2][SiH3](23)'],
    transitionState = 'TS14',
    kinetics = Arrhenius(A=(7.20571e+06,'m^3/(mol*s)'), n=0.100587, Ea=(0,'kJ/mol'), T0=(1,'K'), comment="""Estimated using template (Y_rad;Y_rad) for rate rule (Si_rad;Si_silyl)
Ea raised from -0.8 to 0 kJ/mol."""),
)

reaction(
    label = 'reaction3',
    reactants = ['Si2H5(4)', 'SiH(11)'],
    products = ['[SiH][SiH2][SiH3](23)'],
    transitionState = 'TS15',
    kinetics = Arrhenius(A=(7.20571e+06,'m^3/(mol*s)'), n=0.100587, Ea=(0,'kJ/mol'), T0=(1,'K'), comment="""Estimated using template (Y_rad;Y_rad) for rate rule (Si_rad;Si_rad)
Ea raised from -0.8 to 0 kJ/mol."""),
)

reaction(
    label = 'reaction4',
    reactants = ['[H](16)', '[SiH][SiH][SiH3](43)'],
    products = ['[SiH][SiH2][SiH3](23)'],
    transitionState = 'TS16',
    kinetics = Arrhenius(A=(7.20571e+06,'m^3/(mol*s)'), n=0.100587, Ea=(0,'kJ/mol'), T0=(1,'K'), comment="""Estimated using template (Y_rad;Y_rad) for rate rule (Si_rad;H_rad)
Ea raised from -0.8 to 0 kJ/mol."""),
)

reaction(
    label = 'reaction5',
    reactants = ['[H](16)', '[SiH][SiH2][SiH2](44)'],
    products = ['[SiH][SiH2][SiH3](23)'],
    transitionState = 'TS17',
    kinetics = Arrhenius(A=(7.20571e+06,'m^3/(mol*s)'), n=0.100587, Ea=(0,'kJ/mol'), T0=(1,'K'), comment="""Estimated using template (Y_rad;Y_rad) for rate rule (Si_rad;H_rad)
Ea raised from -0.8 to 0 kJ/mol."""),
)

reaction(
    label = 'reaction6',
    reactants = ['[H](16)', '[Si][SiH2][SiH3](45)'],
    products = ['[SiH][SiH2][SiH3](23)'],
    transitionState = 'TS18',
    kinetics = Arrhenius(A=(7.20571e+06,'m^3/(mol*s)'), n=0.100587, Ea=(0,'kJ/mol'), T0=(1,'K'), comment="""Estimated using template (Y_rad;Y_rad) for rate rule (H_rad;Si_rad)
Ea raised from -0.8 to 0 kJ/mol."""),
)

reaction(
    label = 'reaction8',
    reactants = ['[SiH][Si][SiH3](36)', 'H2(7)'],
    products = ['[SiH][SiH2][SiH3](23)'],
    transitionState = 'TS19',
    kinetics = Arrhenius(A=(2.4e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Exact match found for rate rule (Si-Si-Si;H_H)
Multiplied by reaction path degeneracy 2
Ea raised from -2.1 to 0 kJ/mol."""),
)

reaction(
    label = 'reaction9',
    reactants = ['[SiH][SiH2][SiH](46)', 'H2(7)'],
    products = ['[SiH][SiH2][SiH3](23)'],
    transitionState = 'TS20',
    kinetics = Arrhenius(A=(1.52e+13,'cm^3/(mol*s)'), n=0, Ea=(3.3472,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Exact match found for rate rule (Si-Si-H;H_H)
Multiplied by reaction path degeneracy 4"""),
)

reaction(
    label = 'reaction10',
    reactants = ['SiH4(1)', 'Si2H2(15)'],
    products = ['[SiH][SiH2][SiH3](23)'],
    transitionState = 'TS21',
    kinetics = Arrhenius(A=(4.8e+10,'cm^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Exact match found for rate rule (Si-Si-H;SiH4)
Multiplied by reaction path degeneracy 8
Ea raised from -38.1 to 0 kJ/mol."""),
)

reaction(
    label = 'reaction1',
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
        ('SiH2(5)', 'SiH2SiH2(9)'),
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

