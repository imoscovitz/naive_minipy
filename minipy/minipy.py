import re
import sys
import warnings

def min(filename, save=True, random_state=42):
    """ Saves and returns a minimized version of a .py file.

        args:
            filename<str>: path and filename of your bloated source code

            save<bool> (optional): autosave the minimized version
            random_state<int> (optional, default=42): does nothing
    """

    if '.py' not in filename:
        warnings.warn(f'IOWarning: minipy is intended for use with .py files. It may not work as intended for {filename}')

    # Read in file, removing whitespace and inline comments, then remove docstrings
    code = []
    with open(filename, "r") as f:
        for line in f:
            line = rm_whitespace(line)
            line = rm_inlinecomments(line)
            code.append(line)
    code = ''.join(code)
    code = rm_docstrings(code)

    # Autosave, if applicable
    if save:
        newfilename = filename.replace('.py','_min.py')
        with open(newfilename, 'w+') as f:
            f.write(code)

    return code

def score(filename):
    with open(filename, 'r') as f:
        oldsize = sys.getsizeof(f.read())
    try:
        with open(filename.replace('.py','_min.py'), 'r') as f:
            newsize = sys.getsizeof(f.read())
    except:
        newsize = sys.getsizeof(min(filename, save=False))

    print(f'You saved {oldsize - newsize} bytes')

def fit_score(filename):
    with open(filename, 'r') as f:
        oldsize = sys.getsizeof(f.read())
    newsize = sys.getsizeof(min(filename, save=True))

    print(f'You saved {oldsize - newsize} bytes')

def rm_whitespace(string):
    for tok in ['\n','\t','\r',' ']:
        string = string.replace(tok,'')
    return string

def rm_inlinecomments(line):
    result = []
    for char in line:
        if char != '#':
            result.append(char)
        else:
            break
    return ''.join(result)

def rm_docstrings(text_block):
    text_block = re.sub(r'""".*?"""', '', text_block)
    text_block = re.sub(r"'''.*?'''", '', text_block)
    return text_block
