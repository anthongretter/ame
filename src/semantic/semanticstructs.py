from __future__ import annotations

from dataclasses import dataclass
import pprint


@dataclass
class Node:
    vallex: str
    left: Node
    right: Node

    def __repr__(self, depth=1):
        return_string = [str(self.vallex)]
        for child in [self.left, self.right]:
            if child is None: continue
            return_string.extend(["\n", " " * (depth+1), child.__repr__(depth+1)])
        return "".join(return_string)


if __name__ == "__main__":
    raiz = Node('a', Node('b', None, None), Node('c', None, Node('d', None, None)))
    print(raiz)


    