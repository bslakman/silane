species(
    label = 'SiH2Si(16)',
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
    label = 'Si2H2(19)',
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
    label = 'H2(11)',
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
    label = '[Si]=[Si](28)',
    structure = SMILES('[Si]=[Si]'),
    E0 = (449.207,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([180],'cm^-1')),
    ],
    spinMultiplicity = 1,
    opticalIsomers = 1,
    molecularWeight = (56.171,'amu'),
    collisionModel = TransportData(shapeIndex=1, epsilon=(920.412,'J/mol'), sigma=(4.443e-10,'m'), dipoleMoment=(0,'C*m'), polarizability=(0,'angstroms^3'), rotrelaxcollnum=0, comment="""Epsilon & sigma estimated with fixed Lennard Jones Parameters. This is the fallback method! Try improving transport databases!"""),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[2.66451,0.0198424,-3.08668e-05,2.55142e-08,-8.28952e-12,54055.9,10.7967], Tmin=(100,'K'), Tmax=(862.239,'K')), NASAPolynomial(coeffs=[4.96224,0.00655922,-3.19418e-06,5.89064e-10,-3.93962e-14,53757.2,0.617609], Tmin=(862.239,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(449.207,'kJ/mol'), comment="""Thermo group additivity estimation: group(si-Sid-H) + other(R) + group(si-Sid-H) + other(R)"""),
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

transitionState(
    label = 'TS1',
    E0 = (446.928,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS2',
    E0 = (440.604,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

reaction(
    label = 'reaction1',
    reactants = ['Si2H2(19)'],
    products = ['SiH2Si(16)'],
    transitionState = 'TS1',
    kinetics = Arrhenius(A=(1.58e+13,'cm^3/(mol*s)'), n=0, Ea=(5.3095,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1600,'K'), comment="""Estimated using template (SiRSiH) for rate rule (SiHSiH)
Multiplied by reaction path degeneracy 2"""),
)

reaction(
    label = 'reaction2',
    reactants = ['H2(11)', '[Si]=[Si](28)'],
    products = ['SiH2Si(16)'],
    transitionState = 'TS2',
    kinetics = Arrhenius(A=(4.2e+06,'cm^3/(mol*s)'), n=1.97, Ea=(0,'kJ/mol'), T0=(1,'K'), Tmin=(400,'K'), Tmax=(2000,'K'), comment="""Exact match found for rate rule (Si2S;H_H)
Multiplied by reaction path degeneracy 4
Ea raised from -1.9 to 0 kJ/mol."""),
)

network(
    label = '34',
    isomers = [
        'SiH2Si(16)',
        'Si2H2(19)',
    ],
    reactants = [
        ('H2(11)', '[Si]=[Si](28)'),
    ],
    bathGas = {
        'Ar': 0.25,
        'He': 0.25,
        'N2': 0.25,
        'Ne': 0.25,
    },
)

pressureDependence(
    label = '34',
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

