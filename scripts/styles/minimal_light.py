# Copyright 2016 David van Gemeren
# Minimal Light syntax highlighter
# MIT license

from pygments.style import Style
from pygments.token import Text, Whitespace, Literal, Keyword, Name, Comment, String, Error, Number, Operator, Generic, Other, Punctuation

color_bg = '#fff'
color_fg = '#000'
color_code = '#00f'
color_content = '#090'
color_accent = '#09c'
color_constant = '#e10'
color_highlight = '#fd0'
color_comment = '#ff8000'
color_neutral = '#888'

class MinimalLight(Style):
    default_style = "bg:#"+color_bg+" "+color_fg
    styles = {

        Text:                       color_fg,
        Whitespace:                 color_fg,
        Error:                      color_constant,
        Other:                      color_fg,

        Keyword:                    color_code,
        Keyword.Constant:           'bold '+color_constant,
        Keyword.Declaration:        'bold '+color_code,
        Keyword.Namespace:          'bold '+color_code,
        Keyword.Pseudo:             'bold '+color_constant,
        Keyword.Reserved:           'bold '+color_code,
        Keyword.Type:               'bold '+color_constant,

        Name:                       color_code,
        # Name.Attribute: (inherit from Name)
        Name.Builtin:               'bold '+color_code,
        Name.Builtin.Pseudo:        color_accent,
        Name.Class:                 'bold '+color_code,
        Name.Constant:              'bold '+color_constant,
        # Name.Decorator: (need an example)
        Name.Entity:                'bold '+color_constant,
        Name.Exception:             'bold '+color_code,
        # Name.Function: (inherit from Name)
        # Name.Label: (inherit from Name)
        Name.Namespace:             'bold '+color_code,
        # Name.Other: (inherit from Name)
        # Name.Tag: (inherit from Name)
        Name.Variable:              color_accent,
        # Name.Variable.Class: (need an example)
        # Name.Variable.Global: (need an example)
        # Name.Variable.Instance: (need an example)

        Literal:                    'bold '+color_constant,
        # Literal.Date: (inherit from Literal)

        String:                     color_content,
        # String.Backtick: (inherit from String)
        # String.Char: (need an example)
        # String.Doc: (need an example)
        # String.Double: (inherit from String)
        String.Escape:              'bold '+color_constant,
        # String.Heredoc: (inherit from String)
        String.Interpol:            color_accent,
        String.Other:               color_accent,
        String.Regex:               color_accent,
        # String.Single: (inherit from String)
        String.Symbol:              color_constant,

        Number:                     'bold '+color_constant,
        # Number.Bin: (inherit from Number)
        # Number.Float: (inherit from Number)
        # Number.Hex: (inherit from Number)
        # Number.Integer: (inherit from Number)
        # Number.Integer.Lon: (inherit from Number)
        # Number.Oct: (inherit from Number)

        Operator:                   color_fg,
        Operator.Word:              color_code,

        # (want to make it semi-transparent, but isn't an option)
        Punctuation:                color_fg,

        Comment:                    'italic '+color_comment,
        # Comment.Multiline: (inherit from Comment)
        Comment.Preproc:            color_neutral,
        # Comment.Single: (inherit from Comment)
        # Comment.Special: (inherit from Comment)

        Generic:                    color_fg,
        Generic.Deleted:            color_constant,
        Generic.Emph:               'bold',
        Generic.Error:              color_constant,
        Generic.Heading:            color_code,
        Generic.Inserted:           color_content,
        Generic.Output:             color_content,
        # Generic.Prompt: (need an example)
        Generic.Strong:             'bold',
        Generic.Subheading:         color_code,
        Generic.Traceback:          color_constant

    }
