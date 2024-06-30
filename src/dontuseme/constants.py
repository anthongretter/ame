import re

RESERVED_WORDS_DIAG: dict = {
    "d": {
        "e": {
            "f": {
                "$": "DEF"
            }
        }
    },
    "c": {
        "a": {
            "l": {
                "l": {
                    "$": "CALL"
                }
            }
        }
    },
    "n": {
        "e": {
            "w": {
                "$": "NEW"
            }
        }
    },
    "i": {
        "f": {
            "$": "IF"
        },
        "n": {
            "t": {
                "$": "INT"
            }
        }
    },
    "e": {
        "l": {
            "s": {
                "e": {
                    "$": "ELSE"
                }
            }
        }
    },
    "p": {
        "r": {
            "i": {
                "n": {
                    "t": {
                        "$": "PRINT"
                    }
                }
            }
        }
    },
    "f": {
        "o": {
            "r": {
                "$": "FOR"
            }
        },
        "l": {
            "o": {
                "a": {
                    "t": {
                        "$": "FLOAT"
                    }
                }
            }
        }
    },
    "s": {
        "t": {
            "r": {
                "i": {
                    "n": {
                        "g": {
                            "$": "STRING"
                        }
                    }
                }
            }
        }
    },
    "r": {
        "e": {
            "a": {
                "d": {
                    "$": "READ"
                }
            },
            "t": {
                "u": {
                    "r": {
                        "n": {
                            "$": "RETURN"
                        }
                    }
                }
            }
        }
    },
    "+": {
        "$": "PLUS"
    },
    "-": {
        "$": "MINUS"
    },
    "*": {
        "$": "TIMES"
    },
    "/": {
        "$": "DIVIDE"
    },
    "%": {
        "$": "MOD"
    },
    "=": {
        "$": "ASSIGN",
        "=": {
            "$": "EQUAL"
        }
    },
    "!": {
        "=": {
            "$": "DIFF"
        }
    },
    ">": {
        "$": "GREATER",
        "=": {
            "$": "GREATEREQUAL"
        }
    },
    "<": {
        "$": "LESS",
        "=": {
            "$": "LESSEQUAL"
        }
    },
    "(": {
        "$": "LPAREN"
    },
    ")": {
        "$": "RPAREN"
    },
    "{": {
        "$": "LBRACE"
    },
    "}": {
        "$": "RBRACE"
    },
    "[": {
        "$": "LBRACKET"
    },
    "]": {
        "$": "RBRACKET"
    },
    ",": {
        "$": "COMMA"
    },
    ";": {
        "$": "SEMICOLON"
    }
}

SEPS = {'+', '-', '*', '/', '%', '=', '==', '!=', '>', '<', '>=', '<=',
        '(', ')', '{', '}', '[', ']', ',', ';'}
#
# PALAVRAS_RESERVADAS = ['def', 'if', 'else', 'print', 'for', 'int', 'float', 'string', 'read', 'return']
# OPERADORES = ['+', '-', '*', '/', '%', '=', '==', '!=', '>', '<', '>=', '<=']
# DELIMITADORES = ['(', ')', '{', '}', '[', ']', ',', ';']
# ESPACOS = [' ', '\n']


STRING_CONSTANT = re.compile(r"'(?:[^'\\]|\\.)*'|\"(?:[^\"\\]|\\.)*\"")
FLOAT_CONSTANT = re.compile(r'[+-]?\d+\.\d+')
INT_CONSTANT = re.compile(r'[+-]?\d+')
IDENT = re.compile(r'[^\W0-9]\w+')
