ipfs-trie
=============

ipfs-trie is a python utility for storing and querying key-value-pairs via ipfs.  The keys need to be strings whose characters are valid in directory names. A [trie](https://en.wikipedia.org/wiki/Trie) is used to store the value, and it is implemented via a directory structure (see example below).

### Local Caching

When the `add` verb is used, the trie is created `~/.ipfs-trie/<PeerID>/` where `<PeerID>` is the local ipfs node.  The trie is then added to ipfs and pinned.

When the `ask` verb is used, `~/.ipfs-trie/<PeerID>/` is checked to see if the answer is stored locally.  If not, then the indicated peer is asked, and then the relevant trie-path is stored locally, and the value is output the command line.

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
                                      [last key character]
                                                |
                                                v
                                             [value]

If the redirect block doesn't have a link called ipfs-trie-root, then that link will be added.

If the redirect block does have a link called ipfs-trie-root, then that link will be updated to point to the new trie root.

In either case, IPNS will be updated so that the local PeerId points to the redirect block

### Performance

There's a high likelihood of superfluous nodes, which will probably slow things down and waste memory.  Perhaps it would be better to do something like [this](https://github.com/ethereum/wiki/wiki/Patricia-Tree).

No performance tests have been done.

### Example

#### Key Value Pairs

| Key | Value |
|-----|-------|
| foo | qux   |
| bar | quux  |
| baz | quuz  |

#### ipfs-trie Commands

These commands add key-value-pairs under the local ipns namespace

    $ ipfs-trie add foo qux
    $ ipfs-trie add bar quux
    $ ipfs-trie add baz quuz

#### OS Calls

The underlying directory is created like this (this part is handled by ipfs-trie).

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

    $ ipfs-trie ask <PeerID> foo
    qux

    $ ipfs-trie ask <ipfs-node> bar
    quux

    $ ipfs-trie ask <ipfs-node> baz
    quuz

    $ ipfs-trie ask <ipfs-node> corge
    Error: Not Found

### Usage

From the top level directory...

#### Run without installing
`python ipfs-trie`

#### Installation
`python3 setup.py install --record installed_files.txt` in a root shell. After this, the command: `ipfs-trie` will be available from anywhere.

#### Uninstall
`cat installed_files.txt | xargs rm -f && hash -r` in a root shell.
