from click.testing import CliRunner 
from upper_case_file import upper_case_file

def is_upper():
    runner = CliRunner()
    runner.invoke(upper_case_file, input = 'python upper_case_file.py --input-file C:\\Users\\User\\Desktop\\Congenica\\Task4\\data\\betty.input.txt --output.file C:\\Users\\User\\Desktop\\Congenica\\Task4\\output.txt')
    #print (open('C:\\Users\\User\\Desktop\\Congenica\\Task4\\output.txt'), 'r'.read())

    #Could not figure out how to open a file made through CliRunner, instead of it's output

    #assert result.output == open('C:\\Users\\User\\Desktop\\Congenica\\Task4\\data\\betty.output.txt', 'r').read()

#is_upper()
