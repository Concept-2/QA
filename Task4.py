from click.testing import CliRunner
from upper_case_file import upper_case_file
import os
#changes working directory to /data
os.chdir("./data")

def test_isupper(file):
    runner = CliRunner()
    
    #creates temporary output file
    result = runner.invoke(upper_case_file, ["--input-file", file, "--output-file", "temp.txt"])
    assert result.exit_code == 0

    try:
        assert open('temp.txt', 'r').read() == open(file.replace('input', 'output'), 'r').read()
        print (file + ' passed')

    #prints out errors complete with file content
    except AssertionError:
        print (file + ' ASSERTION ERROR')
        print (open('temp.txt', 'r').read() + '\n')
        print (open(file.replace('input', 'output'), 'r').read())
        
    #deletes temporary output file
    os.remove('temp.txt')

for i in os.listdir():
    if 'input' in i and i.replace('input', 'output') in os.listdir():
        test_isupper(i)
