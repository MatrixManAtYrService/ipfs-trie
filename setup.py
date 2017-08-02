#!/usr/bin/env python

from setuptools import setup

setup(
    name ='ipfs-trie-cli',
    version ='0.1.0.dev1',
    description = 'Stores and retrieves key value pairs in a trie rooted at an ipns name',
    url = 'https://github.com/MatrixManAtYrService/ipfs_trie_cli',
    author = 'M@ Rixman',
    author_email = 'ipfs_trie_cli@matt.rixman.org',
    license = 'MPL-2.0',
    keywords = 'ipfs ipns key value interface',
    packages = ['ipfs_trie'],
    python_requires ='>=3',
    entry_points = { 'console_scripts' : [ 'ipfs-trie=ipfs_trie.command_line:main' ] }
)
