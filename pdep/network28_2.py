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
    label = '[Si][Si][SiH3](41)',
    structure = SMILES('[Si][Si][SiH3]'),
    E0 = (681.409,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([497.516,1013.56,1013.56,1013.56,1013.56,1013.56,1013.56,1013.56,1013.56,1013.56,2309.09],'cm^-1')),
        HinderedRotor(inertia=(0.00975557,'amu*angstrom^2'), symmetry=1, barrier=(0.2243,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 1,
    molecularWeight = (87.2803,'amu'),
    collisionModel = TransportData(shapeIndex=2, epsilon=(1971.36,'J/mol'), sigma=(5.118e-10,'m'), dipoleMoment=(0,'C*m'), polarizability=(0,'angstroms^3'), rotrelaxcollnum=0, comment="""Epsilon & sigma estimated with fixed Lennard Jones Parameters. This is the fallback method! Try improving transport databases!"""),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[1.82748,0.0534845,-9.10011e-05,8.10316e-08,-2.78025e-11,82027.3,32.308], Tmin=(100,'K'), Tmax=(857.303,'K')), NASAPolynomial(coeffs=[6.93168,0.0181788,-9.12317e-06,1.72659e-09,-1.17125e-13,81574.4,10.9317], Tmin=(857.303,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(681.409,'kJ/mol'), comment="""Thermo group additivity estimation: group(Sis-H3si) + other(R) + group(si) + other(R) + group(si) + other(R) + radical(SiJ_LP_H)"""),
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
    label = '[Si]=[Si](27)',
    structure = SMILES('[Si]=[Si]'),
    E0 = (538.524,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([180],'cm^-1')),
    ],
    spinMultiplicity = 1,
    opticalIsomers = 1,
    molecularWeight = (56.171,'amu'),
    collisionModel = TransportData(shapeIndex=1, epsilon=(920.412,'J/mol'), sigma=(4.443e-10,'m'), dipoleMoment=(0,'C*m'), polarizability=(0,'angstroms^3'), rotrelaxcollnum=0, comment="""Epsilon & sigma estimated with fixed Lennard Jones Parameters. This is the fallback method! Try improving transport databases!"""),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[2.24271,0.0322964,-5.7166e-05,5.37632e-08,-1.91752e-11,64810.4,29.6413], Tmin=(100,'K'), Tmax=(872.989,'K')), NASAPolynomial(coeffs=[3.8681,0.0140129,-7.13195e-06,1.33583e-09,-8.96591e-14,64939.5,24.3854], Tmin=(872.989,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(538.524,'kJ/mol'), comment="""Thermo group additivity estimation: group(si) + other(R) + group(si) + other(R)"""),
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
    label = '[Si][SiH]=[SiH](38)',
    structure = SMILES('[Si][SiH]=[SiH]'),
    E0 = (644.01,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([210.099,210.184,210.215,210.29,210.299,210.325,1573.33,1573.33,1573.39],'cm^-1')),
    ],
    spinMultiplicity = 3,
    opticalIsomers = 1,
    molecularWeight = (86.2724,'amu'),
    collisionModel = TransportData(shapeIndex=2, epsilon=(1971.36,'J/mol'), sigma=(5.118e-10,'m'), dipoleMoment=(0,'C*m'), polarizability=(0,'angstroms^3'), rotrelaxcollnum=0, comment="""Epsilon & sigma estimated with fixed Lennard Jones Parameters. This is the fallback method! Try improving transport databases!"""),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[2.31204,0.0458164,-9.81051e-05,9.60342e-08,-3.40968e-11,77509.1,6.01214], Tmin=(100,'K'), Tmax=(891.106,'K')), NASAPolynomial(coeffs=[5.00589,0.0126815,-6.90796e-06,1.30682e-09,-8.64864e-14,77864.4,-1.98575], Tmin=(891.106,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(644.01,'kJ/mol'), comment="""Thermo group additivity estimation: group(Sis-Sis4) + other(R) + group(Sid-H2) + other(R) + group(si) + other(R) + radical(SiJ_LP_Si) + radical(SidsJ_Si)"""),
)

