# this version updated by RHW in May 2013
"""
make the dot file prettier
"""
import os, sys, re
import subprocess

StripLineLabels=False
if StripLineLabels:
    print "stripping edge (line) labels"


# replace this:
#  s10 [ fontname="Helvetica", label="C11H23J"];
# with this:
#  s10 [ shapefile="mols/C11H23J.png" label="" width="1" height="1" imagescale=true fixedsize=true color="white" ];
 
reSize=re.compile('size=\"5,6\"\;page=\"5,6\"')
reNode=re.compile('(?P<node>s\d+)\ \[\ fontname=\"Helvetica\",\ label=\"(?P<label>[^\"]*)\"\]\;')

rePicture = re.compile('(?P<smiles>.+?)\((?P<id>\d+)\)\.png')
reLabel = re.compile('(?P<name>.+?)\((?P<id>\d+)\)$')

species_pictures=dict()
for picturefile in os.listdir('species'):
    match = rePicture.match(picturefile)
    if match:
        species_pictures[match.group('id')] = picturefile
    else:
        print picturefile, "didn't look like a picture"

directory='.'
for filename in os.listdir(directory):
    if filename.endswith('-pretty'): continue # already done!
    filepath = os.path.join(directory,filename)
    if not os.path.isfile(filepath): continue # skip directories etc.
    if not open(filepath).readline().startswith('digraph'):
        print "Skipping {0} - not a digraph".format(filepath)
        continue
    
    infile=open(filepath)
    prettypath = filepath+'-pretty'
    outfile=open(prettypath,'w')


    for line in infile:
        (line,changedSize)=reSize.subn('size="12,12";page="12,12"',line)
        match=reNode.search(line)
        if match:
            label = match.group('label')
            idmatch = reLabel.match(label)
            if idmatch:
                idnumber = idmatch.group('id')
                if idnumber in species_pictures:
                    line='%s [ image="species/%s" label="" width="0.5" height="0.5" imagescale=false fixedsize=false color="none" ];\n'%(match.group('node'),species_pictures[idnumber])
    
        # rankdir="LR" to make graph go left>right instead of top>bottom
    
        if StripLineLabels:
            line=re.sub('label\s*=\s*\"\s*[\d.]+\"','label=""',line)
            
        # change colours
        line=re.sub('color="0.7,\ (.*?),\ 0.9"',r'color="1.0, \1, 0.7*\1"',line)
            
        outfile.write(line)
    
    outfile.close()
    infile.close()

    try:
        subprocess.check_call(['dot', '-Tpdf', prettypath,  '-O'])
    except subprocess.CalledProcessError:
        print("Error returned by 'dot' when generating graph of the profile statistics.")
        print("To try it yourself:\n     dot -Tpdf {0} -o {0}.pdf".format(prettypath))
    except OSError:
        print("Couldn't run 'dot' to create graph. Check graphviz is installed properly and on your path.")
        print("Once you've got it, try:\n     dot -Tpdf -O {0}".format(prettypath))
    else:
        print("Graph saved to: {0}.pdf".format(prettypath))
