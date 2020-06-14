""" I don't plan to post this project to pypi, so this file is only used for
development purposes
"""

from setuptools import setup, find_packages

requirements = ('requests', )

setup(
    name='as_salah',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
)
