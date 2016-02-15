species(
    label = '[SiH2][SiH2](79)',
    structure = SMILES('[SiH2][SiH2]'),
    E0 = (364.025,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([300,800,800,800,800,800,1600,1600,1600,1600,1600],'cm^-1')),
        HinderedRotor(inertia=(0.156089,'amu*angstrom^2'), symmetry=1, barrier=(3.5888,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 3,
    opticalIsomers = 1,
    molecularWeight = (60.2028,'amu'),
    collisionModel = TransportData(shapeIndex=2, epsilon=(920.412,'J/mol'), sigma=(4.443e-10,'m'), dipoleMoment=(0,'C*m'), polarizability=(0,'angstroms^3'), rotrelaxcollnum=0, comment="""Epsilon & sigma estimated with fixed Lennard Jones Parameters. This is the fallback method! Try improving transport databases!"""),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[2.80413,0.0266235,-2.85659e-05,1.61455e-08,-3.65347e-12,43824.9,11.7758], Tmin=(100,'K'), Tmax=(1069.62,'K')), NASAPolynomial(coeffs=[7.51796,0.00899559,-3.84543e-06,7.38017e-10,-5.23616e-14,42816.5,-11.2831], Tmin=(1069.62,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(364.025,'kJ/mol'), comment="""Thermo library: SiliconHydrideLibrary + radical(SisJ_Si_H2) + radical(SisJ_Si_H2)"""),
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
    label = '[SiH2][SiH2](80)',
    structure = SMILES('[SiH2][SiH2]'),
    E0 = (485.451,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([180,637.188,1235.37,1235.45,4000,4000],'cm^-1')),
    ],
    spinMultiplicity = 3,
    opticalIsomers = 1,
    molecularWeight = (58.1869,'amu'),
    collisionModel = TransportData(shapeIndex=2, epsilon=(920.412,'J/mol'), sigma=(4.443e-10,'m'), dipoleMoment=(0,'C*m'), polarizability=(0,'angstroms^3'), rotrelaxcollnum=0, comment="""Epsilon & sigma estimated with fixed Lennard Jones Parameters. This is the fallback method! Try improving transport databases!"""),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[3.64643,0.00832612,-6.60092e-06,2.86939e-09,-5.20415e-13,58398.5,9.66432], Tmin=(100,'K'), Tmax=(1267.63,'K')), NASAPolynomial(coeffs=[4.92228,0.00430021,-1.83705e-06,3.64014e-10,-2.63104e-14,58075.1,3.20651], Tmin=(1267.63,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(485.451,'kJ/mol'), comment="""Thermo library: SiliconHydrideLibrary + radical(SisJ_SiLP) + radical(SiJ_LP_Si)"""),
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
    E0 = (549.361,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS2',
    E0 = (476.848,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

reaction(
    label = 'reaction1',
    reactants = ['SiH3(9)', 'SiH(10)'],
    products = ['[SiH2][SiH2](79)'],
    transitionState = 'TS1',
    kinetics = Arrhenius(A=(5.58e+14,'cm^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), Tmin=(295,'K'), Tmax=(595,'K'), comment="""Exact match found for rate rule (Si2S;Si_H)
Multiplied by reaction path degeneracy 3
Ea raised from -1.9 to 0 kJ/mol."""),
)

reaction(
    label = 'reaction2',
    reactants = ['H2(3)', '[SiH2][SiH2](80)'],
    products = ['[SiH2][SiH2](79)'],
    transitionState = 'TS2',
    kinetics = Arrhenius(A=(2.1e+06,'cm^3/(mol*s)'), n=1.97, Ea=(0,'kJ/mol'), T0=(1,'K'), Tmin=(400,'K'), Tmax=(2000,'K'), comment="""Exact match found for rate rule (Si2S;H_H)
Multiplied by reaction path degeneracy 2
Ea raised from -1.9 to 0 kJ/mol."""),
)

network(
    label = '68',
    isomers = [
        '[SiH2][SiH2](79)',
    ],
    reactants = [
        ('SiH3(9)', 'SiH(10)'),
    ],
    bathGas = {
        'He': 0.25,
        'Ar': 0.25,
        'Ne': 0.25,
        'N2': 0.25,
    },
)

pressureDependence(
    label = '68',
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

