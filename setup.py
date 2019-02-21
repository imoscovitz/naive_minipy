import setuptools
setuptools.setup(
  name = 'naive_minipy',
  version = '0.1.0',
  license='MIT',
  description = 'A side-effect-laden module for minimizing Python code by removing whitespace',
  long_description=open('DESCRIPTION.rst').read(),
  author = 'Ilan Moscovitz',
  author_email = 'ilan.moscovitz@gmail.com',
  url = 'https://github.com/imoscovitz/naive_minipy',
  #keywords = ['Classification', 'Decision Rule', 'Machine Learning', 'Explainable Machine Learning', 'Data Science'],
  packages=setuptools.find_packages(),
  install_requires=[
          're'
      ],
  classifiers=[
    'Programming Language :: Python',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7'
  ],
)
