from setuptools import find_packages,setup
from typing import List


def get_requirements(file_path:str)->List[str]:
    
    '''
    this fuction will return the list of requirements
    '''
    
    repuirements=[]
    
    with open(file_path) as file_obj:
        requirements=file_obj.readline()
        repuirements=[req.replace("\n","")for req in requirements]
        
    return repuirements
            
    
setup(
    name="MLproject",
    version="0.0.1",
    author="Ravindra",
    author_email="rky251996@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
    
    
    
)
