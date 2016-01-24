#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import subprocess
from utilities.fonts import font_list

for font in font_list:
    font_name = font[0]
    font_size = font[1]['size']
    font_filename = font[1]['filename']

    # create test pattern command
    tp_command = """python render.py -t specimens/test-pattern.txt -l text -x 2175 -b "#fcfdffff" -i ../images/gallery/""" + font_filename + """-STP.png -f '""" + font_name + """' -p 20"""

    # create compact test pattern command
    tpc_command = """python render.py -t specimens/test-pattern-compact.txt -l text -x 2175 -b "#fcfdffff" -i ../images/gallery/""" + font_filename + """-STPC.png -f '""" + font_name + """' -p 20"""

    # create dark syntax higlighter command
    dh_command = """python render_highlight.py -t specimen/samplecode.c -x 2175 -i ../images/gallery/""" + font_filename + """-dark.png -f '""" + font_name + """' -p 20 --style dark"""

    # create light syntax highlighter command
    lh_command = """python render_highlight.py -t specimen/samplecode.c -x 2175 -i ../images/gallery/""" + font_filename + """-light.png -f '""" + font_name + """' -p 20 --style light"""


    exit_code_tp = subprocess.call(tp_command, shell=True)
    exit_code_tpc = subprocess.call(tpc_command, shell=True)
    exit_code_dh = subprocess.call(dh_command, shell=True)
    exit_code_lh = subprocess.call(lh_command, shell=True)

    if exit_code_tp != 0:
        sys.stderr.write("ERROR: Test pattern image error for the typeface '" + font_name + "'\n")
        sys.exit(1)
    elif exit_code_tpc != 0:
        sys.stderr.write("ERROR: Compact test pattern image error for the typeface '" + font_name + "'\n")
        sys.exit(1)
    elif exit_code_dh != 0:
        sys.stderr.write("ERROR: Dark highlighter image error for the typeface '" + font_name + "'\n")
        sys.exit(1)
    elif exit_code_lh != 0:
        sys.stderr.write("ERROR: Light highlighter image error for the typeface '" + font_name + "'\n")
        sys.exit(1)
    else:
        print(font_name + " image writes completed successfully")

