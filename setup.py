#!/usr/bin/env python
#
# Copyright 2015-2020 Blizzard Entertainment. Subject to the MIT license.
# See the included LICENSE file for more information.
#

import sys
import setuptools
import heroprotocol.build

install_requires = ['mpyq >= 0.2.5']

setuptools.setup(
    name='heroprotocol',
    version=heroprotocol.build.game_version(),
    author='Blizzard Entertainment',
    author_email='HeroesReplays@blizzard.com',
    url='https://github.com/Blizzard/heroprotocol',
    description='Python library to decode Heroes of the Storm replays',
    packages=[
        'heroprotocol',
        'heroprotocol.versions'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Games/Entertainment :: Real Time Strategy',
        'Topic :: Software Development :: Libraries',
        'Topic :: System :: Archiving',
        'Topic :: Utilities',
    ],
    install_requires=install_requires,
    entry_points={
        'console_scripts': [
            'heroprotocol = heroprotocol.heroprotocol:main',
            'hero_cli.py = heroprotocol.hero_cli:main',
        ]
    },
    python_requires='>=2.6'
)
