from setuptools import find_packages, setup
from typing import List


HYPEN_E_DOT = "-e ."
def get_requirements(file_path:str)->List[str]:
    
    requirements = []
    
    with open(file_path) as file_obj:
        lines = file_obj.readlines()
        
        for line in lines:
            requirement = line.strip()
            
            if requirement != "" and requirement != HYPEN_E_DOT:           
                requirements.append(requirement)
    
    return requirements

setup(
    name="mlproject",
    version="0.0.1",
    author="chandula",
    author_email="chandulasenevirathna@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
    
)