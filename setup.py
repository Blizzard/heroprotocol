#!/usr/bin/env python
#
# Copyright 2015-2020 Blizzard Entertainment. Subject to the MIT license.
# See the included LICENSE file for more information.
#

import sys
import setuptools
import heroprotocol.build


with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='heroprotocol',
    version=heroprotocol.build.game_version(),
    author='Blizzard Entertainment',
    author_email='HeroesReplays@blizzard.com',
    url='https://github.com/Blizzard/heroprotocol',
    description='Python library to decode Heroes of the Storm replays',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=['heroprotocol', 'heroprotocol.versions',],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Games/Entertainment :: Real Time Strategy',
        'Topic :: Software Development :: Libraries',
        'Topic :: System :: Archiving',
        'Topic :: Utilities',
    ],
    install_requires=['mpyq >= 0.2.5', 'six >= 1.14.0'],
    entry_points={
        'console_scripts': ['heroprotocol = heroprotocol.heroprotocol:main',]
    },
    python_requires='>=2.7',
)
