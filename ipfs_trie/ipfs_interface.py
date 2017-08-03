import subprocess
import json
import re

import multihash
from hashlib import sha256
from base58 import b58encode

import IPython

def is_installed():
    return subprocess.run(['which', 'ipfs'], stdout=subprocess.PIPE).returncode == 0

def is_running():
    return subprocess.run(['curl', '--silent', 'localhost:5001'], stdout=subprocess.PIPE).returncode == 0

def get_config():
    proc = subprocess.run(['ipfs', 'config', 'show'], stdout=subprocess.PIPE)
    config = json.loads(proc.stdout.decode("utf-8"))
    return config

def get_PeerID():
    return get_config()['Identity']['PeerID']

def add(data_bytes):
    ps = subprocess.Popen(['ipfs', 'add'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    output = ps.communicate(input=data_bytes)[0]
    return output.decode('ascii').split()[1]


def get_ObjectBytes(b58_sha256_hash):
    proc = subprocess.run(['ipfs', 'object', 'get', b58_sha256_hash, '--encoding', 'protobuf'], stdout=subprocess.PIPE)
    return proc.stdout

def get_ObjectDict(b58_sha256_hash):
    proc = subprocess.run(['ipfs', 'object', 'get', b58_sha256_hash, '--encoding', 'json'], stdout=subprocess.PIPE)
    if proc.returncode != 0:
        return None
    return json.loads(proc.stdout.decode('ascii'))

def make_hash(object_bytes):
    hasher = sha256()
    hasherm.update(object_bytes)
    return b58encode(bytes(multihash.encode(hasher.digest(), multihash.SHA2_256)))

def add_link(link_name, orig, ref):
        proc = subprocess.run(['ipfs', 'object', 'patch', 'add-link', orig, link_name, ref], stdout=subprocess.PIPE)
        if proc.returncode != 0:
            return None
        else:
            return proc.stdout.decode('ascii')[:-1] # strip newline

def get_link(link_name, key):
        proc = subprocess.run(['ipfs', 'object', 'links', key], stdout=subprocess.PIPE)
        if proc.returncode != 0:
            return None
        else:
            output = proc.stdout.decode('ascii')[:-1] # strip newline

            expr = re.compile(link_name + "\s*$")
            for line in output.split('\n'):
                if re.search(expr, line):
                    return line.split(' ')[0]
        return None





