from setuptools import setup

setup(
    name='cli',
    version='0.0.1',
    packages=['cli'],
    entry_points={
        'console_scripts': [
            'cli = src.cli.__main__:main'
        ]
    })
