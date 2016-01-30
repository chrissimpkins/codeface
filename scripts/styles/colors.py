
# Minimal Syntax and Minimal Syntax Dark syntax highlighting themes
#  Color schemes Copyright 2016 David van Gemeren
#  MIT License
#  Minimal Syntax:      https://github.com/burodepeper/minimal-syntax
#  Minimal Syntax Dark: https://github.com/burodepeper/minimal-syntax-dark


class SyntaxHighlighter(object):
    def __init__(self):
        self.light = {
            'bg':         '#ffffff',
            'fg':         '#000000',
            'syntax':     '#0000ff',
            'syntax_alt': '#0000b3',
            'content':    '#009900',
            'variable':   '#0099cc',
            'constant':   '#ee1100',
            'highlight':  '#ffdd00',
            'comment':    '#ff8000',
            'neutral':    '#888888'
        }
        self.dark = {
            'bg':         '#33333f',
            'fg':         '#cccccc',
            'syntax':     '#ffdd00',
            'syntax_alt': '#b39b00',
            'content':    '#00b3cc',
            'variable':   '#ff6600',
            'constant':   '#ff00cc',
            'highlight':  '#ffdd00',
            'comment':    '#888888',
            'neutral':    '#888888'
        }

