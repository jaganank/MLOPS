from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return  requirements

setup(
    name='DiamondPricePrediction',
    version='0.0.1',
    author='Naveen Kumar',
    author_email='naveenj_kumar@rediffmail.com',
    install_requires=get_requirements(["requirments.txt"]),
    packages=find_packages()
)