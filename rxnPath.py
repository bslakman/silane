"""
Viewing a reaction path diagram.

This script uses Graphviz to generate an image. You must have Graphviz installed
and the program 'dot' must be on your path for this example to work.
Graphviz can be obtained from http://www.graphviz.org/ or (possibly) installed
using your operating system's package manager.
"""

import os
import sys

import cantera as ct

# these lines can be replaced by any commands that generate
# an object of a class derived from class Kinetics in some state.
gas = ct.Solution('chem.cti')#chemkin/chem.inp')
gas.TPX = 913.0, 39000, 'SiH4(1):0.00016,Ar:0.99984'
r = ct.IdealGasReactor(gas, energy='off')
net = ct.ReactorNet([r])
T = r.T
n = 0
time = 0
while n<50:#T < 1900:
    print(gas.mole_fraction_dict()['SiH4(1)']/0.00016)
    time += 0.01
    net.advance(time)

    T = r.T

    element = 'Si'

    diagram = ct.ReactionPathDiagram(gas, element)
    diagram.title = 'Reaction path diagram following {0}'.format(element)
    diagram.label_threshold = 0.001
    diagram.threshold = 0.001

    dot_file = 'rxnpath{0}.dot'.format(n)
    img_file = 'rxnpath{0}.png'.format(n)
    img_path = os.path.join(os.getcwd(), img_file)

    diagram.write_dot(dot_file)
    # print(diagram.get_data())

    print("Wrote graphviz input file to '{0}'.".format(os.path.join(os.getcwd(), dot_file)))

    os.system('dot {0} -Tpng -o{1} -Gdpi=200'.format(dot_file, img_file))
    print("Wrote graphviz output file to '{0}'.".format(img_path))

    if "-view" in sys.argv:
        import webbrowser
        webbrowser.open('file:///' + img_path)

    n += 1
