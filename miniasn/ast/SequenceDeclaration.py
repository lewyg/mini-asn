from miniasn.node.Node import Node
from miniasn.node.NodeType import NodeType
from miniasn.token.TokenType import TokenType


class SequenceDeclaration(Node):
    first = TokenType.SEQUENCE

    def __init__(self, attributes, arguments):
        super().__init__()
        self.attributes = attributes
        self.arguments = arguments

    @staticmethod
    def parse(parser, *args, **kwargs):
        parser.parse_node(TokenType.SEQUENCE)

        arguments = parser.parse_node(NodeType.ARGUMENTS) if parser.can_parse(NodeType.ARGUMENTS) else None

        parser.parse_node(TokenType.CLIP_LEFT_BRACKET)

        attributes = [parser.parse_node(NodeType.ATTRIBUTE)]

        while parser.can_parse(NodeType.ATTRIBUTE):
            attributes.append(parser.parse_node(NodeType.ATTRIBUTE))

        parser.parse_node(TokenType.CLIP_RIGHT_BRACKET)

        return SequenceDeclaration(attributes, arguments)

    def __str__(self):
        return 'SEQUENCE{}\n\t{}'.format(self.arguments,
                                         '\n\t'.join([str(attribute) for attribute in self.attributes]))
