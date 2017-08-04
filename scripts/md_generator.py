#!/usr/bin/env python
# -*- coding: utf-8 -*-

# =========================================
# md_generator.py
# Copyright 2017 Christopher Simpkins
# MIT License
# =========================================

# ### [Anonymous Pro](fonts/anonymous-pro)

# [ [License](fonts/anonymous-pro/license.txt) ]

# <img src="images/anonymous-pro-STP.png" width="725">
# <img src="images/anonymous-pro-STPC.png" width="725">
# <img src="images/anonymous-pro-dark.png" width="725">
# <img src="images/anonymous-pro-light.png" width="725">

# Usage
#  md_generator.py > galleryfonts.md

from utilities import fonts

DEFAULT_WIDTH = "725"

repolink_tag_first = '### ['
repolink_tag_second = """](fonts/"""
repolink_tag_third = ')'

license_tag_first = '[ [License](fonts/'
license_tag_second = '/license.txt) ]'

img_tag_first = '<img src="images/gallery/'
img_tag_second = '" width="'
img_tag_third = '">'

markdown_string = ""

for font in fonts.font_list:
    font_string = repolink_tag_first + font[0] + repolink_tag_second + font[1]['filename'] + repolink_tag_third + "\n\n"
    font_string += license_tag_first + font[1]['filename'] + license_tag_second + "\n\n"
    for suffix in ['-STP.png', '-STPC.png', '-dark.png', '-light.png']:
        font_string += img_tag_first + font[1]['filename'] + suffix + img_tag_second + DEFAULT_WIDTH + img_tag_third + "\n"
    font_string += "\n\n\n"

    # add to the markdown string
    markdown_string += font_string

print(markdown_string)
