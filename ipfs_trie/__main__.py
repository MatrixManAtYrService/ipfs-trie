import sys

usage = """Usage:
    ipfs_trie add <key> <value>

        adds <value> to the keystore under <key>

        (ipfs node must be running locally)

    ipfs_trie ask <name> <key>

        asks the ipfs node at <ipns-name> for <key>
        returns the assiciated value

        (<name> must be an ipfs node configured by ipfs_trie,
        and <key> must have an associated value)
"""

def main(args=None):
    if args is None:
        args = sys.argv[1:]

    if len(args) == 0:
        print(usage)
    else:
        if args[0] == "add":
            print("TODO: ADD")

        elif args[0] == "ask":
            print("TODO: ASK")

        else:
            print(usage)

if __name__ == "__main__":
    main()
