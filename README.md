**Note: this software isn't even alpha, it's just an empy shell for a project.  I'll remove this note when it's even marginally useful**

ipfs_trie
=============

ipfs_trie is a python utility for storing and querying key-value-pairs via ipfs.  A [trie](https://en.wikipedia.org/wiki/Trie) is used to store the value, and it is implemented with a directory structure (see example below).

### Local Caching

When the `add` verb is used, the trie is created `/var/ipfs_trie/<PeerID>/` where `<PeerID>` is the local ipfs node.  The trie is then added to ipfs and pinned.

When the `ask` verb is used, `/var/ipfs_trie/<PeerID>/` is checked to see if the answer is stored locally.  If not, then the indicated peer is asked, and then the relevant trie-path is stored locally, and the value is output the command line.

Removal is not currently supported.

### IPFS Stuff

description pending, here's a sketch:

    PeerId --(ipns)-> [redirect-block] --> [trie-root]
                                                |
                                                v
                                      [first key character]
                                                |
                                                v
                                       (branches omitted)
                                                |
                                                v
                                      [last key character : value]

- If the redirect block doesn't have a link called ipfs_trie_root, then that link will be added.

- If the redirect block does have a link called ipfs_trie_root, then that link will be updated to point to the new trie root.

- In either case, IPNS will be updated so that the local PeerId points to the redirect block

Future feature: Accept PeerID/<trie-name> to allow multiple tries to be stored by a single peer

### Performance

There's a high likelihood of superfluous nodes, which will probably slow things down and waste memory.  Perhaps it would be better to do something like [this](https://github.com/ethereum/wiki/wiki/Patricia-Tree).  But...
 1. Optimize when needed, not up front
 2. I'm lazy
 3. I haven't thought through the implications of having different nodes' tries balanced in different ways (based on incomplete data), the naieve-trie doesn't rebalance, so each node's trie structurally resembles all others'.

To work around this limitation, I recommend using short keys.

No performance tests have been done.

## Example Use

#### Key Value Pairs

| Key | Value |
|-----|-------|
| foo | qux   |
| bar | quux  |
| baz | quuz  |

#### ipfs_trie Commands

These commands add key-value-pairs under the local ipns namespace

    $ ipfs_trie add foo qux
    $ ipfs_trie add bar quux
    $ ipfs_trie add baz quuz

#### OS Calls

The underlying directory is created like this (this part is handled by ipfs_trie).

    $ mkdir -p "f/o"
    $ echo "qux" > f/o/o

    $ mkdir -p "b/a"
    $ echo "quux" > b/a/r

    $ mkdir -p "b/a"
    $ echo "quuz" > b/a/z

#### Directory Tree

    .
    ├── b
    │   └── a
    │       ├── r (contains: "quux")
    │       └── z (contains: "quuz")
    └── f
        └── o
            └── o (contains: "qux")

#### Query Commands

    $ ipfs_trie ask <PeerID> foo
    qux

    $ ipfs_trie ask <ipfs-node> bar
    quux

    $ ipfs_trie ask <ipfs-node> baz
    quuz

    $ ipfs_trie ask <ipfs-node> corge
    Error: Not Found

## Relevant Commands

The commands below are executed from the top level of the repo.

| Command | Action | Root? |
|---------|--------|---------------|
|`python ipfs_trie`| run without installing | no |
|`python3 setup.py install --record installed_files.txt`| install ipfs_trie | yes |
|<code>cat installed_files.txt &#124; xargs rm -f && hash -r</code> | uninstall ipfs_trie | yes |
|`pip install -r requirements_test.txt` | prepare for testing | no |
|`python -m unittest` | runs all tests | no|
|`python -m unittest tests.test_trie.TrieStore.test_dummy1` | run a specific test | no |

- Be sure that the ipfs daemon is running before running unit tests

- If you run ipfs_trie without installing, the directory trie will be written to `~/.ipfs_trie/<PeerId>` which means that separate users will have separate caches

- Once ipfs_trie is installed, the command `ipfs_trie` will be available from anywhere
