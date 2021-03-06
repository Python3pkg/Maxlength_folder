#!/usr/bin/env python
# -*- coding: utf-8 -*-


from setuptools import setup, find_packages


with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.md') as history_file:
    history = history_file.read()

requirements = [
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='maxlength_folder',
    version='0.2.1',
    description=('Handle files and folder which exceeds the'
                 'maximum length of filesystems'),
    long_description=readme + '\n\n' + history,
    author="Fabricio Roberto reinert",
    author_email='fabricio.reinert@live.com',
    url='https://github.com/FRReinert/Maxlength_folder',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='maxlength_folder, NTFS, maxlength, filesystem',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests.test_app.tests',
    tests_require=test_requirements
)