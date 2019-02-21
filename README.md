# naive_minipy

A side-effect-laden module for minimizing Python code by removing whitespace and comments

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

Simply call .min to remove all docstrings, comments, and whitespace:

```python
>>> import naive_minipy as np
>>> from naive_minipy import min
>>> min('mybloatedcode.py')
...
```

It will save and return a minimized version of your code:

```python
>>> %ls
mybloatedcode.py
mybloatedcode_min.py
```

```python
>>> %cat 'mybloatedcode_min.py'

importpandasaspdimportcopyimportmathimportwarningsfromwittgensteinimportbasefrom.baseimportCond,Rule,Rulesetfrom.baseimportrnd,fit_bins
,bin_transform,score_accuracyclassRIPPER:def__init__(self,k=2,prune_size=.33,dl_allowance=64,verbosity=0):self.prune_size=prune_sizeself
.dl_allowance=dl_allowanceself.k=kself.verbosity=verbositydef__str__(self):fitstr=f'withfitruleset'ifhasattr(self,'ruleset_')else'(unfit)
'returnf'<RIPPERobject{fitstr}(k={self.k},prune_size={self.prune_size},dl_allowance={self.dl_allowance})>'__repr__=__str__deffit(self,
df,y=None,class_feat=None,pos_class=None,n_discretize_bins=None,random_state=None):df,self.class_feat,self.pos_class=base.trainset_cla
ssfeat_posclass(df,y=y,class_feat=class_feat,pos_class=pos_class)numeric_feats=base.find_numeric_feats(df,min_unique=n_discretize_bins
...
```

Optional parameters:
```
__save (default=True)__: autosave the minimized version
__random_state (default=42)__: no effect on anything
```

Let's clock the minified version:
```python
>>> %timeit mybloatedcode_min.py

File "mybloatedcode_min.py", line 1
    importpandasaspdimportcopyimportmathimportwarningsfromwittgensteinimportbasefrom.baseimportCond,Rule,Rulesetfrom.baseimportrnd,fit_bin...

    ^ SyntaxError: invalid syntax

0.4 ns ± 0.102 ns per loop (mean ± std. dev. of 7 runs, 100000000 loops each)
```

It's recursively compatible:

```python
>>> min('minipy.py')

importredefmin(filename,save=True,random_state=42):if'.py'notinfilename:raiseIOError('')code=[]withopen(filename,"r")asf:forlineinf:line=
rm_whitespace(line)line=rm_inlinecomments(line)code.append(line)code=''.join(code)code=rm_docstrings(code)ifsave:newfilename=filename.rep
lace('.py','_min.py')withopen(newfilename,'w+')asf:f.write(code)returncodedefrm_whitespace(string):fortokin['\n','\t','\r','']:string=string
.replace(tok,'')returnstringdefrm_inlinecomments(line):result=[]forcharinline:ifchar!='result.append(char)else:breakreturn''.join(result)de
frm_docstrings(text_block):text_block=re.sub(r'','',text_block)text_block=re.sub(r"",'',text_block)returntext_block
```

np also implements .score and .fit_score methods:
```python
>>> np.fit_score('minipy.py')
You saved 904 bytes
```
