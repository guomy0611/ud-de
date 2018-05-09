"""
    this module contains some util functions for processing
    configuration/source files for german specific functionality
    can be extended for other languages in the future
    __author__ = Muyan Guo
"""

import codecs
import os
THISDIR=os.path.dirname(os.path.abspath(__file__))

def load_upos_xpos():

    """loads german specific UPOS-XPOS tagset mapping"""

    f =os.path.join(THISDIR, 'stts2ud.de')
    mapping={}
    with codecs.open(f,"r","utf-8") as f:
        for line in f:
            line=line.strip()
            if not line or line.startswith(u"#"):
                continue

            line = line.strip(',')
            line = line.replace('"', '')
            line = line.split(' => ')

            if line[1] in mapping:
                mapping[line[1]].add((line[0]))
            else:
                mapping[line[1]] = {line[0]}

    return mapping

def load_deprel_upos():

    """loads german specific deprel and pos consistency check rules """

    f = os.path.join(THISDIR, './deprel_upos_consistency.de')
    rules={}
    with codecs.open(f,"r","utf-8") as f:
        for line in f:
            if '=>' in line:
                line = line.strip()
                line = line.split(' => ')
                line[0] = line[0].replace('* ','')
                line[1] = eval_set(line[1])

                rules[line[0]] = line[1]
    return rules

def eval_set(s):

    """ helper-function: convert a set like string "{a,b,c}" to a list {a,b,c} """

    s = s.replace('{', '')
    s = s.replace('}', '')
    s = {elm.strip() for elm in s.split(',')}

    return s

def extract_de_xpos():

    """ helper-function: extract german stts postags as xpos and write in to a file """
    f = 'stts2ud.de'
    xpos=[]
    with codecs.open(f,"r","utf-8") as f:
        for line in f:
            line=line.strip()
            if not line or line.startswith(u"#"):
                continue

            line = line.strip(',')
            line = line.replace('"', '')
            line = line.split(' => ')
            xpos.append(line[0])

    with open('xpos.de','w') as op:
        for t in xpos:
            op.writelines(t+'\n')

if __name__ == '__main__':
    map = load_upos_xpos()
    print(map)

    rules = load_deprel_upos()
    print(rules)

    #extract_de_xpos()
