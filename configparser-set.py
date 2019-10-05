#!/usr/bin/python3


import configparser, sys


def printusage():
        print('''Usage:
'''+sys.argv[0]+''' <file> <section> <option> <value>
''')
        sys.exit(1)

def main():
        pcount=len(sys.argv)
        if pcount==5:
                configfile=sys.argv[1]
                section=sys.argv[2]
                option=sys.argv[3]
                value=sys.argv[4]
                config = configparser.ConfigParser()
                config.optionxform = str
                config.readfp(open(configfile))
                print("INFO: old -> " + config.get(section, option)+" (configfile: "+configfile+")")
                config.set(section,option,value)
                print("INFO: new -> " + config.get(section, option)+" (configfile: "+configfile+")")
                with open(configfile, 'wt', encoding='utf8') as newconfigfile:
                        config.write(newconfigfile)
        else:
                printusage()

if __name__=='__main__':
        main()
