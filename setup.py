#!/usr/bin/env python

from setuptools import setup

setup(
    name ='ipfs_trie',
    version ='0.1.0.dev1',
    description = 'Stores and retrieves key value pairs in a trie rooted at an ipns name',
    url = 'https://github.com/MatrixManAtYrService/ipfs_trie',
    author = 'M@ Rixman',
    author_email = 'ipfs_trie@matt.rixman.org',
    license = 'MPL-2.0',
    keywords = 'ipfs ipns key value interface',
    packages = ['ipfs_trie'],
    python_requires ='>=3',
    entry_points = { 'console_scripts' : [ 'ipfs_trie=ipfs_trie.__main__:main' ] }
)
