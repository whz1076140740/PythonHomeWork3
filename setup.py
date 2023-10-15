from setuptools import setup, find_packages

import library

#this function read required dependency
#for example: install_requries = ["numpy", ...]
def get_requirements(requirements_path='requirements.txt'):
    with open(requirements_path) as fp:
        #string.strip() clear the character inside .strip()
        return [x.strip() for x in fp.read().split('\n') if not x.startswith('#')]

with open("README.md", encoding= 'utf-8') as readmef:
    long_description = readmef.read()

setup(
    name='library',
    version=library.__version__,
    

    url='https://github.com/whz1076140740/PythonHomeWork3',
    author='wu_hangze',
    author_email='1076140740@qq.com',

    description = "python HW 3 library",
    long_description = long_description,
    long_description_content_type = "text/markdown",

    install_require = get_requirements(),
    classifiers=[
        'Programming Language :: Python :: 3.12.0',
        "Operating System :: OS Independent"
    ],

    #py_modules=['example_lib_1.py'], 
    #This is for a library structure with only single file
    packages = find_packages(),
    setup_requires=['pytest-runner', 'wheel'],
)
