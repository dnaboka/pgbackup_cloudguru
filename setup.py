from setuptools import find_packages, setup

with open('READMe.md', 'r') as f:
    long_description = f.read

setup(
        name='pgbackup',
        version='0.1.0',
        author='Dima Naboka',
        author_email='dnaboka@gmail.com',
        description='A utility for backing up PGSQL DB',
        long_description=long_description,
        long_description_content_type='text/markdown',
        url='git@github.com:dnaboka/pgbackup_cloudguru.git',
        packages=find_packages('src')
    )