species(
    label = '[Si][Si]=[SiH2](39)',
    structure = SMILES('[Si][Si]=[SiH2]'),
    E0 = (644.01,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([210.099,210.184,210.215,210.29,210.299,210.325,1573.33,1573.33,1573.39],'cm^-1')),
    ],
    spinMultiplicity = 3,
    opticalIsomers = 1,
    molecularWeight = (86.2724,'amu'),
    collisionModel = TransportData(shapeIndex=2, epsilon=(1971.36,'J/mol'), sigma=(5.118e-10,'m'), dipoleMoment=(0,'C*m'), polarizability=(0,'angstroms^3'), rotrelaxcollnum=0, comment="""Epsilon & sigma estimated with fixed Lennard Jones Parameters. This is the fallback method! Try improving transport databases!"""),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[2.31204,0.0458164,-9.81051e-05,9.60342e-08,-3.40968e-11,77509.1,6.01214], Tmin=(100,'K'), Tmax=(891.106,'K')), NASAPolynomial(coeffs=[5.00589,0.0126815,-6.90796e-06,1.30682e-09,-8.64864e-14,77864.4,-1.98575], Tmin=(891.106,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(644.01,'kJ/mol'), comment="""Thermo group additivity estimation: group(Sis-Sis4) + other(R) + group(Sid-H2) + other(R) + group(si) + other(R) + radical(SidsJ_Si) + radical(SiJ_LP_Si)"""),
)

