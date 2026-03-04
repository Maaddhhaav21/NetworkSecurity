'''
this setup.py file is an essential part of the packaging and distributing Python projects. It is used by setuptools, a powerful library that helps developers create and manage Python packages. The setup.py file contains metadata about the project, such as its name, version, author, and dependencies. It also defines how the package should be built and installed.
'''

from setuptools import setup, find_packages
from typing import List

def get_requirements() -> List[str]:
    '''
    This function will return list of requirements from the given file paths
    '''
    requirement_list:List[str] = []
    try:
        with open('requirements.txt', 'r') as file:
            ##Read lines from the file and return as a list
            lines = file.readlines()
            ##Process each line
            for line in lines:
                requirement = line.strip()
                ##ignore the empty lines and -e.
                if requirement and requirement != '-e .':
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print(f"Error: The file requirements.txt was not found.")

    return requirement_list

setup(
    name='NetworkSecurity',
    version='0.0.1',
    author='Madhav',
    author_email="maadhavmanoj21@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)
