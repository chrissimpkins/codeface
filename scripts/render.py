# Copyright (c) 2015  Andrew Kensler with modifications by Chris Simpkins
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS.  IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.


# python render.py -t samplecode/test-pattern.txt -l text -x 1450 -b "#ddddddff" -i test.png -f "Anonymous Pro 16"

import argparse
import codecs
import pygments
import pygments.lexers
import pygments.formatters
import re
import cairo
import pango
import pangocairo

RESOLUTION = 216

# Basic argument parsing

parser = argparse.ArgumentParser(
    description = "Render sample images of fonts using Pango/Cairo.",
    formatter_class = argparse.ArgumentDefaultsHelpFormatter )
parser.add_argument( "-t", "--text", default = "sample.txt",
                     help = "name of sample text to render" )
parser.add_argument( "-l", "--lang", default = "text",
                     help = "Pygments language to interpret sample as" )
parser.add_argument( "-s", "--style", default = "borland",
                     help = "Pygments style to render sample in" )
parser.add_argument( "-r", "--regular", action="store_true",
                     help = "regular only, ignore bold and italic in style" )
parser.add_argument( "-i", "--image", default = "sample.png",
                     help = "name of image to write" )
parser.add_argument( "-f", "--font", default = "monospace 15",
                     help = "Pango specification for font to use" )
parser.add_argument( "-m", "--mode", default = "subpixel",
                     choices = [ "grey", "bilevel", "subpixel" ],
                     help = "antialiasing mode" )
parser.add_argument( "-b", "--background", default = "#ffffffff",
                     help = "background color and opacity" )
parser.add_argument( "-p", "--pad", default = 4, type = int,
                     help = "padding in pixels around image" )
parser.add_argument( "-x", "--width", default = 0, type = int,
                     help = "minimum width of image to generate" )
parser.add_argument( "-y", "--height", default = 0, type = int,
                     help = "minimum height of image to generate" )
args = parser.parse_args()

# Read sample text in (may be utf-8) and optionally syntax highlight it
# with Pygments.  The markup will be adapted for Pango.

with codecs.open( args.text, encoding = "utf-8" ) as source:
    text = source.read().strip( "\n" )
lexer = pygments.lexers.get_lexer_by_name( args.lang )
formatter = pygments.formatters.HtmlFormatter(
    noclasses = True,
    nowrap = True,
    style = args.style )
text = pygments.highlight( text, lexer, formatter )
text = re.sub( "style=\"color: (#[0-9A-Fa-f]{6})(?:; )?",
               "foreground=\"\\1\" style=\"", text )
if args.regular:
    text = re.sub( "style=\"font-weight: bold(?:; )?",
                   "style=\"", text )
    text = re.sub( "style=\"font-style: italic(?:; )?",
                   "style=\"", text )
else:
    text = re.sub( "style=\"font-weight: bold(?:; )?",
                   "weight=\"bold\" style=\"", text )
    text = re.sub( "style=\"font-style: italic(?:; )?",
                   "style=\"italic\" style=\"", text )
text = re.sub( "style=\"background-color: (#[0-9A-Fa-f]{6})(?:; )?",
               "background=\"\\1\" style=\"", text )
text = re.sub( "style=\"\"", "", text )
text = text.strip()

# First pass, find image size to hold the text.

mode = { "grey" : -1,
         "bilevel" : cairo.ANTIALIAS_NONE,
         "subpixel" : cairo.ANTIALIAS_SUBPIXEL
       }[ args.mode ]
pangocairo.cairo_font_map_get_default().set_resolution( RESOLUTION )
surface = cairo.ImageSurface( cairo.FORMAT_ARGB32, 0, 0 )
context = pangocairo.CairoContext( cairo.Context( surface ) )
layout = context.create_layout()
options = cairo.FontOptions()
options.set_antialias( mode )
pangocairo.context_set_font_options( layout.get_context(), options )
layout.set_font_description( pango.FontDescription( args.font ) )
layout.set_markup( text )
width = max( layout.get_pixel_size()[ 0 ] + args.pad * 2, args.width )
height = max( layout.get_pixel_size()[ 1 ] + args.pad * 2, args.height )

# Second pass, render actual image and save it.

surface = cairo.ImageSurface( cairo.FORMAT_ARGB32, width, height )
context = pangocairo.CairoContext( cairo.Context( surface ) )
layout = context.create_layout()
options = cairo.FontOptions()
options.set_antialias( mode )
pangocairo.context_set_font_options( layout.get_context(), options )
layout.set_font_description( pango.FontDescription( args.font ) )
layout.set_markup( text )
context.set_source_rgba(
    int( args.background[ 1 : 3 ], 16 ) / 255.0,
    int( args.background[ 3 : 5 ], 16 ) / 255.0,
    int( args.background[ 5 : 7 ], 16 ) / 255.0,
    int( args.background[ 7 : 9 ], 16 ) / 255.0 )
context.rectangle( 0, 0, width, height )
context.fill()
context.set_source_rgb( 0, 0, 0 )
context.translate( args.pad, args.pad )
context.update_layout( layout )
context.show_layout( layout )
with open( args.image, "wb" ) as result:
    surface.write_to_png( result )