species(
    label = '[Si][SiH2][SiH](40)',
    structure = SMILES('[Si][SiH2][SiH]'),
    E0 = (675.697,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([510.135,1009.58,1009.58,1009.58,1009.58,1009.58,1009.58,1009.58,1009.58,1009.58,2314.82],'cm^-1')),
        HinderedRotor(inertia=(0.00975557,'amu*angstrom^2'), symmetry=1, barrier=(0.2243,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 1,
    molecularWeight = (87.2803,'amu'),
    collisionModel = TransportData(shapeIndex=2, epsilon=(1971.36,'J/mol'), sigma=(5.118e-10,'m'), dipoleMoment=(0,'C*m'), polarizability=(0,'angstroms^3'), rotrelaxcollnum=0, comment="""Epsilon & sigma estimated with fixed Lennard Jones Parameters. This is the fallback method! Try improving transport databases!"""),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[2.33133,0.0409182,-6.47078e-05,5.78406e-08,-2.04308e-11,81323.6,32.8434], Tmin=(100,'K'), Tmax=(828.937,'K')), NASAPolynomial(coeffs=[5.53932,0.0177373,-8.82559e-06,1.6905e-09,-1.16412e-13,81056.3,19.5645], Tmin=(828.937,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(675.697,'kJ/mol'), comment="""Thermo group additivity estimation: group(Sis-H3si) + other(R) + group(si) + other(R) + group(si) + other(R) + radical(SiJ_LP_Si)"""),
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
    label = '[Si][SiH]=[Si](42)',
    structure = SMILES('[Si][SiH]=[Si]'),
    E0 = (651.852,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([180,180,180,180,180,180],'cm^-1')),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 1,
    molecularWeight = (85.2644,'amu'),
    collisionModel = TransportData(shapeIndex=2, epsilon=(1971.36,'J/mol'), sigma=(5.118e-10,'m'), dipoleMoment=(0,'C*m'), polarizability=(0,'angstroms^3'), rotrelaxcollnum=0, comment="""Epsilon & sigma estimated with fixed Lennard Jones Parameters. This is the fallback method! Try improving transport databases!"""),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[2.25348,0.0448642,-8.61068e-05,8.01908e-08,-2.7803e-11,78456.4,13.3537], Tmin=(100,'K'), Tmax=(885.017,'K')), NASAPolynomial(coeffs=[5.93548,0.0131695,-6.87452e-06,1.28784e-09,-8.55603e-14,78394.2,-0.629486], Tmin=(885.017,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(651.852,'kJ/mol'), comment="""Thermo group additivity estimation: group(Sis-Sis4) + other(R) + group(si) + other(R) + group(si) + other(R) + radical(SiJ_LP_Si)"""),
)

species(
    label = '[SiH][Si][SiH2](43)',
    structure = SMILES('[SiH][Si][SiH2]'),
    E0 = (671.517,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([200,800,900,1000,1100,1200,1300,1400,1500,1600],'cm^-1')),
        HinderedRotor(inertia=(0.156089,'amu*angstrom^2'), symmetry=1, barrier=(3.5888,'kJ/mol'), semiclassical=False),
        HinderedRotor(inertia=(0.156089,'amu*angstrom^2'), symmetry=1, barrier=(3.5888,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 1,
    molecularWeight = (87.2803,'amu'),
    collisionModel = TransportData(shapeIndex=2, epsilon=(1971.36,'J/mol'), sigma=(5.118e-10,'m'), dipoleMoment=(0,'C*m'), polarizability=(0,'angstroms^3'), rotrelaxcollnum=0, comment="""Epsilon & sigma estimated with fixed Lennard Jones Parameters. This is the fallback method! Try improving transport databases!"""),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[1.75653,0.05757,-0.000107414,1.00391e-07,-3.51251e-11,80837.8,34.8941], Tmin=(100,'K'), Tmax=(879.444,'K')), NASAPolynomial(coeffs=[5.97178,0.0193833,-9.8509e-06,1.84761e-09,-1.23525e-13,80831.7,19.28], Tmin=(879.444,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(671.517,'kJ/mol'), comment="""Thermo group additivity estimation: group(Sis-H3si) + other(R) + group(si) + other(R) + group(si) + other(R) + radical(SisJ_SiLP)"""),
)

species(
    label = '[Si][Si](51)',
    structure = SMILES('[Si][Si]'),
    E0 = (654.483,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([180],'cm^-1')),
    ],
    spinMultiplicity = 3,
    opticalIsomers = 1,
    molecularWeight = (56.171,'amu'),
    collisionModel = TransportData(shapeIndex=1, epsilon=(920.412,'J/mol'), sigma=(4.443e-10,'m'), dipoleMoment=(0,'C*m'), polarizability=(0,'angstroms^3'), rotrelaxcollnum=0, comment="""Epsilon & sigma estimated with fixed Lennard Jones Parameters. This is the fallback method! Try improving transport databases!"""),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[3.43358,0.0140106,-3.06941e-05,2.62383e-08,-7.90427e-12,78735.2,4.27073], Tmin=(100,'K'), Tmax=(1002.37,'K')), NASAPolynomial(coeffs=[6.13162,-0.00204604,1.25018e-06,-2.72636e-10,2.09572e-14,78460.1,-7.42648], Tmin=(1002.37,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(654.483,'kJ/mol'), comment="""Thermo library: SiliconHydrideLibrary + radical(SiJ_LP_H) + radical(SiJ_LP_H)"""),
)

species(
    label = '[Si][Si][SiH2](52)',
    structure = SMILES('[Si][Si][SiH2]'),
    E0 = (777.953,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([180,180,180,180,180,180,180,180],'cm^-1')),
        HinderedRotor(inertia=(2.18259,'amu*angstrom^2'), symmetry=1, barrier=(50.1821,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 3,
    opticalIsomers = 1,
    molecularWeight = (86.2724,'amu'),
    collisionModel = TransportData(shapeIndex=2, epsilon=(1971.36,'J/mol'), sigma=(5.118e-10,'m'), dipoleMoment=(0,'C*m'), polarizability=(0,'angstroms^3'), rotrelaxcollnum=0, comment="""Epsilon & sigma estimated with fixed Lennard Jones Parameters. This is the fallback method! Try improving transport databases!"""),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[1.90217,0.0540976,-0.00010426,9.72279e-08,-3.36295e-11,93634.1,32.5082], Tmin=(100,'K'), Tmax=(890.966,'K')), NASAPolynomial(coeffs=[6.21858,0.0158487,-8.0959e-06,1.50132e-09,-9.89467e-14,93613.9,16.3855], Tmin=(890.966,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(777.953,'kJ/mol'), comment="""Thermo group additivity estimation: group(Sis-H3si) + other(R) + group(si) + other(R) + group(si) + other(R) + radical(SiJ_LP_H) + radical(SisJ_SiLP)"""),
)

species(
    label = '[Si][Si][SiH](53)',
    structure = SMILES('[Si][Si][SiH]'),
    E0 = (915.561,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([180,180,180,180,180],'cm^-1')),
        HinderedRotor(inertia=(2.04863,'amu*angstrom^2'), symmetry=1, barrier=(47.1021,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 1,
    molecularWeight = (85.2644,'amu'),
    collisionModel = TransportData(shapeIndex=2, epsilon=(1971.36,'J/mol'), sigma=(5.118e-10,'m'), dipoleMoment=(0,'C*m'), polarizability=(0,'angstroms^3'), rotrelaxcollnum=0, comment="""Epsilon & sigma estimated with fixed Lennard Jones Parameters. This is the fallback method! Try improving transport databases!"""),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[1.84702,0.0568225,-0.000111818,1.07337e-07,-3.80654e-11,110185,50.1124], Tmin=(100,'K'), Tmax=(885.327,'K')), NASAPolynomial(coeffs=[5.07462,0.0195599,-1.02584e-05,1.92452e-09,-1.28034e-13,110502,39.954], Tmin=(885.327,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(915.561,'kJ/mol'), comment="""Thermo group additivity estimation: group(si) + other(R) + group(si) + other(R) + group(si) + other(R) + radical(SiJ_LP_H)"""),
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
    E0 = (720.076,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS2',
    E0 = (855.815,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS3',
    E0 = (855.815,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS4',
    E0 = (709.587,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS5',
    E0 = (701.074,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS6',
    E0 = (643.248,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS7',
    E0 = (676.827,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS8',
    E0 = (769.388,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS9',
    E0 = (836.035,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS10',
    E0 = (989.757,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS11',
    E0 = (910.305,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

reaction(
    label = 'reaction1',
    reactants = ['SiH3(3)', '[Si]=[Si](27)'],
    products = ['[Si]=[SiH][SiH2](34)'],
    transitionState = 'TS1',
    kinetics = Arrhenius(A=(1.116e+15,'cm^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), Tmin=(295,'K'), Tmax=(595,'K'), comment="""Exact match found for rate rule (Si2S;Si_H)
Multiplied by reaction path degeneracy 6
Ea raised from -1.9 to 0 kJ/mol."""),
)

reaction(
    label = 'reaction2',
    reactants = ['[H](16)', '[Si][SiH]=[SiH](38)'],
    products = ['[Si]=[SiH][SiH2](34)'],
    transitionState = 'TS2',
    kinetics = Arrhenius(A=(7.20571e+06,'m^3/(mol*s)'), n=0.100587, Ea=(0,'kJ/mol'), T0=(1,'K'), comment="""Estimated using template (Y_rad;Y_rad) for rate rule (Si_rad;H_rad)
Ea raised from -0.8 to 0 kJ/mol."""),
)

reaction(
    label = 'reaction3',
    reactants = ['[H](16)', '[Si][Si]=[SiH2](39)'],
    products = ['[Si]=[SiH][SiH2](34)'],
    transitionState = 'TS3',
    kinetics = Arrhenius(A=(7.20571e+06,'m^3/(mol*s)'), n=0.100587, Ea=(0,'kJ/mol'), T0=(1,'K'), comment="""Estimated using template (Y_rad;Y_rad) for rate rule (Si_rad;H_rad)
Ea raised from -0.8 to 0 kJ/mol."""),
)

reaction(
    label = 'reaction4',
    reactants = ['[Si][SiH2][SiH](40)'],
    products = ['[Si]=[SiH][SiH2](34)'],
    transitionState = 'TS4',
    kinetics = Arrhenius(A=(2e+12,'1/s'), n=0, Ea=(33.8904,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Exact match found for rate rule (SiHSiH2)
Multiplied by reaction path degeneracy 2"""),
)

reaction(
    label = 'reaction5',
    reactants = ['[Si][Si][SiH3](41)'],
    products = ['[Si]=[SiH][SiH2](34)'],
    transitionState = 'TS5',
    kinetics = Arrhenius(A=(2.505e+12,'1/s'), n=0, Ea=(19.6648,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Exact match found for rate rule (SiSiSiH3)
Multiplied by reaction path degeneracy 3"""),
)

reaction(
    label = 'reaction6',
    reactants = ['H2(7)', '[Si][SiH]=[Si](42)'],
    products = ['[Si]=[SiH][SiH2](34)'],
    transitionState = 'TS6',
    kinetics = Arrhenius(A=(4.2e+06,'cm^3/(mol*s)'), n=1.97, Ea=(0,'kJ/mol'), T0=(1,'K'), Tmin=(400,'K'), Tmax=(2000,'K'), comment="""Exact match found for rate rule (Si2S;H_H)
Multiplied by reaction path degeneracy 4
Ea raised from -1.9 to 0 kJ/mol."""),
)

reaction(
    label = 'reaction7',
    reactants = ['[SiH][Si][SiH2](43)'],
    products = ['[Si]=[SiH][SiH2](34)'],
    transitionState = 'TS7',
    kinetics = Arrhenius(A=(7.9e+12,'cm^3/(mol*s)'), n=0, Ea=(5.3095,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1600,'K'), comment="""Estimated using template (SiRSiH) for rate rule (SiSiSiH)"""),
)

reaction(
    label = 'reaction8',
    reactants = ['SiH(11)', 'SiH2Si(12)'],
    products = ['[Si]=[SiH][SiH2](34)'],
    transitionState = 'TS8',
    kinetics = Arrhenius(A=(3.72e+14,'cm^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), Tmin=(295,'K'), Tmax=(595,'K'), comment="""Exact match found for rate rule (Si2S;Si_H)
Multiplied by reaction path degeneracy 2
Ea raised from -1.9 to 0 kJ/mol."""),
)

reaction(
    label = 'reaction9',
    reactants = ['SiH3(3)', '[Si][Si](51)'],
    products = ['[Si][Si][SiH3](41)'],
    transitionState = 'TS9',
    kinetics = Arrhenius(A=(1.44114e+07,'m^3/(mol*s)'), n=0.100587, Ea=(0,'kJ/mol'), T0=(1,'K'), comment="""Estimated using template (Y_rad;Y_rad) for rate rule (Si_rad;Si_silyl)
Multiplied by reaction path degeneracy 2
Ea raised from -0.8 to 0 kJ/mol."""),
)

reaction(
    label = 'reaction10',
    reactants = ['[Si][Si][SiH2](52)', '[H](16)'],
    products = ['[Si][Si][SiH3](41)'],
    transitionState = 'TS10',
    kinetics = Arrhenius(A=(7.20571e+06,'m^3/(mol*s)'), n=0.100587, Ea=(0,'kJ/mol'), T0=(1,'K'), comment="""Estimated using template (Y_rad;Y_rad) for rate rule (Si_rad;H_rad)
Ea raised from -0.8 to 0 kJ/mol."""),
)

reaction(
    label = 'reaction11',
    reactants = ['[Si][Si][SiH](53)', 'H2(7)'],
    products = ['[Si][Si][SiH3](41)'],
    transitionState = 'TS11',
    kinetics = Arrhenius(A=(7.6e+12,'cm^3/(mol*s)'), n=0, Ea=(3.3472,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Exact match found for rate rule (Si-Si-H;H_H)
Multiplied by reaction path degeneracy 2"""),
)

network(
    label = '28',
    isomers = [
        '[Si]=[SiH][SiH2](34)',
        '[Si][Si][SiH3](41)',
    ],
    reactants = [
        ('SiH3(3)', '[Si]=[Si](27)'),
        ('SiH(11)', 'SiH2Si(12)'),
    ],
    bathGas = {
        'He': 0.25,
        'Ne': 0.25,
        'Ar': 0.25,
        'N2': 0.25,
    },
)

pressureDependence(
    label = '28',
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

