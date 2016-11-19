try:
    from setuptools import setup
except:
    from distutils.core import setup

full_description = """
    s4 is a python based programming framework. The project goals are to 
        - plan and develop organizational level software in a cogent and consistent way.
        - use code generation and JIT compilation to generate bug-free software.
        - unify Machine Learning/AI and conventional, rule-based programming in the same framework.
"""


config = {
    'name'              : 's4',
    'author'            : 'A G',
    'description'       : 'The S4 programming framework',
    'long_description'  : full_description,
    'url'               : 'https://github.com/abhinav-goyal/s4',
    'license'           : 'MIT',
    'install_requires'  : [],
    'package_data'      : {},
}


setup(**config)
