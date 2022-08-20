from setuptools import setup
###################
### Goobler 2022 ##
###################
# Scripts made by Eric #


setup(
  # the name must match the folder name 'verysimplemodule'
        name="verysimplemodule", 
        version=VERSION,
        author="Jason Dsouza",
        author_email="<admin@goobler.epizy.com>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python', 'first package'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)
