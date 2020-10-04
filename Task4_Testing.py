import os

#requires files to be in /data directory
os.chdir("./data")

for i in os.listdir():
    #takes all files with input in name that have their matching output file
    if 'input' in i and i.replace('input', 'output') in os.listdir():
        if open ('betty.input.txt', 'r').read().upper() == open ('betty.output.txt', 'r').read():
            print ('success')
        else:
            print (i + ' failed to match output')
