# naive_minipy

A side-effect-laden module for minimizing Python code by removing whitespace

## Installation

To install, use
```bash
$ pip install naive_minipy
```

To uninstall, use
```bash
$ pip uninstall naive_minipy
```

## Usage

```python
>>> import naive_minipy as np
>>> from naive_minipy import min
```

naive_minipy is recursively compatible:
```
>>> min('minipy.py')
importredefmin(filename,save=True,random_state=42):if'.py'notinfilename:raiseIOError('')code=[]withopen(filename,"r")asf:forlineinf:line=
rm_whitespace(line)line=rm_inlinecomments(line)code.append(line)code=''.join(code)code=rm_docstrings(code)ifsave:newfilename=filename.rep
lace('.py','_min.py')withopen(newfilename,'w+')asf:f.write(code)returncodedefrm_whitespace(string):fortokin['\n','\t','\r','']:string=string
.replace(tok,'')returnstringdefrm_inlinecomments(line):result=[]forcharinline:ifchar!='result.append(char)else:breakreturn''.join(result)de
frm_docstrings(text_block):text_block=re.sub(r'','',text_block)text_block=re.sub(r"",'',text_block)returntext_block
```

np implements .score and .fit_score methods:
```
>>> np.fit_score('minipy.py')
You saved 904 bytes
```
