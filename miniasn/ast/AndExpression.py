from miniasn.node.Node import Node
from miniasn.node.NodeType import NodeType
from miniasn.token.TokenType import TokenType


class AndExpression(Node):
    first = NodeType.SIMPLE_EXPRESSION

    def __init__(self, simple_expressions):
        super().__init__()
        self.simple_expressions = simple_expressions

    @staticmethod
    def parse(parser, *args, **kwargs):
        simple_expressions = []

        simple_expression = parser.parse_node(NodeType.SIMPLE_EXPRESSION)
        simple_expressions.append(simple_expression)

        while parser.can_parse(TokenType.AND):
            parser.parse_node(TokenType.AND)
            simple_expression = parser.parse_node(NodeType.SIMPLE_EXPRESSION)
            simple_expressions.append(simple_expression)

        return AndExpression(simple_expressions)

    def __str__(self):
        result = str(self.simple_expressions[0])
        for simple_expression in self.simple_expressions[1:]:
            result += ' and {}'.format(simple_expression)

        return result
