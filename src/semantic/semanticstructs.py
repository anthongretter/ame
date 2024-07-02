from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Node:
    vallex: str
    left: Node
    right: Node

