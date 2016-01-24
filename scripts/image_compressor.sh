#!/bin/bash

# image_compressor.sh
# Copyright 2016 Christopher Simpkins
# MIT License

# Executes image compression on png files with the dependencies:

#################################################################
#  imageoptim-cli
#################################################################
#  Project Source : https://github.com/JamieMason/ImageOptim-CLI
#  Please see above project page for dependencies

# imageoptim-cli Usage: imageOptim [options]

# Options:

#   -d, --directory     directory of images to process
#   -a, --image-alpha   pre-process PNGs with ImageAlpha.app *
#   -j, --jpeg-mini     pre-process JPGs with JPEGmini.app **
#   -q, --quit          quit all apps when complete
#   -c, --no-color      disable color output
#   -h, --help          display this usage information
#   -e, --examples      display some example commands and uses
#   -v, --version       display the version number

##################################################################
# ImageOptim
##################################################################
#      URL: https://imageoptim.com/
# CL Usage: https://imageoptim.com/command-line.html


# image_compressor.sh Usage
#
#  Excecute image compression on all png images in the Codeface repository
#  $ ./image_compressor.sh
#
#  Excecute image compression on a set of defined images
#  $ ./image_compressor.sh [image path 1] <image path 2> ...


if [ $# -eq 0 ]; then
	# excecute imageoptim-cli on all png files in the images directory
	find ../images/gallery -name '*.png' | imageOptim -a
else
	for file in "$@";
		do
			if [ -f "$file" ]; then
				# pngquant on requested files
				echo "pngquant on '$file' started"
				pngquant --ext=.png --force --speed=1 --quality=75-100 --skip-if-larger "$file"
				echo "pngquant on '$file' completed successfully"
			else
				echo "'$file' does not appear to be a file." >&2
				exit 1
			fi
		done;
	# ImageOptim all requested post-pngquant files
	open -a ImageOptim "$@"
fi

