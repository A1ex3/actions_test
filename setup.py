from setuptools import setup, find_packages

setup(
    name='test actions',
    version='0.0.0',
    packages=find_packages(),
    install_requires=[
        'fastapi[all]',
        'pytest',
    ],
)