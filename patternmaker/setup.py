'''
This is the setup script for galah.  It contains all of the package information
and dependencies
'''
from setuptools import setup,find_packages
import os

pkg_vars  = {}

with open("src/patternmaker/version.py") as fp:
    exec(fp.read(), pkg_vars)

setup(
    #name='galah',
    version=pkg_vars['__version__'],
    license='GNU-3.0',
    author='Amanda Buyan',
    author_email='amanda.buyan@gmail.com',
    description="Something here",
    long_description="Something here",
    long_description_content_type='text/markdown',
    packages=find_packages('src'),
    package_dir={'':'src'},
    url='https://galah.ala.org.au/Python/',
    keywords='galah',
    #'tempfile'
    install_requires=[
        'setuptools',
        'numpy',
        'pandas',
        'pillow',
        'pytest',
        'unittest2py3k',
        'openpyxl'
    ],

    include_package_data = True,
    package_data = {
    # If any package contains *.ini files or *.csv files, include them
    '': ['dmc_numbers_with_hex_codes.csv'],
    },
)