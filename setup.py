from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'  # This automatically triggers setup.py

def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements
    '''
    with open(file_path, 'r') as f:
        requirements=f.readlines()
        # This causes '\n' to be added which needs to be removed
        requirements = [req.replace("\n", "") for req in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

setup(
    name='MLProject', 
    version='0.0.1',
    author="Ujjwal",
    author_email='batman.c731@gmail.com',
    packages=find_packages(), 
    install_requires=get_requirements('requirements.txt')
)