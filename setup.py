from setuptools import setup, find_packages

setup(
    name="JSFNC",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        'pyinstaller',
    ],
    entry_points={
        'console_scripts': [
            'jsfnc=src.main:main',
        ],
    },
)