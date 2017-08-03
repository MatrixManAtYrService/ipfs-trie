import unittest

import ipfs_trie.ipfs_interface as ipfs
import time
from hashlib import sha256
import multihash
from multihash import SHA2_256
from base58 import b58encode

import ipdb
import IPython

def undebug():
    def f() : pass
    ipdb.set_trace = f
    IPython.embed = f

class IPFS(unittest.TestCase):

    def setUp(self):
        self.assertTrue(ipfs.is_installed(), 'ipfs must be installed')
        self.assertTrue(ipfs.is_running(), 'ipfs must be running')

    def test_peer_ID(self):
        peer_id = ipfs.get_PeerID()
        self.assertEqual(peer_id[0:2], 'Qm') # ipfs uses base58 encoded sha2-256
                                          # multihash prefixes 0x12 for sha2-256
                                          # 0x12 is Qm in base58

    # this test fails, see https://discuss.ipfs.io/t/exactly-what-gets-hashed/880/1
    def test_obj_add_hash(self):
        ipfs_hash = ipfs.add(b'hello world')
        obj_bytes = ipfs.get_ObjectBytes(ipfs_hash)

        hasher = sha256()
        hasher.update(obj_bytes)
        my_hash = b58encode(bytes(multihash.encode(hasher.digest(), SHA2_256)))

        self.assertEqual(ipfs_hash, my_hash, "I assume that the ipfs hash is a base58 encoded SHA2_256 multihash of the protobuf for the ipfs object (i.e. data plus links")

    def test_obj_add_json(self):
        hello_hash = ipfs.add(b'hello world')
        obj_dict = ipfs.get_ObjectDict(hello_hash)

        self.assertTrue("Links" in obj_dict.keys())
        self.assertTrue("Data" in obj_dict.keys())
        self.assertEqual(len(obj_dict["Links"]), 0)

        goodbye_hash = ipfs.add(b'goodbye cruel world')
        hello_hash = ipfs.add_link("goodbye", hello_hash, goodbye_hash)

        link_target = ipfs.get_link("goodbye", hello_hash)
        self.assertEqual(goodbye_hash, link_target)

    def not_found(self):

        # so far as I know, this object is not on ipfs
        missing_hash = "QmbZF9JyEckHMtyALnYfknEktXhjCp2k5vFRJX7NswEXFr"
        obj_dict = ipfs.get_ObjectDict(missing_hash)
        self.assertEqual(obj_dict, None)

