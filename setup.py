#!/usr/bin/env python

from setuptools import setup, find_packages

def readme():
  return open('README.md').read()

setup(
  name='genpassword',
  version='0.0.1',
  description='Generate Password.',
  long_description=readme(),
  url='https://github.com/0x9900/genpassword/',
  license='BSD',
  author='Fred C.',
  author_email='github-fred@hidzz.com',
  py_modules=['genpassword'],
  # install_requires=['keyring'],
  entry_points = {
    'console_scripts': ['genpassword = genpassword:main'],
  },
  classifiers=[
    'Development Status :: 2 - Alpha',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7'
  ],
)
