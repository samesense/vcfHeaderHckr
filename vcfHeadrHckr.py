"""Update vcf header INFO as desired.
   Replaces:
     grep ^# vcf > head
     edit head INFOs
     grep -v ^# > content
     cat head content > vcf

   Ex fix for gemini:
     Change ##INFO=<ID=tot_esp,Number=.,Type=String
     To ##INFO=<ID=tot_esp,Number=1,Type=Float

   Handles multiple INFO replacements:
   python vcfHeadrHckr.py vcfIn vcfOut AA_AC,Number_AAA,Type_BB CDP,XX,YYY
"""
import argparse, re

def updateLine(newInfo, line):
    newNumber, newType = newInfo
    updateNumber = re.sub(r'Number=.+?,', r'Number=%s,' % (newNumber,), line)
    return re.sub(r'Type=.+?,', 'Type=%s,' % (newType,), updateNumber)

def parseID(line):
    return line.split('ID=')[1].split(',')[0]

def modLine(line, infoDict):
    id = parseID(line)
    if id in infoDict:
        return updateLine(infoDict[id], line)
    else:
        return line

def parseInfoArgs(infos):
    ls = [x.split(',') for x in infos]
    return {x[0]:x[1:] for x in ls}

def main(args):
    infos = parseInfoArgs(args.infos)
    with open(args.vcfIn) as f, open(args.vcfOut, 'w') as fout:
        for line in f:
            printLine = True
            if line[0] == '#':
                if '##INFO=' == line[0:7]:
                    print( modLine( line.strip(), infos ),
                           file=fout)
                    printLine = False
            if printLine:
                print(line.strip(), file=fout)

if __name__ == "__main__":
    desc = 'Update header INFO as desired.'
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('vcfIn')
    parser.add_argument('vcfOut')
    parser.add_argument('infos', nargs='+')
    args = parser.parse_args()
    main(args)

