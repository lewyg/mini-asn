from miniasn.node.Node import Node
from miniasn.token.TokenType import TokenType


class SimpleType(Node):
    first = [TokenType.UINT,
             TokenType.BITSTRING,
             TokenType.BOOL]

    def __init__(self, type):
        super().__init__()
        self.type = type

    @staticmethod
    def parse(parser, *args, **kwargs):
        type = parser.parse_or_node_list([TokenType.UINT,
                                          TokenType.BITSTRING,
                                          TokenType.BOOL])

        return SimpleType(type)

    def __str__(self):
        return str(self.type)
