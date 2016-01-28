

import os

from setuptools import setup, find_packages

from heroprotocol import __version__


setup(
    name='heroprotocol',
    version=__version__,
    author='Blizzard Entertainment',
    author_email='cmstewart@blizzard.com',
    packages=find_packages(exclude=['tests']),
    entry_points={
        'console_scripts': [
            'heroprotocol = heroprotocol.cmdline:main',
        ],
    },
    install_requires=[line.strip() for line in open('requirements.txt')],
    long_description=open('README.md').read(),
    license=open('LICENSE').read(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Topic :: Utilities',
    ],
)