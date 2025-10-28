"""Setup script for DeskTick."""

from setuptools import setup, find_packages
from src import __version__, __author__, __description__

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

with open('requirements.txt', 'r', encoding='utf-8') as f:
    requirements = [line.strip() for line in f if line.strip() and not line.startswith('#')]

setup(
    name='desktick',
    version=__version__,
    author=__author__,
    description=__description__,
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/leixq1024/DeskTick',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Financial and Insurance Industry',
        'Topic :: Office/Business :: Financial :: Investment',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'desktick=main:main',
        ],
    },
    keywords='stock ticker desktop widget investment finance real-time monitoring',
)
