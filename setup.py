#!/usr/bin/env python
from setuptools import setup, find_packages


setup(
    name='tangent_importer_dashboard',
    version='0.1',
    description='Dashboard for Tangent Importer framework',
    url='http://github.com/tangentlabs/tangent-importer-dashboard',
    author='Costas Basdekis',
    author_email='costas@basdekis.io',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "Django>=1.8,<1.9",
    ],
)
