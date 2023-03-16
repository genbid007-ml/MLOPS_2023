from setuptools import find_packages, setup
from typing import List

HYPHEN_E ='-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    this function will get installed all the requirements present in the input file
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        #remove the /n in the file
        requirements=[req.replace("\n", " ") for req in requirements] 

        if HYPHEN_E in requirements:
            requirements.remove(HYPHEN_E)

    return requirements

setup(

name='MLOPS 2023 project',
version='0.0.1',
author='Bidyut BS',
author_email='genbid007.ml@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)