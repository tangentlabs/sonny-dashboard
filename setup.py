#!/usr/bin/env python
from setuptools import setup, find_packages


setup(
    name='sonny_dashboard',
    version='0.1',
    description='Dashboard for Sonny Importer framework',
    url='http://github.com/tangentlabs/sonny-dashboard',
    author='Costas Basdekis',
    author_email='costas@basdekis.io',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "Django>=1.8,<1.9",
    ],
)
