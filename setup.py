from setuptools import setup
from setuptools import find_packages
###################
### Goobler 2022 ##
###################
# Scripts made by Eric #


setup(
  # the name must match the folder name 'GooblerPKG'
        name="GooblerPKG", 
        version="2.0.15",
        author="Goobler",
        author_email="<admin@goobler.epizy.com>",
        description="The Goobler Python API",
        long_description="Goobler's python API package which you may host your bot on!",
        packages=find_packages(),
        install_requires=['requests', ''], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python', 'api'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)
