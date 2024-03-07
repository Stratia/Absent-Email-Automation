#!/usr/bin/env python3

import setuptools

# https://stackoverflow.com/questions/6967331/how-do-i-install-a-script-to-run-anywhere-from-the-command-line
# Run in CMD: python setup.py develop
# Yes, that's the reason this exists | Use anywhere in any commandline

install_requires = [
        'python-dotenv'
        ]

setuptools.setup(
    name="Absent_Automation",
    version="1.1",
    packages=setuptools.find_packages(),
    install_requires=install_requires,
    entry_points={
        'console_scripts': [
            'Absent = Absent:main',
        ],
    },
    include_package_data=True,
    )