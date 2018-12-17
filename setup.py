from setuptools import setup

setup(name='word-transversal',
      version='1.0',
      description='Recursively goes through synonyms of the initial words based on provided topics',
      url='https://github.com/Zedjones/word-transversal',
      author='Nicholas Jones',
      author_email='ncj4861@rit.edu',
      license='GPL-2.0',
      packages=[],
      install_requires=[
          'argparse', 'anytree', 'graphviz', 'flask', 'flask_wtf'
      ],
      zip_safe=False)
